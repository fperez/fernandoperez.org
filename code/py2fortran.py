"""Utilities to convert python variables into Fortran sources.

The routines in this module enable the quick generation of valid Fortran
source code for variables computed in Python.  This can be handy when writing
Fortran programs which require constants (either scalars or arrays) which are
easier to compute with Python.

The main routines of 'public' interest here are pyvars2str() and
pyvars2file().  The former generates its output as strings, while the latter is
a wrapper around the former which writes directly to a named file.

In all routines, arrays can be written out to Fortran as either 0- or
1-offset."""

__author__ = 'Fernando Perez <Fernando.Perez@colorado.edu>'

import sys
import Numeric as N

# a mapping from Numeric typecodes to their fortran form
fortran_typestrings = { N.Float32 : 'real *4',
                        N.Float64 : 'real *8',
                        N.Int0 : 'integer *1',
                        N.Int16 : 'integer *2',
                        N.Int32 : 'integer *4',
                        N.Int : 'integer *8',
                        }

fortran_formats = { N.Float32 : '% .10e',
                    N.Float64 : '% .20e',
                    N.Int0 : '%d',
                    N.Int16 : '%d',
                    N.Int32 : '%d',
                    N.Int : '%d',
                    }

def zero_out_src(arr_name,shape,arr_offset=1):
    """Return a string with the source to zero out an array.

    Inputs:

      - arr_name: the name of the array to be zeroed out.

      - shape: a tuple with the shape of the array.
    """
    
    # Dict of templates for supported dimensions
    tpl_nd = { 1 : """\
      do ii0__tmp = %(arr_offset)d,%(i0_max)d
        %(arr_name)s(ii0__tmp) = 0
      enddo""",
               2 : """\
      do ii1__tmp = %(arr_offset)d,%(i1_max)d
        do ii0__tmp = %(arr_offset)d,%(i0_max)d
            %(arr_name)s(ii0__tmp,ii1__tmp) = 0
        enddo
      enddo""",
               3 : """\
      do ii2__tmp = %(arr_offset)d,%(i2_max)d
        do ii1__tmp = %(arr_offset)d,%(i1_max)d
          do ii0__tmp = %(arr_offset)d,%(i0_max)d
            %(arr_name)s(ii0__tmp,ii1__tmp,ii2__tmp) = 0
          enddo
        enddo
      enddo""",
               }
    # Get dimensionality and actual template to be used
    ndim = len(shape)
    tpl  = tpl_nd[ndim]
    # get the max indices and unpack them into individual vars
    imax = tuple(N.array(shape) + arr_offset - 1)
    if ndim==1:
        i0_max, = imax
    elif ndim==2:
        i0_max,i1_max = imax
    elif ndim==3:
        i0_max,i1_max,i2_max = imax
    # expand the template and return it
    out = ['c     Auto-generated zeroing of array <%s>' % arr_name,
           'c',
           tpl % vars(),
           'c',
           'c     End auto-generated zeroing of <%s>' % arr_name]
    return '\n'.join(out)

def append_array(name,arr,out,sparse=False,zero_sparse=False,arr_offset=1):
    """Append the data from an array into an output list.  The output list is
    modfied in-place.

    Inputs:

      - name: string to use in value assignments.

      - arr: Numeric array with data.

      - out: Python list which is appended to, with each value of the array
      adding one line to this list.


    Optional:

      - sparse(False): if True, only append to output for non-zero entries of
      the array.

      - zero_sparse(False): if True, generate code to zero out the arrays
      treated as sparse.
    """

    # initial formats and info about the array
    format = fortran_formats[arr.typecode()]
    template = '      %s%%s = %%s ' % name
    append = out.append

    shape = arr.shape
    ndim = len(shape)

    # declare a couple of helper functions using closures to trap locals
    def app_dense(arr,idx,fmt=format,tpl=template,append=append):
        f_idx = tuple(N.array(idx)+arr_offset)
        fnum = (fmt % arr[idx]).replace('e','d')
        append(tpl % (f_idx,fnum))

    def app_sparse(arr,idx,fmt=format,tpl=template,append=append):
        py_idx = tuple(N.array(idx)-arr_offset)
        val = arr[py_idx]
        if val != 0:
            fnum = (fmt % val).replace('e','d')
            append(tpl % (idx,fnum))

    # Select the proper appending routine for sparse/dense arrays
    if sparse:
        append_val = app_sparse
        if zero_sparse:
            append(zero_out_src(name,shape,arr_offset))
        else:
            append('c     WARNING: Only the non-zero elements of <%s> are written'
                       % name)
            append('c')
    else:
        append_val = app_dense

    # Loop over the array, appending source lines for each value
    idx_ranges = [xrange(arr_offset,s+arr_offset) for s in shape]
    idx_ranges = map(xrange,shape)
    if ndim == 1:
        for i in idx_ranges[0]:
            append_val(arr,(i,))
    elif ndim == 2:
        irng,jrng = idx_ranges
        for i in irng:
            for j in jrng:
                append_val(arr,(i,j))
    elif ndim == 3:
        irng,jrng,krng = idx_ranges
        for i in irng:
            for j in jrng:
                for k in krng:
                    append_val(arr,(i,j,k))
    else:
        m_ = 'array <%s> of unsupported dimensionality <%s>' % \
             (name,ndim)
        raise ValueError(m_)
    
def pyvars2str(varnames,ns=None,precision=18,arr_offset=1,
                 sparse=None,zero_sparse=False,join_output=False):
    """Return a pair of strings in valid Fortran format for the given
    variables, or a single string if join_output is True.

    The first string contains the variable declarations and the second
    contains the actual variable definitions.

    Inputs:

    - varnames: a list/tuple of names to be used.

    Optional:
    
    - ns: a namespace where the list of names is to be evaluated, typically
    locals().  If not provided, this function automatically extracts the
    locals() of the caller.

    - arr_offset(1): initial offset for the arrays.  Typically Fortran uses
    1-offset arrays while Python and C use 0-offsets.

    - precision: float precision passed to Numeric's array2string function.

    - sparse: a list of names to treat as sparse arrays.  For these, only the
    elements which are non-zero are actually written out.  WARNING: by
    default, no zeroing is done of other elements.

    - zero_sparse(False): if True, generate code to zero out the arrays
    treated as sparse.

    - join_output(False): if True, the declaration/definition strings are
    merged into a single string.
    """

    # get all variables first
    val = {}
    if ns is None: ns = sys._getframe(1).f_locals
    try:
        for varname in varnames:
            val[varname] = ns[varname]
    except KeyError,key:
        raise KeyError('Variable not found: %s' % key)

    # sparse is a list of names to treat as sparse arrays
    if sparse is None: sparse = []

    # Our values for generating repr().  There's a bug in array2string, so I
    # need to put things into sys and use repr(), which seems to be the only
    # string-generating function which works correctly
    output_line_width = 78
    float_output_precision = precision

    # Don't mess up user settings
    save_olw = save_fop = 0
    if hasattr(sys,'output_line_width'):
        save_olw = 1
        save_olw_val = sys.output_line_width
    if hasattr(sys,'float_output_precision'):
        save_fop = 1
        save_fop_val = sys.float_output_precision

    # Store values in sys
    sys.output_line_width = output_line_width
    sys.float_output_precision = float_output_precision

    # Build the variable declarations
    var_declarations = []
    dec_append = var_declarations.append
    dec_append('c')
    dec_append('c     Variable declarations')
    dec_append('c')
    for name in varnames:
        var = val[name]
        if type(var) == N.ArrayType:
            fortran_shape = []
            for d in var.shape:
                fortran_shape.append('%s:%s'% (arr_offset,arr_offset+(d-1)) )
            fortran_shape = ','.join(fortran_shape)
            dec_append('      %s %s(%s)' % (fortran_typestrings[var.typecode()],
                                        name,fortran_shape))
        elif isinstance(var,float):
            dec_append('      real *8 %s' % name)
        elif isinstance(var,int):
            dec_append('      integer *4 %s' % name)
        else:
            raise ValueError('variable <%s> of unknown type <%s>' %
                             (name,type(var)))
    if sparse and zero_sparse:
        dec_append('c')
        dec_append('c     Auto-generated indices for zeroing-out sparse arrays')
        dec_append('c')
        dec_append('      integer *4 ii0__tmp,ii1__tmp,ii2__tmp')
        dec_append('c')

    # Define actual variable values
    var_definitions = []
    def_append = var_definitions.append
    def_append('c')
    def_append('c     Variable definitions')
    for name in varnames:
        def_append('c')
        var = val[name]
        if type(var) == N.ArrayType:
            append_array(name,var,var_definitions,name in sparse,
                         zero_sparse,arr_offset)
        elif isinstance(var,float):
            fnum = ('% .20e' % var).replace('e','d')
            def_append('      %s = %s' % (name,fnum))
        elif isinstance(var,int):
            def_append('      %s = %s' % (name,var))

    # Restore user settings if we modified them
    if save_olw: sys.output_line_width = save_olw_val
    if save_fop: sys.float_output_precision = save_fop_val

    # Header/footer used to mark each auto-generated string
    c_line = 'c'+'-'*75
    header = [c_line,'c     Begin code automatically created by Python.',c_line]
    footer = [c_line,'c     End code automatically created by Python.',c_line]

    if join_output:
        out_str = '\n'.join(header + var_declarations + var_definitions + footer)
        # We must fix the fact that single-element tuples in
        # python expand to (i,) instead of (i) as strings.
        out_str = out_str.replace(",)",")")
        return out_str
    else:
        # The return value is a pair of strings, which we build by joining the
        # above lists, after tagging them with the header/footer
        vdec_str = '\n'.join(header + var_declarations + footer)
        vdef_str = '\n'.join(header + var_definitions + footer)
        vdef_str = vdef_str.replace(",)",")")

        # Now, return the actual strings
        return vdec_str,vdef_str

def pyvars2file(varnames,fname,**kwargs):
    """Write to a Fortran file the specified list of variables.

    The interface to this routine is otherwise the same as that for
    pyvars2str, see that docstring for details on keyword arguments.  The
    only difference is that the option join_output is unconditinally set to
    true.

    Inputs:

     - varnames: list of variables, passed unchanged to pyvars2str.

     - fname: name of the file to write to.
     """
    kwargs['join_output'] = True
    # Get caller's namespace
    ns = kwargs.get('ns')
    if ns is None: ns = sys._getframe(1).f_locals
    kwargs['ns'] = ns
    
    ffile = open(fname,'w')
    ffile.write(pyvars2str(varnames,**kwargs))
    ffile.write('\n')
    ffile.close()


# some trivially simple tests
if __name__=='__main__':

    def test1():
        import math
        arr_int0 = N.arange(4,typecode=N.Int0)
        arr_int16 = N.reshape(N.arange(4,typecode=N.Int16),(2,2))
        arr_int32 = N.reshape(N.arange(4,typecode=N.Int16),(2,2))
        arr_int = N.reshape(N.arange(4,typecode=N.Int),(2,2))
        arr_float32 = (1.2345*N.reshape(N.arange(4),(2,2))).astype(N.Float32)
        arr_float64 = (-1.2345*N.reshape(N.arange(8),(2,2,2))).astype(N.Float64)
        sparr_int = N.zeros(5)
        sparr_int[1] = sparr_int[3] = 99
        sparr_float = N.reshape(N.zeros(6,typecode=N.Float32),(2,3))
        sparr_float[0,1] = sparr_float[1,2] = 42
        pi = math.pi
        scalar_int = 99
        vdec, vdef = pyvars2str(['arr_int0','arr_int16','arr_int32','arr_int',
                                 'arr_float32','arr_float64','pi','scalar_int',
                                 'sparr_int','sparr_float'],
                                sparse = ['sparr_int','sparr_float'],
                                zero_sparse = True)
        print '*'*75
        print 'Testing with one offsets'
        print
        print vdec
        print vdef
        print '*'*75
        print 'Testing with zero offsets'
        print
        vdec, vdef = pyvars2str(['arr_float32','sparr_int','sparr_float'],
                                sparse = ['sparr_int','sparr_float'],
                                arr_offset = 0,
                                zero_sparse = True)
        print vdec
        print vdef
        
    def test2():
        print '*'*75
        print 'Testing zeroing-out of arrays:'
        print
        print zero_out_src('ww',(10,))
        print zero_out_src('ww',(10,20))
        print zero_out_src('ww',(10,20,30))
        print zero_out_src('ww',(10,20,30),arr_offset=1)

    test1()
    test2()
