Title: Mac OS X Lionでsshfs
Date: 2011-08-03 06:11
Author: masayukig
Tags: Apple, lion, Mac, sshfs
Status: published


Mac OS X
Lionでsshfsを使おうと思い、portでsshfs-guiインストールを行ったところ、
以下の様なエラーが出て、インストールに失敗しました。
<https://gist.github.com/1121166.js?file=sshfs-gui-install-failed-on-Mac-OS-X-Lion.log>

ググってみたところ、以下の情報を得たので、やってみました。

-   [OSX
    Lionでは、タダじゃあsshfsが動かないみたい。](http://inabu.asia/monooki/357/2011/07/31/)
-   [ubuntuやmac(OSX
    Lion)でsshfs](http://crysis-fs.blogspot.com/2011/07/ubuntumacosx-lionsshfs.html)

というわけで、
<http://www.tuxera.com/mac/macfuse-core-10.5-2.1.9.dmg>
を、ダウンロード＆インストール後、
<https://gist.github.com/1121166.js?file=static-binary-download.log>
の様な感じで実行し、うまくマウントできました。（warningが出てるけど無視w）

まだ、ハードな使用はしていないので、それは、後ほど試します。
