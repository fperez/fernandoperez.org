(indefero_dreamhost)=
# Sharing Git repositories on Dreamhost with InDefero

This document explains how to install the
[InDefero](http://www.indefero.net/) project management system on a
shared host like Dreamhost. They should also be useful for any other
self-contained deployment with minor adjustments, as I've tried to
explain in detail a number of points that weren't too clear in the
original documentation. While these notes focus on Git, InDefero also
supports Mercurial and SVN backends; the installation part of this
document may still be useful to you even if you intend to use either of
those backends.

I wanted to have a way of hosting my own Git repositories and projects
for collaboration with colleagues. While I already use
[github](http://github.com/fperez) for open source projects, I wanted an
easy solution for private collaboration. For this type of work I don't
need all the bells and whistles of Github, my requirements are pretty
simple:

- Hosting multiple git repositories.
- Open source code I can run on my own server.
- The ability to add users and have different users on different
  projects, without needing to give each user a real shell account on
  the server.
- Basic code management features: source viewing, change log and
  commits.
- A few project documentation and ticket managemet features are welcome,
  but not a deal breaker.

I looked around quite a bit, and InDefero seemed to fit the bill best.
The various \*Forge alternatives are enormous beasts, from what I found
online Trac's git support may still be a bit flaky (I found
discouraging comments about the plugin), Redmine looks neat but it
requires a full Rails stack, which I'm not really interested in getting
into, and gitosis may be just a tad too bare bones for what I wanted.
But InDefero kept appearing as a good balance of the above, so I decided
to give it a try. I'd summarize it as a lightweight, google-code-like
project management system whose git backend design is inspired by
gitosis. It also supports Hg and SVN backends, though I'm not
interested in those and won't discuss their configuration here (I
turned them off).

So far I have been very satisfied in that I think it does precisely what
I need. There are one or two minor things I'd like to have that I miss
from Trac, but in the end they are all sugar I can live without, since
they involve git history and log manipulations I can easily do with a
local client.

The one thing that wasn't too easy was the installation: the
documentation isn't the best, the installation instructions are
scattered across various documents, and a number of key steps are not
explained at all (not even mentioned), so it took me a fair amount of
time to get the whole thing working. I am putting together these notes
in the hope they save someone else time, and the InDefero team is
welcome to use any or all of this in their own documents. I estimate
that with a document like this one, you should be able to start from
scratch and configure an entire setup in 2-4 hours, assuming you are
comfortable working in a Linux command-line environment and are used to
building software from source.

Please let me know of any inaccuracies in this document so I can correct
them for the benefit of others.

## Preliminaries

The key sets of instructions that this document complements are:

- [InDefero general
  installation.](http://projects.ceondo.com/p/indefero/page/Installation)
- Installation on [Dreamhost with Mercurial
  backend](http://projects.ceondo.com/p/indefero/page/Installation-Dreamhost-Mercurial):
  this comes closest to our needs, but it's missing a few key pieces of
  information. Still, if something is missing in my notes, see this
  document.
- Configuring [the InDefero Git
  backend](http://projects.ceondo.com/p/indefero/page/InstallationScmGit):
  another piece of the puzzle.
- The [Dreamhost notes on Git](http://wiki.dreamhost.com/Git): they may
  be useful to you, though I think all of the pieces regarding git are
  contained here.

Hopefully if I missed something, the above should let you figure out the
whole thing.

For everything below, I have set the variable:

    PREFIX=$HOME/usr/local

and I have a set of bash utilities that configure my various `*PATH`
variables so this is a valid installation prefix for me, so all installs
will be done using `--prefix=$PREFIX`. This means that the following
path variables are all properly configured:

    PATH: binary execution
    LD_LIBRARY_PATH: dynamic linker search path
    LIBRARY_PATH: static linking by gcc (like -L)
    CPATH: generic include path for gcc (like -I), used for all languages
    C_INCLUDE_PATH: C-specific include path, after CPATH
    CPLUS_INCLUDE_PATH: C++-specific include path, after CPATH
    PYTHONPATH: search path for python packages

I also use a little python script called
[unpack](http://arctrix.com/nas/python/unpack) that knows how to unpack
zip, tar, gzip, bz2 and other formats with a single call, so I don't
have to constantly remember what to type. If you don't use `unpack`,
simply substitute the appropriate `tar/unzip` commands as needed.

## Dreamhost configuration

This section contains the various things you need to do on the Dreamhost
account, some of them via the control panel, some locally on the shell.
Basically, you will need:

- A custom domain for your InDefero install, along with a set of
  directories for it.
- A MySQL database.
- A new user whose purpose will be only to manage the Git repositories,
  and who will receive the SSH keys of your InDefero users.

We'll now see these in detail.

### Domain configuration and file layout

Since on a shared host I can't install in `/home/www` as the default
instructions suggest, I made a separate directory for the InDefero
installation, along with a sub-domain pointing to it. In these
instructions, I will use `example.com` as the generic domain and `site`
for the subdomain hosting the InDefero site, substitute your values
accordingly.

If the main site is called `http://example.com`, then I created a
subdomain in the Dreamhost panel called `http://site.example.com`, wich
was pointed to the directory `$HOME/example.com/site/www` as the serving
directory. The extra `www` subdirectory is meant to host the actual
public files (akin to `/var/www` in a non-shared host), while
`$HOME/example.com/site` holds the various files of the InDefero
install, git repositories, etc. Specifically, in my case, the layout of
`$HOME/example.com/site` is:

    drwxrwxr-x 3 2009-11-30 18:31 git_repos/
    drwxrwxr-x 2 2009-11-28 21:51 idf_upload/
    drwxrwxr-x 2 2009-11-28 21:51 idf_upload_attach/
    lrwxrwxrwx 1 2009-11-28 17:14 indefero -> indefero-0.8.8/
    drwxrwxr-x 8 2009-11-29 21:38 indefero-0.8.8/
    drwxrwxr-x 3 2009-12-01 03:41 mysql-dumps/
    lrwxrwxrwx 1 2009-11-28 23:50 pluf -> pluf-master-091126/
    drwxrwxr-x 7 2009-11-28 17:14 pluf-master-091126/
    drwxrwxr-x 2 2009-11-28 23:37 www/
    drwxrwxr-x 3 2009-11-30 18:00 tmp/

The `www/` directory where files actually get served from only contains:

    .htaccess -> ../indefero/www/.htaccess
    favicon.gif
    favicon.ico
    index.php -> ../indefero/www/index.php
    media -> ../indefero/www/media/

A local directory is needed for the actual git repositories. The
InDefero suggested layout can't be used on a shared host, which is why
there is a `git_repos` subdirectory shown above. This will be put in the
InDefero config file later.

The `mysql-dumps` directory will be used to store backups of our
database, as explained below.

:::: note
::: title
Note
:::

I kept the main `indefero` and `pluf` directories as symlinks to the
unpacked versions I downloaded, to make upgrades easier by repointing a
symlink once things are tested to work (and to make backing off a
problem a little easier). I also created a git repo for each of indefero
and pluf upon download, so that I can track my local changes as patches
on git, which hopefully will make it easiet to upgrade by showing me
precisely what I changed from the default install.
::::

### MySQL

One thing the instructions didn't mention even in passing, is the
separate MySQL configuration steps required. This may be common
knowledge for someone used to PHP, but it wasn't for me. Using the
Dreamhost panel, I made an SQL database with:

    User: USER
    Host: mysql.site.example.com
    DB  : examplecom_site

For reference, the local login command is:

``` bash
mysql -u USER -p -h mysql.site.example.com examplecom_site
```

### Local user for Git management

We need a user to manage the git transactions. All tutorials I've found
suggest the creation of a dedicated user called `git`. On dreamhost this
username is already taken, so I made another user (call it `git2`), and
also created a custom group to which both `git2` and my normal user will
belong. As long as this information is given to the proper InDefero
config variables, the actual name of the user is irrelevant.

In the git user's home directory, don't forget to make the `.ssh`
directory with the proper permissions and make an empty
`authorized_keys` file. The InDefero instructions for the SyncGit plugin
explain this, but they assume you have sudo access. On a shared host
this isn't the case, so you must do it manually by logging in as the
new user, and then running the rest of the commands. For reference
(substitute `git2` with the name of your git user):

``` bash
su - git2  # become the new user manually
cd
mkdir .ssh
touch .ssh/authorized_keys
chmod 0700 .ssh
chmod 0600 .ssh/authorized_keys
exit
```

:::: note
::: title
Note
:::

On the Dreamhost panel, when creating the new user, do *not* select
"enhanced security", because we need this new user to be able to share
a group with the normal user, and if I understand correctly, "enhanced
security" would lock down the new user too much.
::::

## Installing all the prerequisites

### OpenSSL and Curl (for Git)

As suggested by [this
post](http://www.ivankuznetsov.com/2009/07/setting-up-ruby-rails-git-and-redmine-on-dreamhost.html),
I built OpenSSL and Curl, as they provide some extra functionality to
the Git we'll build (the one on Dreamhost is very old). In my case they
may not have been 100% necessary, as right now I don't intend to have
my InDefero repositories pulling, but it's easy enough to do as part of
the whole build. They are perfectly straightforward. First, the latest
openssl:

``` bash
wget http://www.openssl.org/source/openssl-0.9.8l.tar.gz
unpack openssl-0.9.8l.tar.gz
cd openssl-0.9.8l
./config shared zlib --prefix=$PREFIX
make
make install
```

And similarly for Curl:

``` bash
wget http://curl.haxx.se/download/curl-7.19.7.tar.gz
unpack curl-7.19.7.tar.gz 
cd curl-7.19.7/
./configure --prefix=$PREFIX --with-ssl=$PREFIX
make
make install
```

If you have symbol version problems with OpenSSL, you may find the
following notes by [Jacobo de Vera](http://blog.jacobodevera.com) useful
(thanks for the contribution!):

The upstream version of OpenSSL does not include versioning symbols,
since this causes problems when more than one version of a library is
present, the versions of openSSL that are shipped with the main distros
are patched to include versioning symbols. One of the symptoms of this
is having those error messages output whenever a tool that uses OpenSSL
is executed:

    $ php
    php: /home/user/run/lib/libssl.so.0.9.8: no version information
    available (required by php)
    php: /home/user/run/lib/libcrypto.so.0.9.8: no version information
    available (required by php)
    php: /home/user/run/lib/libcrypto.so.0.9.8: no version information
    available (required by /usr/lib/libc-client.so.2002edebian)
    php: /home/user/run/lib/libssl.so.0.9.8: no version information
    available (required by /usr/lib/libc-client.so.2002edebian)
    php: /home/user/run/lib/libssl.so.0.9.8: no version information
    available (required by /usr/lib/libcurl.so.3)
    php: /home/user/run/lib/libcrypto.so.0.9.8: no version information
    available (required by /usr/lib/libcurl.so.3)

What I have done to avoid this, since I compiled my own OpenSSL in order
to build a newer version of GIT (to replace the default one provided by
Dreamhost), is to follow the steps that distros do, described in a
comment here:

    > http://rt.openssl.org/Ticket/Display.html?id=1222&user=guest&pass=guest
    > For that to happen I introduced a version script openssl.ld with the
    > following contents:
    >
    > OPENSSL_0.9.8 {
    > global:
    > *;
    > };
    >
    > It has to be in the toplevel directory and in the engines directory.
    >
    > The SHARED_LDFLAGS get the additional options
    > -Wl,--version-script=openssl.ld

SHARED_FLAGS is a variable in the Makefile that is generated by config.
After installing this version, the errors disappear.

### Git

The [dreamhost wiki page on git](http://wiki.dreamhost.com/Git) has more
details, including the NO_MMAP suggestion to prevent dreamhost from
killing git processes that access large files via mmap (this triggers a
false positive on their automatic memory police). In my case, I built
v1.6.5.3. After unpacking the sources, I used:

``` bash
./configure --prefix=$PREFIX --with-openssl=$PREFIX --with-curl=$PREFIX
make NO_MMAP=1 install
```

Note that you *must* give the NO_MMAP flag in the install step, else git
will get rebuilt if you only give it in the make step and then try to
run a simple `make install`.

### PEAR and PHP tools

The indefero docs put this later, but to be 100% sure that all
subsequent pear/php commands run using the proper versions, I think
it's safest to first set up the environment by putting this into the
bashrc file and reloading:

``` bash
# PEAR/PHP install at dreamhost
export PHP_PEAR_PHP_BIN=/usr/local/php5/bin/php
export PATH=$HOME/usr/pear:/usr/local/php5/bin:$PATH
```

Now, we can do a local pear install. It seems pear also needs some
caching directories, and I don't know enough about it to be sure it's
safe to have the caching directories below the root pear path, so I'm
keeping them separate. I made the following directories:

``` bash
mkdir -p ~/usr/var/pear/cache
mkdir -p ~/usr/var/pear/temp
```

`~/usr/pear` will be the root pear tree, and `~/usr/var` will hold
server-style data in a single location, and will use that for the PEAR
temporary directories. The indefero installation instructions suggest
using `~/tmp/pear`, but I don't like keeping anything that I can't
simply destroy on `~/tmp`, so I used this layout instead.

Now I can create the pear config:

``` bash
pear config-create ~/usr/ ~/.pearrc
pear config-set download_dir ~/usr/var/pear/cache/
pear config-set cache_dir ~/usr/var/pear/cache/
pear config-set temp_dir ~/usr/var/pear/temp/
```

With this configured, I can now run the install and it all worked fine:

``` bash
pear install -o PEAR
pear install --alldeps Mail
pear install --alldeps Mail_mime
```

A quick check gives me:

    [usr]> pear list
    INSTALLED PACKAGES, CHANNEL PEAR.PHP.NET:
    =========================================
    PACKAGE          VERSION STATE
    Archive_Tar      1.3.3   stable
    Auth_SASL        1.0.3   stable
    Console_Getopt   1.2.3   stable
    Mail             1.1.14  stable
    Mail_Mime        1.5.2   stable
    Mail_mimeDecode  1.5.0   stable
    Net_SMTP         1.3.4   stable
    Net_Socket       1.0.9   stable
    PEAR             1.9.0   stable
    Structures_Graph 1.0.3   stable
    XML_Util         1.2.1   stable

The above worked for me, but [Jacobo](http://blog.jacobodevera.com)
notes that he actually needed to do a full PEAR install, his notes are
below in case you also need a from-scratch PEAR build (still assuming
the PATH configuration listed above):

The version of PEAR that is currently available in DreamHost is so old
that `Archive_Tar`, which is a dependency of the newer PEAR, will not
accept to be installed.

I wanted a clean PEAR installation, like the ones resulting from running
`pear install -o PEAR`, but, ironically, first I needed a newer PEAR :)

I created a temp directory `~/tmpear` and then ran this:

``` bash
cd ~/tmpear
curl http://pear.php.net/go-pear | php
```

Said yes to everything but changed the installation prefix to be
`$HOME/tmpear`. Once that was finished, ran this:

``` bash
$HOME/tmpear/bin/pear config-create $HOME/usr .pearrc
$HOME/tmpear/bin/pear install -of PEAR
```

Notice the -f flag, otherwise it won't reinstall it:

``` bash
rm -rf $HOME/tmpear
```

I then installed the rest of the needed packages:

``` bash
pear install -a Mail
pear install -a Mail_Mime
```

## Install and configure Pluf/InDefero

Once I had the file layout ready, for the actual installation of Pluf
and Indefero, I followed the instructions as listed in part 3 of the
InDefero
[Dreamhost/Mercurial](http://projects.ceondo.com/p/indefero/page/Installation-Dreamhost-Mercurial/)
instructions pretty much to the letter. That section describes fairly
well the changes needed to the generic InDefero install (explained
[here](http://projects.ceondo.com/p/indefero/page/Installation)).

This is the part where most of the work goes, in editing the
configuration of the `conf/idf.php` file (along with a few changes to
`path.php`)

In the `conf/idf.php` file, I created this block of variables that
summarizes most of my configuration:

``` php
# fperez - variables
$fp = 'example.com';
$fp_home = '$HOME';
$fp_site = '$HOME/example.com/site';
$fp_git_user_home = '/home/git2';
$fp_git_repos = "$fp_site/git_repos";
$fp_site_url = 'site.example.com';
$fp_mail_user = 'nobody@nowhere';
$fp_db_login = 'USER';
$fp_db_password = '???';
$fp_db_server = "mysql.$fp_site_url";
$fp_database = 'examplecom_site';
```

Then, with those variables I constructed the values for everything below
in the actual file, minimizing repetition of paths and making the whole
thing a bit easier to understand (for me).

In particular, don't forget that the MySQL information must then be
properly put into the php configuration file also:

``` php
# Database configuration
$cfg['db_login'] = $fp_db_login;
$cfg['db_password'] = $fp_db_password;
$cfg['db_server'] = $fp_db_server;
$cfg['db_version'] = '5.0'; # Only needed for MySQL
$cfg['db_table_prefix'] = 'indefero_';
$cfg['db_engine'] = 'MySQL';
$cfg['db_database'] = $fp_database;
```

A few other configuration variables that rely on the ones above, and on
the directory layout previously explained for our site:

``` php
$cfg['url_upload'] = "http://$fp_proj_url/media/upload";
$cfg['upload_path'] = "$fp_proj/idf_upload";
$cfg['upload_issue_path'] = "$fp_proj/idf_upload_attach";
$cfg['tmp_folder'] = "$fp_proj/tmp";
$cfg['pear_path'] = "$fp_home/usr/pear/php";
$cfg['git_path'] = "$fp_home/usr/local/bin/git";
```

## Initialize Pluf and InDefero

Once the db information above is correctly entered into the php config,
the following should work, executed in the `indefero/src` directory:

    $ php ../../pluf/src/migrate.php --conf=IDF/conf/idf.php -a -i -d
    PHP include path: $HOME/usr/pear/php:.:/usr/local/php5/lib/php:/usr/local/lib/php:$HOME/example.com/site/pluf-master/src
    Install all the apps
    Pluf_Migrations_Install_setup
    IDF_Migrations_Install_setup

Next, run the boostrap script to create the first user. Once that's
working, use this .htaccess file:

    Options +FollowSymLinks
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*) /index.php?_pluf_action=$1

to get shorter urls for projects. Note: the last line is different from
that on the website, and this is the correct one (from a message on the
mailing list by the author).

You should now have a running installation, try it out by creating a new
project. Enjoy!

:::: note
::: title
Note
:::

By default, InDefero does *not* create empty repositories on the server,
nor is there an option to do so. The recommended workflow is simply to
create the project on the server, then make a local repository and push
to the InDefero host (the 'Source' tab for each project has nice
copy/paste instructions for this).
::::

## New users

InDefero is meant as a public forge, but in my case I don't actually
need outsiders to create new accounts, and in fact I don't want the
functionality. I will create new accounts manually only for
collaborators I am going to work with, and this is easily done by
running again the bootstrap script with different user information.
These users can then change their password via the web interface to
whatever they want.

I actually disabled new account creation by simply commenting out from
`src/IDF/templates/idf/login_form.html` the "I am new here" entry that
normally leads to the new account page. Just surround the relevant line
with `{*` and `*}` comment markers:

    > git diff HEAD~2 login_form.html
    diff --git a/src/IDF/templates/idf/login_form.html b/src/IDF/templates/idf/login
    _form.html
    index 624d613..93d5566 100644
    --- a/src/IDF/templates/idf/login_form.html
    +++ b/src/IDF/templates/idf/login_form.html
    @@ -10,8 +10,9 @@
     <p><label for="id_login">{trans 'My login is'}</label> <input type="text" name=
    "login" id="id_login" value="{$login}" /></p>

     <h3>{trans 'Do you have a password?'}</h3>
    -<p><input name="action" id="action-new-user" value="new-user" type="radio" /> <
    label for="action-new-user">{trans 'No, I am a new here.'}</label></p>
    -
    +{*
    +<p><input name="action" id="action-new-user" value="new-user" type="radio" /> <
    label for="action-new-user">{trans 'No, I am a new here.'}</label></p> >
    +*}
     <p><input name="action" id="action-login" value="login" type="radio" checked="c
    hecked" /> <label for="action-login">{trans 'Yes'}</label>, <label for="id_passw
    ord">{trans 'my password is'}</label> <input type="password" name="password" id=
    "id_password" /></p>

     <p><input type="submit" value="{trans 'Sign in'}" />

If you want to *really* disable creation in full, you should also
replace the `indefero/src/IDF/templates/idf/register/index.html`
template with a mostly empty page, since otherwise people can still just
navigate to the `site.example.com/register` url and will get the
registration page. This is what I did for my actual site.

If you make changes to the html templates, remember to flush the
temporary and cache directories to force a refresh of the public pages.

### SSH key synchronization and security

One small nugget that is stated in the [InDefero Git
docs](http://projects.ceondo.com/p/indefero/page/InstallationScmGit) but
is not very clearly explained is how new users are given permissions to
the repositories. This requires two things: a little cron job run *by
the special git user* and understanding how the keys are managed.

Your InDefero users do not have shell access to your server; in order to
use the repositories they must upload their SSH public key through the
web interface. Every time a user's SSH key is uploaded, InDefero leaves
a little temporary file (its name is stored as
`$cfg['idf_plugin_syncgit_sync_file']`) and InDefero ships with a php
script that detects this file and syncs the SSH key from the database
over to the `~/.ssh/authorized_keys` file of the special git user. You
can run this script manually to sync users, and it's a good idea to
leave it as a cron job in case users update their SSH keys later; the
script is `indefero/scripts/gitcron.php`.

An important point is that when these keys are uploaded, they do *not*
give your InDefero users unrestricted login access, as this would defeat
the isolation between projects that InDefero offers. Their SSH keys are
saved as authorized, but *only* to run a single command, a little python
script called `indefero/scripts/gitserve.py` that checks that user's
permissions in the database, and only gives them access to the
repositories consistent with those permissions. This ensures that the
special git user is not a security hole that would allow one user who
knew the path to another repository he's normally not allowed access,
to read it bypassing the web interface. Many thanks to Loic
D'Anterroches, the InDefero project lead, for clarifying this point.

## Backing things up

OK, you now have a system up and running. How do you back it up? Most of
the state of the project lives on the file system (and can thus be
backed up with a simple `rsync` call), except for the SQL database. A
simple way to handle this is to back it up manually once, and then to
store this backup into a git repository. We can then run a cron job on
the server that periodically runs a backup again, and then commits the
changes to the repo. By storing an uncompressed dump of the backup, we
make it easy for git to compute diffs and to later compress the entire
repository efficiently.

We start by running a manual backup once:

``` bash
cd mysql-dumps
mysqldump --opt -uUSER -pPASSWD -h HOSTNAME DBNAME > DUMPFILE
```

with this in place, we can now initialize the git repo:

``` bash
git init
git add DUMPFILE
git ci -m"Initializing: repo to hold backups of SQL database for InDefero site."
```

And now, we can add a cron job that runs every night a script like:

``` bash
#!/bin/bash
# Dump a backup of mysql database and store it in git repo.

#######################################################
# Configure here with your information
user=YOUR_SQL_USERNAME
hostname=YOUR_SQL_HOSTNAME
passwd="????"
dbname=YOUR_DATABASE_NAME
outdir=$HOME/example.com/site/mysql-dumps

# Make sure we use our own git
git=$HOME/usr/local/bin/git

#######################################################
# Code below
dumpfile=$dbname.sql

cd $outdir
mysqldump --opt -u$user -p$passwd -h $hostname $dbname > $dumpfile
# Store the history in git itself.
$git commit -a -m"Automated backup"
# Run gc every time to compact repo and save space
echo "Optimizing repository"
$git gc
```

Since this script has to hold your SQL password in plain text, make it
read-execute only for your user, and don't use an important password
there. Alternatively, if you want to play it safer, you can take the
password as an argument and initiate the backup process remotely over
SSH, from a trusted host. For my purposes this is sufficient.

Once the SQL database is nicely backed up in our site directory, the
entire project state consists of plain files, and we can simply rsync it
nightly to a remote host for off-site backup.

That's it. Every night the SQL database is backed up, and git gives us
a revision history that is also very space efficient, as the gc step
ensures that days with no real changes don't take any extra space on
disk (I tested this). A regular rsync off-site ensures that I have the
entire site state and history safely stored, should anything happen at
Dreamhost.

## Final comments

So far I think InDefero does what I need it to. I hope to clarify a few
small questions I have on the list (the author has been very responsive
to my queries so far), but I think I'll stick with it.

A few final points that I did not cover in these notes but that you may
need in your own setup:

Email

> I did not configure email delivery, as I only expect to make a few new
> users and I will do it by hand. [Jacobo](http://blog.jacobodevera.com)
> notes that if you eliminate from the IDF config file all email-related
> options, then the PEAR Mail module's defaults should work; I haven't
> tested this myself.

Git-daemon

> This is mentioned in the last step of the official instructions, but
> the basic Dreamhost plan does not allow me to run daemons. However,
> git-daemon is only needed if you want to provide anonymous access to
> your repositories. This is not my case (I use github.com for all my
> public code), so I didn't look further into this topic.
