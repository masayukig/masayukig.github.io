---
title: Restore Gemini PDA Firmware
date: '2018-06-06T00:00:00+09:00'
slug: restore-gemini-pda-firmware
categories:
- gadget
tags:
- gadget
- oss
- gemini
draft: false
disqus_identifier: 2018-06-06-restore-gemini-pda-firmware
---

![Gemini PDA](https://photos.app.goo.gl/n0nD0O5Ulc7uPBlj1)

## Problem

I had updated my Gemini PDA firmware which was showed in the
setting. However, after the updating, my gemini never booted with the
planets rotating screen.


## How to solve it

First, I sent an email it to the support. They replied me very quickly
and said "We are aware of the issue. We are investigating the issue
with our firmware over the air (FOTA) ...."

However, I don't want to wait for that :-p. And my friend who has also
a gemini pda told me [Gemini Firmware](http://support.planetcom.co.uk/index.php/Gemini_Firmware) and [Flashing Guide](http://support.planetcom.co.uk/index.php/Flashing_Guide) pages.

To do this, I had to install [libaudio2 rpm package](http://packman.links2linux.org/download/nas/2455730/libaudio2-1.9.4-1.27.x86_64.rpm) manually to use
``flash_tool.sh`` .

And, the flashing part was also tricky. I needed to reboot(press
power + silver button) after pressing "Download" button on the tool. I
didn't notice that for a long time. But finally, I could have flashed
my gemini firmware.

So, I need to setup from the beginning, though...




Happy Hacking!
