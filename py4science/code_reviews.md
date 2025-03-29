(code_reviews)=
# Code reviews: the lab meeting for code 

While working as a postdoc at CU Boulder I met [Rob
Knight](https://knightlab.ucsd.edu), a professor in biochemistry and
molecular biology who had a strict discipline of doing, in addition to
his group lab meetings, regular code reviews with all of his lab
members. Rob\'s group is extremely active and productive, and I recently
asked him about his continued use of this process. He does still hold
them and explained that he feels they are a key element of his lab\'s
success; he also provided some very useful feedback based on which I put
these notes together.

With Rob\'s permission, I am posting here a set of guidelines that come
from his reply to my questions, which I intend to use in my own work
here at UC Berkeley. I have made minor edits to his notes, but the full
credit of these ideas, fine-tuned and validated over more than 7 years
of practice, goes to Rob, to whom I\'m very thankful for allowing me to
reuse them here. I do claim full credit on any blunders I may have added
in editing.

These meetings bridge research and practical implementation questions:
sometimes the discussion may focus on fundamental algorithmic ideas or
the approach to a problem, other times the problems will be
documentation, testing or implementation clarity. But I feel that as our
research sits on an increasingly large and complex pile of software
tools, many of them written in-house, we must treat these tools with the
attention and expectations of rigor that we have for other parts of the
research work. And the only way to do that is to scrutinize the code
with the same peer-review process that we use for results within a lab
before we put them out in a paper sent for publication (where they do
get further reviewed).

## Presentation guidelines

The most difficult part of writing code is always to make it
understandable to other people, including yourself a few months down the
track. There\'s certainly no shame in finding out that your code wasn\'t
as easy to understand or use as you\'d hoped, so don\'t take it
personally when it happens (which it always does, at least in my
experience), but treat it as an opportunity to improve.

Here\'s some general guidelines for making your code review go smoothly:

- Make sure the motivation for your code is clear. Someone who isn\'t
  intimately involved with your project should understand from the
  module documentation and the comments what you are trying to do, what
  approach you\'re taking, and why they should expect it to work.
- Take some time to prepare a presentation about your code that will
  answer the above questions even for someone who hasn\'t read the code.
  You\'re more likely to get useful feedback, rather than nitpicking
  about syntax, if the audience can see the big picture.
- Get the code sent out at least a few days beforehand along with some
  background about what to look at (if large), whether suggestions
  should be about architecture/implementation/algorithm/requirements,
  etc. Make sure everyone has enough time to read the code beforehand,
  and don\'t send a series of updated versions immediately before code
  review.
- Don\'t try to present too much. 200 lines is an absolute maximum \--
  50 is usually more reasonable.
- Include examples, either as unit tests or standalone in the module\'s
  `__main__` block. It can often be a lot easier to see an example
  working than to figure out the algorithm from the code.
- Ask yourself, before sending the code out, if it could be simpler.
  Break complex routines down into smaller ones, consider using built-in
  functions and data types instead of custom ones, see if you can
  separate complex logic into a dispatch routine and simple individual
  functions, etc. This also generally helps you make the code more
  testable.
- Follow the coding guidelines and Python idioms applicable to your
  group. At UC Berkeley I am following for all of my projects the Python
  style guide encoded in [PEP
  8](http://www.python.org/dev/peps/pep-0008), supplemented where
  necessary (in particular with regards to docstring standards) with the
  [Numpy coding style
  guidelines](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt).
- Take advantage of existing mature code in your group, the Python
  cookbook, and other sources of existing code to get an idea of how to
  do things. Many problems have already been solved for you. It\'s
  always better to reuse well-tested code (if it does what you want)
  than to reinvent the wheel.
- It\'s OK to present code that doesn\'t work yet, or that you think
  needs improvement, as long as you signal this fact very clearly in
  your email sending out the code. If there are specific areas you want
  people to focus on, don\'t keep it a secret \-- it\'s a waste of time
  to give detailed feedback on code that is about to be scrapped.

## Suggestions for the meeting leader

Rob also provided the following tips for the person leading the
meetings, which I think are very valid and complement the general
guidelines above for the entire group. These are mostly about setting
the right tone for the discussion, so that a productive culture develops
where the process can be both rigorous and friendly.

- Keep it a safe environment, i.e. make sure chastising is relatively
  gentle even when deserved (but do point out when code doesn\'t meet
  the required standard \-- frame it as a learning experience though).
- Make sure there\'s a core of vocal participants so it isn\'t always
  you.
- Make it clear when you\'re presenting yourself that your code isn\'t
  perfect, point out some of those imperfections yourself if audience is
  slow to do so, *do* present yourself.
- Patiently explain when things are not wrong but just stylistic
  differences (but make it clear that *some* styles are bad, often
  helpful to e.g. ask people to guess what a function returns from its
  name).
