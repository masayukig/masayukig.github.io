:title: The architecture of this blog
:slug: blog-architecture-and-tools
:tags: oss, blog
:category: Misc
:date: 2017-12-08
:Status: published

I already posted_ about switching this blog to igawa.io. But I think
it's good to share the information about the architecture of this blog
for you and especially me :)

.. _posted: ../11/migrated-my-blog-to-igawaio

Architecture/tools
==================

GitHub Pages, CloudFlare
------------------------

So, currently, this blog uses `GitHub Pages`_ which can be used as a
free blog system. And I also use it with my custom domain and HTTPS
with CloudFlare_.

.. _GitHub Pages: https://pages.github.com/
.. _CloudFlare: https://www.cloudflare.com/

Pelican
-------

And I'm using pelican_ as a blog system which is really powerful and
written by python. That means I can improve and fix if I need it. And
`I've done it
<https://github.com/masayukig/masayukig.github.io/issues>`_ before.

.. _pelican: https://github.com/getpelican/pelican

Branches
--------

`Here <https://github.com/masayukig/masayukig.github.io/issues>`_ is
the repository of this blog. This has two main branches, one
is master and the other is source. `master` branch is for managing
generated contents. `source` branch is for managing source code such
as blog post rst/md, imange, files, etc. So, the two branches are
completely different. I feel this is a bit weird, but I couldn't find
a better solution so far. And It seems it works well. I don't need to
change the workflow.

Retrospective
=============

I have some feelings with this system.

Positive
--------

* I can use the issues and wiki on github for my ideas for my
  blog. And I can make them open.
* I can keep and manage my blog posts as simple text files. That
  means I can use git to store the history.
* I don't need the internet connection to writing blog posts.

Negative
--------

But some negative things are,

* I need a text editor to write blog post. Maybe, I can use a web
  browser instead, though.
* It takes some time to generate HTML files everytime.

Summray
=======

Overall, I'm satisfied with this system so far. If you interested in
like this things, feel free to contact me. And you can see and post an
issue here_.

.. _here: https://github.com/masayukig/masayukig.github.io/issues

