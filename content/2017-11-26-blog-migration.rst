:title: Switched my blog to igawa.io
:slug: migrated-my-blog-to-igawaio
:tags: oss, blog
:category: Misc
:date: 2017-11-26
:Status: published

I changed my blog to my original domain. My blogs were split to some
different domains due to my laziness. So I decided to merge them.

I was trying to change it to wordpress.com first. But it's not my
taste :-p So, I decided to use pelican_.

I actually had two blogs on Blogger(br.0r2.info) and github
pages(afterstack.net). So I needed to export br.0r2.info data to merge
github pages. And I also wanted to change the domain to use igawa.io_.

Firstly, I was trying to use wordpress.com, so I exported my blogger
data, and imported it on wordpress. And next, I also exported the
wordprss data, and I imported the data with using pelican-import_ like
this.

::

  $ pelican-import -m \
  markdown --strip-raw --disable-slugs --wp-attach --wpfile -o \
  ./content/imported ~/wordpress.2017-11-26.001.xml

I actually faced some warnings and errors. So, I needed to fix it by
hand :-p And, finally, I did it. Some pages still have some issues
such as images, URLs and some other something. But I did it, anyway.

This is just a starting point for my new blog. I have some candidates
like tempest, my servers, and the other openstack things. I hope I'll
write the posts in the near future.

I really like this pelican blog system. But only one thing is that
editor. I'd like to use text editors to write blog posts such as vim
or emacs but they aren't on my smartphone...


.. _pelican: https://github.com/getpelican/pelican
.. _igawa.io: https://igawa.io/
.. _pelican-import: http://docs.getpelican.com/en/latest/importer.html

