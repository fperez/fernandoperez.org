# Book Review: Expert Python Programming by Tarek Ziadé

**Update**: I\'ve slightly modified the language of this review, which
as my wife correctly pointed out to me, was unnecessarily harsh. While I
stand by my previous evaluation of the book, I think the same things can
be said in a more constructive tone.

*Disclosure*: In December of 2008 I was contacted by Packt publishing
concerning a review of their new book [Expert Python
Programming](http://www.packtpub.com/expert-python-programming/book), by
Tarek Ziadé. What follows is my review of the book based on a copy
provided by the publisher, but for which no compensation of any kind was
given.

Note that I will not do a chapter-by-chapter listing of the book\'s
contents here, since that is readily available both from the book\'s
site and from reviews such as the one by [Ian
Oszvald](http://ianozsvald.com/2009/02/08/review-expert-python-programming-by-packt-2008/)
and that by [James
Stockford](http://baypiggies.net/index_html/user-group-association-program/BookReviews/expert-python-programming-review/).
Instead, I will try to provide my impressions on the strengths and
weaknesses of the book.

## Summary

*Expert Python Programming* covers a list of very interesting topics
regarding real-world development using Python. It assumes a reader who
already knows the basics of the language and covers a number of
important topics, both in the more advanced parts of the language and in
terms of developing applications using Python. There is a strong
emphasis on agile development practices, testing, documentation,
application life cycle management and other aspects of \'real world\'
work. The list of topics covered is excellent, and the book is well
printed and bound.

However, unfortunately it suffers from rather poor editing throughout,
with a broken idea flow that makes for choppy reading. Very few ideas
are properly developed, as the book relies excessively on code snippets,
bullet lists and stand-out info boxes. Ultimately, this gives it more
the feel of a set of notes than that of a coherent volume.

This should not be read as an indictment of the book: the table of
contents alone is a list of \'right things to do\' when using Python,
and there is a great deal of useful material in all of the chapters. If
you are looking for reference material, links and starting points for
further reading, *Expert Python Programming* can be an excellent
resource and well worth your investment. However, if you are searching
for a text that develops complex concepts at length, delving into
details and subtleties, it might not be the ideal tool for you. I hope
this provides a useful picture of the qualities of this book.

## Full review

After reading its table of contents I became very interested in the
book, as it covers a number of important topics for real-world software
development. The book is *not* a basic Python tutorial but instead aimed
at developers who already know the language syntax and are interested
both in using some of the language\'s more advanced features, and in
adopting better practices in Python. The book could be seen as
\"non-beginner-python + agile development practices using Python tools\"
(I use the term *non-beginner* rather than *expert* because more
advanced aspects of the language, such as signature- and
introspection-preserving decorators, or sophisticated metaclass uses,
are not really covered at the *expert* level). The book discusses topics
beyond the basic syntax (naming, class design, good APIs), application
design strategies, and topics that go outside of the language proper:
testing, documentation, automated build systems, multiprocessing,
optimization and profiling, and more.

With this kind of topic list, the book appears as an excellent mix for
doing modern, sustainable software development using tools from the
Python ecosystem (for all of the covered topics, links are provided to
tools that implement them or provide the necessary support). I have to
admit, however, that I ended up disappointed with the actual content. I
hope that these comments will serve as constructive criticism for a
possible second edition, because I really think that this is a *draft*
for a great book, just not a very good one yet.

The book simply feels too much like a collection of notes, links and
snippets about all of its topics, and very few ideas are developed at
enough length to provide genuine insight and understanding. Almost every
single page of the book is a mishmash of code snippets, bullet lists and
stand-out boxes, which makes for difficult reading. I realize that this
is the age of twitter and the 10-second attention span, but for an
\'expert\' book I expected more exposition of ideas with a sustained
train of thought[^1]. As an exercise, I flipped through every single
page of the book, and I counted a total of *four* pages (210, 254, 255
and 331 for the curious) that were made up of full text unbroken by
either a bullet list, a snippet of code or a standout box. I realize
that code examples are actually critical to a programming book, and the
occasional list, summary or highlight is useful. But in this case there
is just too much of it and almost no serious development of the kind of
complex topics that one would expect from an expert level book. Python
is a language that, despite its amazing clarity and simplicity, enables
sophisticated programming approaches and does have subtle corners. This
book unfortunately does not do justice to such topics.

Additionally, the book is not helped by an overall sense of poor
editing, with a fair amount of grammatical errors. I realize that the
author\'s first language may not be English, but there should have been
a much stronger editorial support provided to assist him with the
writing. There are also, unfortunately, technical errors. For example on
p. 55 a decorator called `synchronized` is defined but below, the name
`@locker` is used while no function `locker` was defined. While this
minor error can be easily spotted by a reader, it suggests that the code
snippets in the book were never actually automatically run as part of a
proper test suite that would ensure that the printed code really
executes without errors.

I think that the book suffered from overall insufficient editing,
because it really feels like a fantastic draft with all the right
topics, ideas and tools, that didn\'t quite develop into the book it
could be and was put to press without being fully in shape yet. I really
hope that the author and publisher consider this to be constructive
criticism and revisit the book with a careful eye for a solid second
edition. The topics covered are well chosen and there is a genuine need
for a book like this one. Given that Python continues to grow in a very
healthy way as a programming language, I\'m sure there will be demand
for such a book in the future.

[^1]: I have in mind here books such as Alex Martelli\'s [Python in a
    nutshell](##REF##Python in a
    nutshell) or [Python Cookbook](##REF##Python Cookbook), when I speak
    of a proper exposition of ideas with enough text for the reader to
    feel that something has been genuinely learned.
