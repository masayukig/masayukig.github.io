---
title: Linux2.6系でxfsでLVM のsnapshotをとりたい場合は、xfs_freeze不要？
date: '2008-12-15T04:14:00+09:00'
slug: linux26系でxfsでlvm-のsnapshotをとりたい場合はxfs_freeze不要
tags:
- LVM
- snapshot
- xfs
draft: false
disqus_identifier: 2008-12-15-linux26xi-dexfsdelvm-nosnapshotwotoritaichang-he-ha-xfs_freezebu-yao
---

xfsではsnapshotをとる場合に、整合性を保つために
`xfs_freeze`
というコマンドがある。

が、これは、Linux2.6系では実行してはいけないらしい。
(最近の2.6.27とかでも同様かは不明。)

情報元：

-   <http://ja.wikipedia.org/wiki/XFS#.E3.82.B9.E3.83.8A.E3.83.83.E3.83.97.E3.82.B7.E3.83.A7.E3.83.83.E3.83.88>
-   <http://labs.unoh.net/2006/09/lvm_xfs_mysql.html>
-   <http://marc.info/?l=linux-lvm&m=111014382900031&w=2>
