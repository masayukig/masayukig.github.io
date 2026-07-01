---
title: VirtualBoxのディスクイメージ(vdi)をKVMのディスクイメージ(qcow2)に変換す る
date: '2010-07-24T07:42:00+09:00'
slug: virtualboxのディスクイメージvdiをkvmのディスクイメージqcow2に変換す-る
tags:
- KVM
- qcow2
- qemu
- Software
- vdi
- VirtualBox
draft: false
disqus_identifier: 2010-07-24-virtualboxnodeisukuimezivdiwokvmnodeisukuimeziqcow2nibian-huan-su-ru
cover:
  image: /images/covers/uncategorized.jpg
  alt: VirtualBoxのディスクイメージ(vdi)をKVMのディスクイメージ(qcow2)に変換す る
---

VirtualBoxを使っていたのですが、KVMも使いたくなったのでディスクイメージを変換してみた。

とは言っても、以下のコマンド一発で変換できたので、特に苦労は無し。
`$ qemu-img convert -O qcow2 .VirtualBox/windows7.vdi Documents/windows7.qcow2`

qemu便利だな。。
