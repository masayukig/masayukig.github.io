---
title: Mac で Scala と Lift を使ってみる(1) インストール編
date: '2011-06-10T06:06:00+09:00'
slug: mac-で-scala-と-lift-を使ってみる1-インストール編
tags:
- lift
- Linux
- Mac
- scala
- Software
draft: false
disqus_identifier: 2011-06-10-mac-de-scala-to-lift-woshi-tsutemiru1-insutorubian
---

Scala と Lift が気になってきたので、インストール。
くろだろぐさん： <http://kuroda.exblog.jp/12093277/> の記述を参考に、
最新版っぽいscala29をインストールした。

    sudo port selfupdate
    sudo port upgrade outdated
    sudo port install scala28 scala29 maven2
    sudo port select --set maven maven2
    sudo scala_select scala29
    scala -version
    sudo port install sbt
    mvn archetype:generate -U
    -DarchetypeGroupId=net.liftweb
    -DarchetypeArtifactId=lift-archetype-basic_2.8.1
    -DarchetypeVersion=2.3
    -DarchetypeRepository=http://scala-tools.org/repo-snapshots
    -DremoteRepositories=http://scala-tools.org/repo-snapshots
    -DgroupId=your.com
    -DartifactId=sample
    -Dversion=1.0
    cd sample
    sbt update
    sbt ~jetty-run

で、できた。

[![mac de Scala/Lift
sample](http://farm6.static.flickr.com/5261/5815832647_168f6767f5.jpg){.alignnone}](http://www.flickr.com/photos/31362181@N08/5815832647/ "mac de Scala/Lift sample")
