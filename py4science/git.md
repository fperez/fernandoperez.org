(git_resources)=
# Version control with Git: resources

If you are not using a version control system for all your software
development, paper writing, research code execution and tracking of the
generated results, you should. There is simply no excuse today for not
using version control as a mechanism for tracking what you are doing
with your source materials and data (be they programming language files,
LaTeX/LyX files, plain text, even data results!). Using version control
frees you from the madness of having directories with files named
`mypaper_version2_20100202_revisions_jim_v3_new_new2.tex`, for one
thing. It gives you a mechanism to synchronize your work with colleagues
without tracking who attached what version when, and a way to seamlessly
replicate your work, including its history, across computers. Using a
version control system is much, much easier than you think, and today's
best systems are powerful, well documented and free.

This page isn't meant to be a tutorial, but rather a summary of useful
resources on using the [Git](http://git-scm.com) software for version
control. Of the systems available today (as of 2010) for version
control, I only recommend people use either git or mercurial; I've
personally chosen git and find it to be an extraordinary tool, though I
have also used mercurial lightly and from what I see regarding its
development and uptake it is also a very good system. Git and mercurial
are ultimately [quite similar in their
architecture](http://mercurial.selenic.com/wiki/GitConcepts), and likely
to become even more alike in everyday use over time, as each team learns
from the other.

I will not go here into historical details about other version control
systems, nor is this meant to encourage a comparison or discussion: I
have extensive experience with CVS, SVN and Bazaar, and only use those
systems today *very* reluctantly, when imposed by external constraints.
Git is simply that much better for *my needs*. Should you feel the urge
to comment on this, please send your message to one of the many online
forums where debates on *this vs that* are welcome, not to me.

## Introductory materials

I suggest you start with my [interactive tutorial aimed squarely at
scientists](http://nbviewer.ipython.org/urls/github.com/fperez/reprosw/raw/master/Version%2520Control.ipynb)
who want to collaborate with a few colleagues on a manuscript, grant
proposal or data analysis project.

In addition, I would recommend the following 'core' reading list, and
below I mention a few extra resources:

1.  The concise [GitRef](http://gitref.org) reference: written by one of
    the authors of the excellent GitHub.com site, it's very compact but
    contains all the key ideas with the right approach. If you only read
    one document, make it this one.
2.  For a bit more detail, see the start of the excellent [Pro
    Git](http://progit.org/book) online book, or similarly the early
    parts of the [Git community book](http://book.git-scm.com). Pro
    Git's chapters are very short and well illustrated; the community
    book tends to have more detail and has nice screencasts at the end
    of some sections.
3.  For a different take, the [Git
    parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html)
    is an easy read that walks you through how you would go about
    building a version control system with a little story. By the end of
    this gentle document, you realize that Git's model is a very sound
    and clean one for the issues of source history control, management
    and collaboration.

If you are really impatient and just want a quick start, this [visual
git tutorial](http://www.ralfebert.de/blog/tools/visual_git_tutorial_1)
may be sufficient. It is nicely illustrated with diagrams that show what
happens on the filesystem.

[Understanding Git
Conceptually](http://www.eecs.harvard.edu/~cduan/technical/git/) is an
excellent document that I found invaluable once I understood the basics.
Git has a reputation for being hard to use, but I have found that with a
clear view of what is actually a *very simple* internal design, its
behavior is remarkably consistent, simple and comprehensible. The user
interface can be sometimes opaque (though it's getting better), but I
think the problems most people have arise from thinking with a
Subversion-type model and trying to simply find the corresponding
mimicking commands in git. Since this often makes a mess, you will be
far better served by understanding a tiny bit of the underlying ideas: a
little time invested in this understanding will pay off in hassle-free
work later.

For windows users, [an Illustrated Guide to Git on
Windows](http://nathanj.github.com/gitguide/tour.html) is useful in that
it contains also some information about handling SSH (necessary to
interface with git hosted on remote servers when collaborating) as well
as screenshots of the Windows interface.

## Other resources

Cheat sheets

:   Two different
    [cheat](http://zrusin.blogspot.com/2007/09/git-cheat-sheet.html)
    [sheets](http://jan-krueger.net/development/git-cheat-sheet-extended-edition)
    in PDF format that can be printed for frequent reference.

<!-- -->

[Git ready](http://www.gitready.com)

:   A great website of posts on specific git-related topics, organized
    by difficulty.

<!-- -->

[QGit](http://sourceforge.net/projects/qgit/): an excellent Git GUI

:   Git ships by default with gitk and git-gui, a pair of Tk graphical
    clients to browse a repo and to operate in it. I personally have
    found [qgit](http://sourceforge.net/projects/qgit/) to be nicer and
    easier to use. It is available on modern linux distros, and since it
    is based on Qt, it should run on OSX and Windows.

<!-- -->

[Git Magic](http://www-cs-students.stanford.edu/~blynn/gitmagic/index.html)

:   Another book-size guide that has useful snippets.

The [learning center](http://learn.github.com) at [Github](http://github.com)

:   Guides on a number of topics, some specific to github hosting but
    much of it of general value.

<!-- -->

A [port](http://cworth.org/hgbook-git/tour) of the Hg book's beginning

:   The [Mercurial book](http://hgbook.red-bean.com) has a reputation
    for clarity, so Carl Worth decided to
    [port](http://cworth.org/hgbook-git/tour) its introductory chapter
    to Git. It's a nicely written intro, which is possible in good
    measure because of how similar the underlying models of Hg and Git
    ultimately are.

<!-- -->

[Intermediate tips](http://andyjeffries.co.uk/articles/25-tips-for-intermediate-git-users)

:   A set of tips that contains some very valuable nuggets, once you're
    past the basics.

## Collaboration: sharing repositories

While Git can be used strictly in 'private' mode, where you only keep
repositories in one computer, you will often want to share your work
with others. The most natural way to do this is to have a repository
located on a system that is always online and to which both parties have
access. This central location hosts a repository that can be read from
and written to by both, and acts as a synchronization point.

The resources above have sections explaining how to configure a server
to publish Git repositories, but for open source projects (or for
private ones by paying a fee), there are websites that provide this
service with minimal hassle. I am most familiar with
[Github](http://github.com), but [Gitorious](http://gitorious.org)
offers similar services.

A noteworthy hosting service is [Indefero](http://www.indefero.net):
while less well-known than Github and Gitorious, its special feature is
that the source code behind the website is itself open source and it
contains support for SVN, mercurial and git as well as a wiki and a bug
tracker. This means that you can run Indefero on your own server, with
as many private repositories as you wish and the typical amenities of a
project (Gitorious is also open source, but has no bug tracker). I use
this for my own [private projects](http://projects.fperez.org), and I
have `some notes
</code/indefero_dreamhost>`{.interpreted-text role="doc"} that you may
find useful on configuring Indefero on your own server.

## For SVN users

If you want a bit more background on why the model of version control
used by Git and Mercurial (known as distributed version control) is such
a good idea, I encourage you to read this very well written
[post](http://www.joelonsoftware.com/items/2010/03/17.html) by Joel
Spolsky on the topic. After that post, Joel created a very nice
Mercurial tutorial, whose [first page](http://hginit.com/00.html)
applies equally well to git and is a very good 're-education' for
anyone coming from an SVN (or similar) background.

In practice, I think you are better off following Joel's advice and
understanding git on its own merits instead of trying to bang SVN
concepts into git shapes. But for the occasional translation from SVN to
Git of a specific idiom, the [Git - SVN Crash
Course](http://git-scm.org/course/svn.html) can be handy.

## Tips

### Better shell support

(Sent by Nate Vack to the nipy mailing list)

Adding git branch info to your bash prompt and tab completion for git
commands and branches; they make git life really brilliant:

- <http://github.com/slawcup/dotfiles/blob/master/.git-completion.bash>
- <http://railstips.org/blog/archives/2009/02/02/bedazzle-your-bash-prompt-with-git-info>

### Embedding Git information in LaTeX documents

(Sent by [Yaroslav Halchenko](http://www.onerussian.com))

I use a Make rule:

    # Helper if interested in providing proper version tag within the manuscript
    revision.tex: ../misc/revision.tex.in ../.git/index
       GITID=$$(git log -1 | grep -e '^commit' -e '^Date:' | sed  -e 's/^[^ ]* *//g' | tr '\n' ' '); \
       echo $$GITID; \
       sed -e "s/GITID/$$GITID/g" $< >| $@

in the top level `Makefile.common` which is included in all
subdirectories which actually contain papers (hence all those
`../.git`). The `revision.tex.in` file is simply:

    % Embed GIT ID revision and date
    \def\revision{GITID}

The corresponding `paper.pdf` depends on `revision.tex` and includes the
line `\input{revision}` to load up the actual revision mark.

### Automatically make local branches track remotes

When checking out a remote branch with a local one, adding \--track will
ensure that the new local branch is automatically a tracking branch. But
if you have an existing local branch and you decide you want to push it
remotely, you can do it once by saying:

    git push <remote> <branchname>

or you can configure things (so the local branch becomes a tracking one
with):

    git config branch.<branchname>.remote <remote>
    git config branch.<branchname>.merge refs/heads/<branchname>

Note that as of git 1.7, this can be done with the simpler command:

    git branch --set-upstream <branchname> <remote>/<branchname>

and in all of these, it's possible to set the remote and local branch
names to be different, in case there's a conflict with your local name
already existing in the remote.

Using:

    git config branch.autosetupmerge true

Tells `git-branch` and `git-checkout` to setup new branches so that
`git-pull` will appropriately merge from that remote branch.
Recommended. Without this, you will have to add `--track` to your branch
command or manually merge remote tracking branches with "fetch" and
then "merge".

### git export

Git doesn't have a native export command, but this works just fine:

    git archive --prefix=fperez.org/  master | gzip > ~/tmp/source.tgz

Setting default push/pull:

    (master)maqroll[0203_lecture2]> git push
    fatal: The current branch master is not tracking anything.

So do this:

    git config branch.master.merge refs/heads/master
    git config branch.master.remote origin

and now things work:

    (master)maqroll[0203_lecture2]> git push
    Counting objects: 8, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (6/6), done.
    Writing objects: 100% (6/6), 84.82 KiB, done.
    Total 6 (delta 0), reused 0 (delta 0)
    To git@gfif.udea.edu.co:mscomp-2010.git
       807d520..0a8e2d2  master -> master

### Interactive Rebase

One of the neat things about git is that you can modify your commits
before you push them up to a public, shared repository. Let's say
you've made 10 commits to your local git repository, but you want it to
look like two when it gets pushed up. All you need to do is type:

    git rebase -i HEAD~10

And git will launch your `$EDITOR` and allow you to perform what's
referred to as an "interactive rebase."
