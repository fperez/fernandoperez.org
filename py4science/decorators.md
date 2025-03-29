# Decorators and execution context

Or abusing @ for fun and profit.

:::: note
::: title
Note
:::

These are the notes for a presentation I made on September 16, 2009 at
our UC Berkeley [Py4Science](https://cirl.berkeley.edu/view/Py4Science)
group. Feel free to [email me](Fernando.Perez@berkeley.edu) with any
comments, thoughts or corrections.
::::

## What are Decorators? Quick recap

As [Matthew Brett
says](https://cirl.berkeley.edu/mb312/data_docs/decorating_for_dummies.html),
a decorator is \"a function, that takes a function as input, and returns
a function\" (this is only *mostly* true, as Matthew also clarifies
later, but it will serve for now):

    def deco(func):
        print "I got a function named:", func.func_name
        return func

    @deco
    def sq(x): return x**2

This produces:

    I got a function named: sq

And the function `sq`{.interpreted-text role="func"} still works
normally:

``` ipython
In [3]: sq(3)
Out[3]: 9
```

But a decorator typically modifies the function it gets, it
\'decorates\' it:

    import time
    def timed(func):
        def wrapper(n, **kw):
            st = time.clock()
            out = func(n, **kw)
            print "Time used: %.2f s" % (time.clock()-st)
            return out
        return wrapper

    @timed
    def ssq(n):
        "Sum of squares"
        return sum(i**2 for i in range(n))

Now we automatically get timing info on every call to ssq:

``` ipython
In [2]: ssq(1000)
Time used: 0.00 s
Out[2]: 332833500

In [3]: ssq(100000)
Time used: 0.12 s
Out[3]: 333328333350000L

In [4]: ssq(1000000)
Time used: 1.84 s
Out[4]: 333332833333500000L
```

Unfortunately this messes up introspection on `ssq`{.interpreted-text
role="func"}:

    In [6]: ssq?
    Type:       function
    Base Class: <type 'function'>
    String Form:    <function wrapper at 0x91e302c>
    Namespace:  Interactive
    File:       Dynamically generated function. No source code available.
    Definition: ssq(n, **kw)
    Docstring:
        <no docstring>

So you should use `functools.wraps`{.interpreted-text role="func"} from
the stdlib (thanks to Gael for [reminding
me](http://mail.scipy.org/pipermail/ipython-dev/2009-September/005511.html)
of this on the IPython mailing list discussion that spawned these notes)
:

    import time
    from functools import wraps
    def timed(func):
        @wraps(func)
        def wrapper(*a, **kw):
            st = time.clock()
            out = func(*a, **kw)
            print "Time used: %.2f s" % (time.clock()-st)
            return out
        return wrapper

    @timed
    def ssq(n):
        "Sum of squares"
        return sum(i**2 for i in range(n))

And now you get at least the right docstring (but not the signature):

``` ipython
In [11]: ssq?
    Type:        function
    Base Class:  <type 'function'>
    String Form: <function ssq at 0x91af454>
    Namespace:   Interactive
    File:        Dynamically generated function. No source code available.
    Definition:  ssq(*a, **kw)
    Docstring:
    Sum of squares
```

If you want the whole thing to work right, use Michele Simionato\'s
[decorator](http://pypi.python.org/pypi/decorator) module (available at
PyPI):

    import time
    from decorator import decorator

    @decorator
    def timed(func, *a, **kw):
        st = time.clock()
        out = func(*a, **kw)
        print "Time used: %.2f s" % (time.clock()-st)
        return out

    @timed
    def ssq(n, start=0):
        "Sum of squares"
        return sum(i**2 for i in range(start, n))

And now even full signature information is preserved:

``` ipython
In [7]: ssq?
Type:       function
Base Class: <type 'function'>
String Form:    <function ssq at 0x94e402c>
Namespace:  Interactive
File:       Dynamically generated function. No source code available.
Definition: ssq(n, start=0)
Docstring:
    Sum of squares
```

In summary: if you become a fan of decorators, *use Michele\'s module*,
it rocks. And it should be in the stdlib, if you ask me, because as far
as I\'m concerned `functools.wraps`{.interpreted-text role="func"} is
broken, since it mangles the function signature.

PS - for those paying close attention. What about the source?? It\'s
there, just a little hidden:

``` ipython
In [8]: ssq.undecorated??
Type:       function
Base Class: <type 'function'>
String Form:    <function ssq at 0x8cac17c>
Namespace:  Interactive
File:       /home/fperez/research/code/contexts/t.py
Definition: ssq.undecorated(n, start=0)
Source:
@timed
def ssq(n, start=0):
"Sum of squares"
return sum(i**2 for i in range(start, n))
```

## Now for a twist

While most uses of a decorator return a function, they don\'t *have* to.
The decorator syntax only requires that in:

    @deco1
    def func(): ...

    @deco2(args)
    def func(): ...

`deco1`{.interpreted-text role="func"} be a callable, and that the
result of `deco2(args)` also be a callable, since both will be called
with func as an argument. But there is *no restriction* on the result of
`deco1(func)` or `deco2(args)(func)` itself, as we can see with a simple
example:

    def funnydeco(func):
        return 'Hi, I am a decorator...'

    @funnydeco
    def f(x):
        return x+1

which produces:

``` ipython
In [2]: f(10)
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
TypeError: 'str' object is not callable

In [3]: print f
Hi, I am a decorator...
```

And that opens up a whole lot of interesting possibilities\...

## But first, a detour

Apple\'s [Grand Central
Dispatch](http://arstechnica.com/apple/reviews/2009/08/mac-os-x-10-6.ars/12):

- A kernel-managed set of per-application dynamic threadpools and a
  scheduler for them.
- A library (libdispatch) to provide APIs that let you pass code into
  these thread pools, but with a high-level notion of thread queues.
- An *extension to the C language* called
  [blocks](http://arstechnica.com/apple/reviews/2009/08/mac-os-x-10-6.ars/10)
  that gives C anonymous blocks with local scope as first-class
  entities.

None of this is revolutionary or even new. Yet I\'m willing to bet the
combination will have a tremendous impact, especially since Apple [open
sourced](http://arstechnica.com/open-source/news/2009/09/apple-opens-gcd-challenges-impede-adoption-on-linux.ars)
the GCD libdispatch library and is proposing the blocks extension to the
C standards groups.

:::: note
::: title
Note
:::

Microsoft has [something
similar](http://msdn.microsoft.com/en-us/magazine/cc163340.aspx) in .Net
with C#, though I don\'t know if the scheduling is at the kernel level
like GCD\'s.
::::

Why are we talking about this? A simple code example, this serial code:

``` c
for (i = 0; i < count; i++) { 
    results[i] = do_work(data, i); 
} 

total = summarize(results, count);
```

becomes parallel with tiny changes:

``` c
dispatch_apply(count, dispatch_get_global_queue(0, 0),
  ^(size_t i) {
      results[i] = do_work(data, i);
  }
);

total = summarize(results, count);
```

The only changes are the calls to `dispatch_apply`{.interpreted-text
role="func"} and the new `^{...}` syntax, those are the new fancy C
blocks.

For those of you who are familiar with OpenMP, [this
post](http://www.macresearch.org/cocoa-scientists-xxxi-all-aboard-grand-central)
is a nice followup with an example that compares a simple image blur
done with OpenMP and with GCD. It is unfortunate that the author didn\'t
have 8 or 16 cores to run it on, as getting \'linear speedup\' with N=2
is a bit of a joke, but other than that the post is a clear and
informative example.

## I thought this was a Python meeting and you only used Linux

Coming, coming\... The point is:

- GCD is mostly syntactic sugar.
- But so is Python (you\'re welcome to write all the code for your
  thesis in assembly, I\'ll see you at graduation in 2040).

**SYNTAX MATTERS!!!**

So, can we get that in Python? What do we need?

- A kernel-level thread pool dispatcher? *Nope*.
- A library to access it? *Nope*, but a library can be written.
- Syntax for anonymous blocks? *Nope*, this is Python, not Ruby.

Wait a second, go back to that last one\...

## Syntax in Python for (anonymous) blocks?

How about we compromise and drop the whole \'anonymous\' part. Obama
wants to extend the Patriot act, so anonymity is probably a terrorist
thing, even here in Berkeley. Let\'s make them:

- Named.
- With parameters (like Apple\'s C ones).
- With access to the enclosing scope (like Apple\'s).
- With optional return values (like Apple\'s).

I know! Let\'s call them \"functions\"!

    def outer(a):
        print 'In outer, a=',a
        x = 1
        y = 2
        def func(z):
            print '  In func, z=',z
            print '  I also see x=',x
            return z+x
        return func(a)+y

    outer(10)

    In outer, a= 10
      In func, z= 10
      I also see x= 1

## So, your point is??

That functions already give us everything we need for blocks (minus the
anonymous part, but that\'s OK and it actually has a use).

And the initial mention of decorators had a purpose, too: the part about
decorators not having to return a function. They can do *anything* with
the function they get.

*Including executing it\...*:

    def execute(func):
        print "  Calling function named:", func.func_name
        return func()

    print "About to define a simple function f"

    @execute
    def f():
        return 10

    print "The 'function' f we just defined is:",f

    About to define a simple function f
      Calling function named: f
    The 'function' f we just defined is: 10

## Now onto something more useful

That loop from the GCD example:

    # Consider a simple pair of 'loop body' and 'loop summary' functions:
    def do_work(data, i):
       return data[i]/2

    def summarize(results, count):
       return sum(results[:count])

    # And some 'dataset' (here just a list of 10 numbers
    count = 10
    data = [3.0*j for j in range(count) ]

    # That we'll process.  This is our processing loop, implemented as a regular
    # serial function that preallocates storage and then goes to work.
    def loop_serial():
       results = [None]*count

       for i in range(count):
          results[i] = do_work(data, i)

       return summarize(results, count)

    # The same thing can be done with a decorator:
    def for_each(iterable):
       """This decorator-based loop does a normal serial run.
       But in principle it could be doing the dispatch remotely, or into a thread
       pool, etc.
       """
       def call(func):
          map(func, iterable)

       return call

    # This is the actual code of the decorator-based loop:
    def loop_deco():
       results = [None]*count

       @for_each(range(count))
       def loop(i):
          results[i] = do_work(data, i)

       return summarize(results, count)

    # Test
    assert loop_serial() == loop_deco()
    print 'OK'

    OK

Let\'s summarize the syntactic parallels in isolation, for clarity:

    for i in range(count):
    results[i] = do_work(data, i)

    # becomes:

    @for_each(range(count))
    def loop(i):
    results[i] = do_work(data, i)

A few less trivial examples:

    def traced(func):
        import trace
        t = trace.Trace()
        t.runfunc(func)

and a 2-line change of code:

    def loop_traced():
       results = [None]*count

       @traced  ### NEW
       def func():  ### NEW, the name is irrelevant
           for i in range(count):
               results[i] = do_work(data, i)

       return summarize(results, count)

gives on execution:

``` ipython
In [12]: run contexts.py
 --- modulename: contexts, funcname: func
contexts.py(64):     for i in range(count):
contexts.py(65):         @traced
 --- modulename: contexts, funcname: do_work
contexts.py(10):     return data[i]/2
contexts.py(64):     for i in range(count):
contexts.py(65):         @traced

... etc.
```

This shows how trivial, small decorators can be used to control code
execution. For example, if you are a fan of Robert\'s [fabulous line
profiler](http://packages.python.org/line_profiler), using this trivial
trick you can profile arbitrarily small chunks of code inline:

    def profiled(func):
       import line_profiler
       prof = line_profiler.LineProfiler()
       f = prof(func)
       f()
       prof.print_stats()
       prof.disable()

    def loop_profiled():
       results = [None]*count

       @profiled  # NEW
       def block():  # NEW
           for i in range(count):
               results[i] = do_work(data, i)

       return summarize(results, count)

When run, you get:

``` ipython
In [3]: run contexts.py
Timer unit: 1e-06 s

File: contexts.py
Function: block at line 82
Total time: 1.6e-05 s

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
   82                                               @profiled
   83                                               def block():
   84         5            7      1.4     43.8          for i in range(count):
   85         4            9      2.2     56.2
results[i] = do_work(data, i)
```

## Limitations? No access to enclosing scopes in Python 2.x

With Python 2.x there is at least one real annoyance: the inability to
rebind non-local (but not global) names in an inner scope. This was
fixed with the \'nonlocal\' keyword in 3.0, but for 2.x the following
won\'t work:

    def execute(func):
       return func()

    def simple(n):
       s = 0.0

       @execute
       def block():
       for i in range(n):
           s += i**2

       return s

because you get an unbound local error:

``` ipython
In [13]: run simple

[...]

/home/fperez/research/code/contexts/simple.py in block()
15     def block():
16         for i in range(n):
---> 17             s += i**2
18
19     return s

UnboundLocalError: local variable 's' referenced before assignment
WARNING: Failure executing file: <simple.py>
```

In Python 3, this was fixed and works great:

    def simple(n):
       s = 0.0

       @execute
       def block():
           nonlocal s  ### NEW keyword in Python 3.x
       for i in range(n):
           s += i**2

       return s

## Acknowledgments

These notes are mostly the summary of a long but very useful
[thread](http://mail.scipy.org/pipermail/ipython-dev/2009-September/005485.html)
on the [IPython](http://ipython.scipy.org) [development mailing
list](http://mail.scipy.org/mailman/listinfo/ipython-dev), where I
presented the main points and many others pitched in with very useful
comments and feedback. I\'d like to thank everyone who participated for
their interest, ideas and additional information, and if you find this
topic interesting, I\'d encourage you to have a read of the whole
thread, as there are many more details that I\'ve ommitted here.

And as I mention in that thread, much of my thinking on this problem
stems from discussions with colleagues and seeing other\'s code. Here is
a brief recap of those to whom I owe much of these ideas (minus the
mistakes, on which I hold exclusive rights):

- I\'ve been worrying about scoping and execution control for a while.
  My first \'click\' was a conversation with Eric Jones at Berkeley in
  late 2007, where he pointed out really how the `with` statement could
  be (ab)used for execution management, which they are doing a lot of
  with [Enthought](http://enthought.com)\'s context library
  (BlockCanvas, I think?).
- In March 2008, William Stein implemented for
  [Sage](http://sagemath.org) the `@interact` decorator at the sprint at
  Enthought, using the \'call and consume\' approach to the decorated
  function. This was the first time I saw this pattern used, and it got
  me thinking again about the problem. On the flight back home, I
  implemented for IPython\'s parallel machinery some context managers
  via a different approach: I used the `with` statement. This worked but
  was so nasty that I never really pursued it further (it involved
  brittle stack manipulations and source introspection).
- In September 2008 at Scipy\'08 I had a long talk about the problem
  with Alex Martelli on whether extending the `with` context manager
  protocol with an `__execute__` method to control the actual execution
  of the code would be feasible. This conversation was very
  enlightening, even though it made it fairly clear that the `with`
  approach was probably doomed in the long run. Alex pointed out very
  clearly a few of the key issues regarding scoping that helped me a
  lot.
- Then at SciPy\'09 I had a talk with Peter Norvig again about the same
  problem, so I got the whole thing back in my head.
- And finally, [John Siracusa\'s review of Snow
  Leopard](http://arstechnica.com/apple/reviews/2009/08/mac-os-x-10-6.ars/10)
  at Ars Technica about Apple\'s work with anonymous blocks and Grand
  Central Dispatch make the whole thing click, leading to the
  IPython-dev thread mentioned above and ultimately these notes.

## Summary

:::: note
::: title
Note
:::

There is a certain irony in realizing that *everything* we discuss here
has been available since Python 2.4 (i.e. since November 30 2004!). Yet
I\'ve hardly seen any use \'in the wild\' of this pattern, save for the
isolated case of Sage\'s \@interact (see
[acknowledgments](#acknowledgments)).
::::

Using decorators that consume their functions, we can:

- Declare local (named) blocks that are executed.
- But where we (the decorator) controls the execution context.

This opens up many very interesting possibilities:

- A high-level (GCD-style) API for remote execution via IPython.
  - That can be disabled globally for serial debugging!
- Execution with supervision, timing, modified (shadow) contexts, etc.
- Execution via Cython
- Execution on exotic hardware (GPUs)
- Optional compilation of array expressions via numexpr\...

I hope you all have more ideas! (and that you implement them\...)
