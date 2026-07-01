---
title: Ubuntu(8.10)上のFirefoxで日本語フォントがおかしい（中国語フォント？）
date: '2008-12-13T06:55:00+09:00'
slug: ubuntu810上のfirefoxで日本語フォントがおかしい（中国語フォント）
categories:
- OSS
tags:
- Firefox
- Font
- Linux
- Software
- Ubuntu
- 日本語
draft: false
disqus_identifier: 2008-12-13-ubuntu810shang-nofirefoxderi-ben-yu-huontogaokashiizhong-guo-yu-huonto
cover:
  image: /images/covers/oss.png
  alt: Ubuntu(8.10)上のFirefoxで日本語フォントがおかしい（中国語フォント？）
---

Ubuntu(8.10)上のFirefoxで日本語フォントがおかしい（中国語フォント？）と言う現象に遭遇したので、
解決するためのメモ。

-   <http://forum.ubuntulinux.jp/viewtopic.php?id=3124>
-   <https://bugs.launchpad.net/ubuntu-jp-improvement/+bug/272387>

を参考に(というかそのままだがw)、
`$ sudo ln -s /etc/fonts/conf.avail/69-language-selector-ja-jp.conf /etc/fonts/conf.d/`
を、実行。ブラウザリロード(not リスタート)で、即解決。
