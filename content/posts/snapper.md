---
title: Snapper
date: '2018-02-09T00:00:00+09:00'
slug: snapper
categories:
- OSS
tags:
- oss
- opensuse
draft: false
disqus_identifier: 2018-02-09-snapper
cover:
  image: /images/covers/oss.png
  alt: Snapper
---

I found that [snapper](https://en.opensuse.org/openSUSE:Snapper_Tutorial) of openSUSE is
very useful! When I faced an update trouble, it worked very well
without any trouble!

Basically, we tend to forget to make a  backup everyday every time by
hand because it's not necessary normally. However, the thing is happen
all of a sudden!

This is the first time to use that tool. It worked very well without
any trouble. So, I think snapper is a very good feature.


By default, openSUSE setups snapper on your root volume w/ btrfs. So
you can use it like this, We can rollback where you want.

To use ``snapper``, it's very easy. By default, ``snapper`` creates
snapshots every zypper updates. So, if you want to rollback, you just
need to select the option to rollback on the boot menu. Or you can
specify a snapshot like this:

```
```
 $ sudo snapper rollback [snapshot number]

You can see snapshot numbers by ``snapshot list``.

If you want to get more information, please refer to ``man snapper``,
``snapper --help`` or [snapper tutorial page](https://en.opensuse.org/openSUSE:Snapper_Tutorial).


Happy Hacking!
