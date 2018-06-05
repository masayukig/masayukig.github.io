Title: C/C++でGC
Date: 2008-07-07 23:55
Author: masayukig
Tags: C++, C言語, GC
Status: published

Java野郎(私)が、C/C++でメンドイものの一つに、

**「malloc()したらfree()しなきゃならん」**というものがある。

大体、誰も参照しなくなったら、もはや、誰も触れないんだから、勝手に開放してほしいのだ。

###### でも、それをC言語自体に望むのは無理だって言うのもわかってる。

どうにかなんないの？と思っていたら、C/C++でGCするためのライブラリがあるということを知りました。

<http://www.hpl.hp.com/personal/Hans_Boehm/gc/>

自分(個人)でプログラム書くときは、これ使います。多分。

(いちいち、malloc()/free()なんてしてられっか)
