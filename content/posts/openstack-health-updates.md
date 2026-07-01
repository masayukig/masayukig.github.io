---
title: OpenStack-Health updates
date: '2016-10-19T00:00:00+09:00'
slug: openstack-health-updates
categories:
- Work
tags:
- work
- oss
- openstack
- openstack-health
draft: false
disqus_identifier: 2016-10-19-openstack-health-updates
cover:
  image: /images/openstack-health-2016-10-19.png
  alt: OpenStack-Health
---

本日、[OpenStack-Health](http://git.openstack.org/cgit/openstack/openstack-health) のパッチをいくつかApproveしました。

* [Add base utilities for canvas charts](https://review.openstack.org/#/c/363934/)
* [Add canvas line chart](https://review.openstack.org/#/c/380884/)
* [Add canvas scatter chart](https://review.openstack.org/#/c/380885/)

これは、グラフ描画用のJavascriptライブラリ（ユーティリティ）です。今までは、[nvd3](http://nvd3.org/) という [d3js](https://d3js.org/) を
使いやすくしたJavascriptライブラリを使用していましたが、パフォーマンスと細かなバグに悩まされることも多く、
独自実装に切り替えようとしています。([d3js](https://d3js.org/) は引き続き使っています。)


まだ、全てのグラフを置き換えられたわけではありませんし、荒削りな部分が多々ありますが、良い方向に進んでいる
と思います。

まぁ、最悪、クリティカルなバグがあったとしても、パッチをrevertすれば良いので、
恐る恐る進む必要もなく、むしろ、現時点では、リスクを恐れて前に進まないほうが問題と判断しました。

現時点での課題は...

* unit testが無い
* グラフが二重描画されることがある -> ブラウザリサイズ/リロードでなおる

今後も、品質改善に向けて進んでいきます :)

以下が OpenStack-Health の画面です。って、http://status.openstack.org/openstack-health/ にアクセスすれば、
誰でも見られます :)

----------------------------------------------------------------

![OpenStack-Health](/images/openstack-health-2016-10-19.png)

Happy Hacking!
