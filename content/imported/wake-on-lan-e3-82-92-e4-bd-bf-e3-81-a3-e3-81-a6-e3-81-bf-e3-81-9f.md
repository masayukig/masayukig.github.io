Title: Wake-on-LANを使ってみた
Date: 2010-05-27 05:59
Author: masayukig
Tags: お金, PC, Ubuntu, WOL
Status: published

「PCが複数台あって、必要な時だけPCを起動したい」という欲求が出てきたので、  
[Wake On
Lan(WOL)機能](http://ja.wikipedia.org/wiki/Wake-on-LAN)を使ってみた。

(最近、暑くなってきたこともあり、さらに電気代もバカにならないので、  
不要なPCの電源はできるだけ落としておきたいので)

-   準備(ハードウェア編)

マザーボード等が対応している必要があるが、  
最近のPCであればおそらく対応しているものがほとんどだと思われる。  
ただし、BIOSの設定変更が必要な場合があるので注意が必要。  
私が使っているマザーボード(MSI
KA780GM-M)ではデフォルトでONになっている様でした。

-   準備(ソフトウェア編)

送信側：

1.  「起こされる」PCのMACアドレスを調査
2.  wakeonlanパッケージをインストール
3.  wakeonlanコマンドを使用し、起こす

この様な流れでしょうか。では、詳細を。

1.  「起こされる」PCのMACアドレスを調査
2.  wakeonlanパッケージをインストール
3.  wakeonlanコマンドを使用し、起こす

cron等で「起こす側」がwakeonlanコマンドを実行し、「起こされる側」が定期的にpoweroffするようにすれば、  
「定期的に電源ONをして、終わったら、電源OFF」という運用が可能となる。

参考リンク:  
<http://www.atmarkit.co.jp/flinux/rensai/linuxtips/709usewol.html>
