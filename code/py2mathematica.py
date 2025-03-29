"""Utilities to convert python variables into Mathematica sources.

The routines in this module enable the quick generation of valid Mathematica
source code for variables computed in Python."""

__author__ = 'Fernando Perez <Fernando.Perez@colorado.edu>'

import sys
import Numeric as N

def pyvars2file(varnames,fname,ns=None,precision=18):
    """Save a list of names to a Mathematica file.

    The resulting file can be used in Mathematica via '<<fname'.

    Inputs:

    - varnames: a list/tuple of names to be used

    - fname: name of mathematica file, typically ending in .m.

    Optional:
    
    - ns: a namespace where the list of names is to be evaluated, typically
    locals().  If not provided, this function automatically extracts the
    locals() of the caller.

    - precision: float precision passed to Numeric's array2string function.

    Caveats:

    - This function is NOT perfect, because Mathematica's floating point
    format requires changing numbers from 1.23e+04 to 1.23^*+04.  This is done
    as a string replacement on 'e', so accidentally strings may end up
    modified (though for normal strings the code tries to avoid this).

    - Mathematica does NOT allow underscores in variable names.  This function
    simply removes them blindly, so if you try to save both 'ab' and 'a_b',
    the second one will overwrite the first."""

    # get all variables first
    if ns is None:
        ns = sys._getframe(1).f_locals
    val = {}
    try:
        for varname in varnames:
            val[varname] = ns[varname]
    except KeyError,key:
        print '*** ERROR ***'
        print 'Variable not found:',key
        print 'Aborting without creating file \'%s\'' % fname
        return

    # Our values for generating repr().  There's a bug in array2string, so I
    # need to put things into sys and use repr(), which seems to be the only
    # string-generating function which works correctly
    output_line_width = 80
    float_output_precision = precision

    # Don't mess up user settings
    try:
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

        # for regular floats
        float_tpl = '%.'+str(precision)+'e'
        
        # if we get this far, we have everything we need for saving
        mfile = open(fname,'w')
        print >> mfile,'(* File automatically created by Python. *)\n'
        for name in varnames:
            var = val[name]
            if type(var) == N.ArrayType: # numeric arrays
                vstr = N.array_repr(var)
                vstr = vstr.replace('[','{').replace(']','}').replace('e','*^')
                vstr = vstr.replace('array(','').replace(')','')
                # hack to remove typecode marks
                if vstr[-4:-2] == ",'":
                    vstr = vstr[:-4]
            elif isinstance(var,str):  # simple strings
                vstr = '"%s"' % var
            elif hasattr(var,'__getslice__'):  # lists, tuples, etc
                vstr = str(var).replace('[','{').replace(']','}').replace('e','*^')
            elif isinstance(var,float):  # single floats
                vstr = (float_tpl % var).replace('e','*^')
            elif isinstance(var,complex):  # complex numbers
                vstr = str(var).replace('e','*^')
            else: # the rest.  This probably won't be valid Mathematica
                  # except for integers.
                vstr = str(var)
            # Save the variable's representation to the Mathematica file, removing
            # all underscores from the name
            print >> mfile,'%s = %s;\n' % (name.replace('_',''),vstr)
        mfile.close()

    finally:
        # Restore user settings
        if save_olw:
            sys.output_line_width = save_olw_val
        if save_fop:
            sys.float_output_precision = save_fop_val

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
        fname = 'py2mathtest.m'
        pyvars2file(['arr_int0','arr_int16','arr_int32','arr_int',
                     'arr_float32','arr_float64','pi','scalar_int',
                     'sparr_int','sparr_float'],fname)
        print 'Test file left in:',fname
        print 'Try loading it in Mathematica with <<%s' % fname

    test1()
