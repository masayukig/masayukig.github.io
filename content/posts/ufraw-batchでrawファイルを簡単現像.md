---
title: ufraw-batchでRAWファイルを簡単現像
date: '2008-07-29T22:47:00+09:00'
slug: ufraw-batchでrawファイルを簡単現像
tags:
- カメラ
- 画像
- RAW
- ufraw
- ufraw-batch
- 写真
draft: false
disqus_identifier: 2008-07-29-ufraw-batchderawhuairuwojian-dan-xian-xiang
---

Nikon
D70というカメラを持っていて、最近、コンパクトフラッシュを大容量のものに変えたので、
RAWファイル+BASIC JPGモードで写真を撮ることにしてみた。

とはいえ、たくさんのRAWファイルを簡単に現像したいという欲求にかられたので、
どうにかならないものかと探していたところ、以下のような方法を見つけた。

`ufraw-batch --wb=auto --out-type=jpeg --exposure=auto *.nef`

これで、ホワイトバランスオート、自動露出で、JPEGファイル書き出しとなる。
詳しいことは、ufraw-batch --helpをしてみよう。
