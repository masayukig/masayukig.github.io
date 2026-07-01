---
title: 一般ユーザ権限でrpmbuildを実行
date: '2009-03-21T13:53:00+09:00'
slug: 一般ユーザ権限でrpmbuildを実行
tags:
- rpm
- rpmbuild
draft: false
disqus_identifier: 2009-03-21-yi-ban-yuzaquan-xian-derpmbuildwoshi-xing
cover:
  image: /images/covers/uncategorized.jpg
  alt: 一般ユーザ権限でrpmbuildを実行
---

$ echo "%_topdir $HOME/src/rpms" > $HOME/.rpmmacros
    $ mkdir -p $HOME/src/rpms/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

を、実行して、後は、

    $ rpmbuild --rebuild hogehuga.src.rpm

を実行すればおk。
