Title: Mac に vagrant+devstack を入れてみる - その１ #openstack #devstack #vagrant
Date: 2012-10-03 15:06
Author: masayukig
Category: openstack
Tags: vagrant
Status: published

何するのか?
-----------

[vagrant\_devstack](https://github.com/bcwaldon/vagrant_devstack) っていうのを使って、vagrant+devstack
という素敵な環境を、


Mac OS Mountain Lion(10.8.2)に 作ってみる。  
一応、vagrant\_devstackのREADMEには、Macに対する言及があるので、  
できるんじゃないかと妄想。



はじめに
--------



まずは、



<https://github.com/bcwaldon/vagrant_devstack>



のREADMEにしたがって、



1.  Virtualboxインストール
2.  gem update --system
3.  gem install vagrant


を行った。。。。
困ったこと発生
--------------

が、「3.」で問題発生。



    % gem install vagrant  
    Fetching: archive-tar-minitar-0.5.2.gem (100%)
    Fetching: json-1.5.4.gem (100%)
    Building native extensions.  This could take a while...
    ERROR:  Error installing vagrant:
     ERROR: Failed to build gem native extension.

            /Users/igawa/.rvm/rubies/ruby-1.9.3-p194/bin/ruby extconf.rb
    checking for re.h... *** extconf.rb failed ***
    Could not create Makefile due to some reason, probably lack of
    necessary libraries and/or headers.  Check the mkmf.log file for more
    details.  You may need configuration options.


と、こんな感じのエラーが出力され、インストール出来ない。
解決策
------

ググってみると、

**[【Mac】【RubyGems】/usr/bin/gcc-4.2
がない！](http://loveless-ainakimono.seesaa.net/article/232323709.html)**




という記事を見つけたので、それに習って、以下のようにシンボリックリンクを



張ってみました。


    % sudo ln -s /usr/bin/llvm-gcc-4.2 /usr/bin/gcc-4.2


結果、
    % gem install vagrant                              
    Building native extensions.  This could take a while...
    Fetching: log4r-1.1.10.gem (100%)
    Fetching: net-ssh-2.2.2.gem (100%)
    Fetching: net-scp-1.0.4.gem (100%)
    Fetching: vagrant-1.0.5.gem (100%)
    Successfully installed json-1.5.4
    Successfully installed log4r-1.1.10
    Successfully installed net-ssh-2.2.2
    Successfully installed net-scp-1.0.4
    Successfully installed vagrant-1.0.5
    5 gems installed

っていうように先に進めました。

ようやく本番
------------



ようやく、本来やりたかったところに入れます。

で、更に、マニュアルに従い、

    git clone http://github.com/bcwaldon/vagrant_devstack.git
    cd vagrant_devstack 
    git submodule init
    git submodule update
    cp etc/vagrant.yaml.sample etc/vagrant.yaml
    vim Vagrantfile 

を実行。Vagrantfileは、以下の様な感じに修正。

    % git diff
    diff --git a/Vagrantfile b/Vagrantfile
    index 4aaa5fa..75bccfe 100644
    --- a/Vagrantfile
    +++ b/Vagrantfile
    @@ -4,7 +4,9 @@ conf = {
         'ip_prefix' => '192.168.27',
         'mac_prefix' => '080027027',
         'box_name' => 'precise',
    -    'box_url' => 'http://c479942.r42.cf2.rackcdn.com/precise64.box',
    +    'box_url' => 'http://dl.dropbox.com/u/1537815/precise64.box',
    +#    'box_url' => 'http://files.vagrantup.com/precise64.box',
    +#    'box_url' => 'http://c479942.r42.cf2.rackcdn.com/precise64.box',
         'allocate_memory' => 1024,
         'cache_dir' => 'cache/',
         'ssh_dir' => '~/.ssh/',

で、ここまで来たら、

    vagrant up

を実行。

    [default] Box precise was not found. Fetching box from specified URL...
    [vagrant] Downloading with Vagrant::Downloaders::HTTP...
    [vagrant] Downloading box: http://dl.dropbox.com/u/1537815/precise64.box
    [vagrant] Progress: 7% (43960869 / 567768576)

結構時間が掛かる。待ってられないので、一眠り。。。。
