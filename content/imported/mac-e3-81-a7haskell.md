Title: MacでHaskell
Date: 2011-05-06 10:56
Author: masayukig
Tags: Apple, haskell, Mac, programming
Status: published

ふと、Haskell学習を再開してみたくなったので、  
本棚から、「[ふつうのHaskellプログラミング](http://www.amazon.co.jp/gp/product/4797336021/ref=as_li_ss_tl?ie=UTF8&tag=hughundercons-22&linkCode=as2&camp=247&creative=7399&creativeASIN=4797336021)![](http://www.assoc-amazon.jp/e/ir?t=&l=as2&o=9&a=4797336021){width="1"
height="1"}」を引っ張りだしたが、  
「ん？ghcはどうするんだ？」と思い、ググる。

<http://www.haskell.org/haskellwiki/Mac_OS_X#Mac_OS_X_10.6_.28Snow_Leopard.29>から、  
<http://hackage.haskell.org/platform/mac.html>  
で、「Download Haskell for Mac OS X 10.6 (Intel, 32 bit
GHC)」のリンクをクリックし、  
インストールパッケージをダウンロード。

> Note: Xcode 3.0 or later is required prior to installation.

と、書いてあるので、App
StoreでXcodeをインストール(600円也。まぁいいか。。)。  
ちなみに、Xcodeは4.5GB程度あるのでディスク残量に注意。

ダウンロードしてる間に、「[ふつうのHaskellプログラミング](http://www.amazon.co.jp/gp/product/4797336021/ref=as_li_ss_tl?ie=UTF8&tag=hughundercons-22&linkCode=as2&camp=247&creative=7399&creativeASIN=4797336021)![](http://www.assoc-amazon.jp/e/ir?t=&l=as2&o=9&a=4797336021){width="1"
height="1"}」を再読。  
全く忘れている。。。

そんなこんなで、ダウンロード完了。  
[![](http://b.0r2.info/wp-content/uploads/2011/05/aa5be2c3aa932d14ad065b6f5c90cb3c.png "Xcode installer"){.aligncenter
.size-full .wp-image-1490 width="137"
height="131"}](http://b.0r2.info/wp-content/uploads/2011/05/aa5be2c3aa932d14ad065b6f5c90cb3c.png)  
Xcode installerを起動しインストール。うまく行かないこともあるが、  
その場合はもう一回やってみるとうまく行くこともあるらしい。(何だそりゃ)

で、Xcodeのインストールが完了したら、  
Haskell Platform 2011.2.0.1-i386.pkgをダブルクリックし、インストール。

インストールが完了したら、ターミナルで実行してみる。  
[![](http://b.0r2.info/wp-content/uploads/2011/05/05010e6679ab0951d909cc3a69d7d5da-300x80.png "Haskell-terminal"){.aligncenter
.size-medium .wp-image-1491 width="300"
height="80"}](http://b.0r2.info/wp-content/uploads/2011/05/05010e6679ab0951d909cc3a69d7d5da.png)  
コンパイル(というかリンク時?)にwarningが出るものの、とりあえず実行バイナリが作成されて、  
「Hello, world!」も表示されたので、良しとする。

参考書籍：  
[![](http://ws.assoc-amazon.jp/widgets/q?_encoding=UTF8&Format=_SL160_&ASIN=4797336021&MarketPlace=JP&ID=AsinImage&WS=1&tag=hughundercons-22&ServiceVersion=20070822)](http://www.amazon.co.jp/gp/product/4797336021/ref=as_li_ss_il?ie=UTF8&tag=hughundercons-22&linkCode=as2&camp=247&creative=7399&creativeASIN=4797336021)![](http://www.assoc-amazon.jp/e/ir?t=&l=as2&o=9&a=4797336021){width="1"
height="1"}
