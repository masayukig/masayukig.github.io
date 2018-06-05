Title: Mac に vagrant+devstack を入れてみる - その２ #openstack #devstack #vagrant
Date: 2012-10-04 21:13
Author: masayukig
Category: openstack
Tags: Mac, vagrant
Status: published

続き
----


無事ダウンロードは終了し、VMも起動したが、NFSでマウントできないってエラーが



発生。




    [vagrant] Downloading box: http://dl.dropbox.com/u/1537815/precise64.box
    [vagrant] Extracting box...
    [vagrant] Verifying box...
    [vagrant] Cleaning up downloaded box...
    [default] Importing base box 'precise'...
    [default] The guest additions on this VM do not match the install version of
    VirtualBox! This may cause things such as forwarded ports, shared
    folders, and more to not work properly. If any of those things fail on
    this machine, please update the guest additions and repackage the
    box.

    Guest Additions Version: 4.1.18
    VirtualBox Version: 4.1.23
    [default] Matching MAC address for NAT networking...
    [default] Mounting shared folders...
    [default] -- v-root: /vagrant
    [default] -- v-ssh: /home/vagrant/.host-ssh
    [default] -- v-csc-1: /tmp/vagrant-chef-1/chef-solo-1/cookbooks
    [default] Mounting NFS shared folders...
    Mounting NFS shared folders failed. This is most often caused by the NFS
    client software not being installed on the guest machine. Please verify
    that the NFS client software is properly installed, and consult any resources
    specific to the linux distro you're using for more information on how to
    do this.

でも、vagrant sshでGuest OSには接続できた!

    -> % vagrant ssh
    Welcome to Ubuntu 12.04.1 LTS (GNU/Linux 3.2.0-23-generic x86_64)

     * Documentation:  https://help.ubuntu.com/
    Welcome to your Vagrant-built virtual machine.
    Last login: Mon Aug 20 19:28:45 2012 from 10.0.2.2
    vagrant@precise64:~$ uname -a
    Linux precise64 3.2.0-23-generic #36-Ubuntu SMP Tue Apr 10 20:39:51 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux
    vagrant@precise64:~$ uptime
     21:52:20 up  5:24,  1 user,  load average: 0.00, 0.01, 0.05

でも、OpenStack関連のサービスは全く起動していないようだったので、
vagrant reloadをやってみた


    -> % vagrant reload
    [default] Attempting graceful shutdown of VM...
    [default] Clearing any previously set forwarded ports...
    [default] Forwarding ports...
    [default] -- 22 => 2222 (adapter 1)
    [default] Exporting NFS shared folders...
    [vagrant] Preparing to edit /etc/exports. Administrator privileges will be required...
    Password:
    [default] Creating shared folders metadata...
    [default] Clearing any previously set network interfaces...
    [default] Preparing network interfaces based on configuration...
    [default] Running any VM customizations...
    [default] Booting VM...
    [default] Waiting for VM to boot. This can take a few minutes.
    [default] VM booted and ready for use!
    [default] Configuring and enabling network interfaces...
    [default] Mounting shared folders...
    [default] -- v-root: /vagrant
    [default] -- v-ssh: /home/vagrant/.host-ssh
    [default] -- v-csc-1: /tmp/vagrant-chef-1/chef-solo-1/cookbooks
    [default] Mounting NFS shared folders...
    [default] Running provisioner: Vagrant::Provisioners::ChefSolo...
    [default] Generating chef JSON and uploading...
    [default] Running chef-solo...
    stdin: is not a tty
    [Thu, 04 Oct 2012 20:38:58 +0000] INFO: *** Chef 0.10.10 ***
    [Thu, 04 Oct 2012 20:38:59 +0000] DEBUG: Building node object for precise64.
    [Thu, 04 Oct 2012 20:38:59 +0000] DEBUG: Extracting run list from JSON attributes provided on command line
    [Thu, 04 Oct 2012 20:38:59 +0000] INFO: Setting the run_list to ["recipe[vagrant-openstack::hostname]", "recipe[vagrant-openstack::cache]", "recipe[vagrant-openstack::devstack-cache]", "recipe[devstack]", "recipe[vagrant-openstack::devstack-update-cache]"] from JSON

と、最初の方は調子良さそうだったが...

    + sudo rm -rf /home/vagrant/cache /home/vagrant/devstack
    rm: cannot remove `/home/vagrant/cache': Device or resource busy
    ++ failed
    ++ local r=1
    +++ jobs -p
    ++ kill
    ++ set +o xtrace
    ---- End output of su -c 'set -e; cd /home/vagrant/devstack; RECLONE=yes bash stack.sh > devstack.log' vagrant ----
    Ran su -c 'set -e; cd /home/vagrant/devstack; RECLONE=yes bash stack.sh > devstack.log' vagrant returned 1
    Chef never successfully completed! Any errors should be visible in the
    output above. Please fix your recipes so that they properly complete.

と、エラー終了orz.. 道のりは長そうだ。
