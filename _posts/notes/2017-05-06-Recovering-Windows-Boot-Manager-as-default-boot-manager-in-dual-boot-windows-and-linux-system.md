---
title: Recovering Windows Boot Manager as default boot manager in dual boot windows and linux system
categories:
  - notes
tags:
  - computer
---

I don't know if I am a Linux fan. I am not even a computer nerd. But I like to try out different linux distors on my machine. My introduction to Linux started with Ubuntu. When I was an undergrad back in 2008, I used to order free Ubuntu installation disks just for the fun of it. Somehow a linux desktop and working with the terminal or bash shell made me feel like I am actually doing something! I tried to test almost all of the releases they put out both ubuntu and kubuntu. The user experience was somewhat satisfactory and mostly banging head on the desk. There were so much simple things that the system could not handle. For example the internet that I was using in my university residential hall was a wired a connection and I had to specify IP address to the computer. Windows could do this in an instant. With my first linux it worked just after installation. But after a restart evrything would go upside down. The OS would loose all of the IP information along with the 'Network Connection' application. There was not any direct solution available on the internet community. And guess what. I couldn't even look for the solution on the internet without getting back to windows with a stable internet. But in the subsequent releases that problem somehow went away. After many years I got a laptop running Windows 10 with Nvidia Optimus technology. Things are kind of thorny with linux and Nvidia Optimus. Every linux distro I tried crashed its display on this laptop. There are some getaround to this like the Bumblebee project but none of them worked every time I gave a restart.

## Problem
I was trying out the new KDE Neon 2017. It was working for some time. But after an update the system failed to start and would boot into initramfs console. So I ditched it and tried out Netrunner Cyclotron edition. Both Neon and Netrunner would fail to start display in the Live desktop mode. I had to use recovery mode to get the display running. After installation Netrunner would boot into a tty menu. Ocassionally it would boot to GUI. This unstable behaviour force me to get rid of GRUB menu and use the default windows boot manager to start windows directly. The simplest way is to not uninstall GRUB but to put the windows boot manager to the top of the boot order in the BIOS. I would select windows boot manager at bios but it took me to a grub recovery console. Windows would start normally from grub menu of netrunner but setting windows loader to the top from bois was taking me to a grub recovery! I searched the internet. There was nothing. But there was something that led me to find the root of the problem. I looked into the `efibootmgr -v` output in linux to see the bootmanager set to windows. It shows something like this.

```
$ efibootmgr -v
BootCurrent: 0002
Timeout: 1 seconds
BootOrder: 0000,0002,0011,0012
Boot0000* Windows Boot Manager  HD(1,GPT,xxxxxx-xxxxxxxx-xxxxxx)/File(\EFI\ubuntu\grubx64.efi)WINDOWS ....
```

Wich means windows boot manager was using ubuntu's grub. But it was supposed to be using `\EFI\Microsoft\Boot\bootmgfw.efi`. This might have somehow happed when I replaced Neon with Netrunner. Neon is ubuntu based. And Neos's grub was somehow assigned windows. And since there is no Neon in the system right now grub failed to start and went to grub recovery console. So the fix was clear. I have to set the windows boot manager to use the `bootmgfw.efi`.

I did this in windows. I booted into windows using Netrunner grub menu. Then I used `bcdedit` [commands](https://technet.microsoft.com/en-us/library/dn336950.aspx) to set correct bootmanager which resides in EFI system partition. To do that first the EFI system partition should be mounted. Using a cmd prompt in administration mode the following will mount the EFI system partition.

```
C:\WINDOWS\system32>diskpart
DISKPART> list disk

  Disk ###  Status         Size     Free     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  Disk 0    Online          xxx GB      0 B        *
  
DISKPART> sel disk 0

Disk 0 is now the selected disk.

DISKPART> list vol

  Volume ###  Ltr  Label        Fs     Type        Size     Status     Info
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
  Volume 0     C   OS           NTFS   Partition    xxx GB  Healthy    Boot
  Volume 1     D   lab0         NTFS   Partition    xxx GB  Healthy
  Volume 2     E   lab1         NTFS   Partition    xxx GB  Healthy
  Volume 3     F   lab2         NTFS   Partition    xxx GB  Healthy
  Volume 4         ESP          FAT32  Partition    xxx MB  Healthy    System
  Volume 5         WINRETOOLS   NTFS   Partition    xxx MB  Healthy    Hidden
  Volume 6         Image        NTFS   Partition     xx GB  Healthy    Hidden
```
For my case I had only one hard disk which is listed as `Disk 0`. I have an ESP system partition on volume 4.This needs to be mounted. The following commands will mount the ESP partition and set the windows boot manager's device to the ESP system partition and path the `bootmgfw.efi`.

```
DISKPART> select volume 4 
DISKPART> assign letter=s
DISKPART> exit
C:\WINDOWS\system32> Bcdedit /set {bootmgr} device partition=s: bcdedit /set {bootmgr} device partition=s:
C:\WINDOWS\system32> bcdedit /set {bootmgr} path \efi\microsoft\boot\bootmgfw.efi
```

And voila! I could boot again from windows boot manager.
