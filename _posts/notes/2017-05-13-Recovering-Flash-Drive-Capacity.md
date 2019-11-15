---
title: Recovering Flash Drive Capacity
categories:
  - notes
tags:
  - computer
---

I usually use my pen-drive/flash-drive to do fresh install of operating systems on my laptop. I would use a ISO burner tool to burn OS ISO on the flash drive and make it bootable.
Typically I found my flash drive unharmed and usable without any issue using it this way. Recently burning more recent Linux OS ISO like KDE Neon or Netrunner on the flash drive made
a problem. After Burning the OS ISO, the capacity of the flash drive would show in KB size. For example I have a 14GB flash drive. But after burning the ISO the capacity of the drive
was showing to be ~700KB! This size did not change back to normal even after formating the flash drive. I tried to use the windows disk partion GUI to fix the problem as you would with
a regular hard disk. But I could not delete or modify the flash drive because the GUI was not showing any of those options. I thought the falsh drive was damaged.

After searching the internet, I found that the problem is nothing. The flash drive was OK and the lower capacity that it would show after ISO burning is something that normally happens.
The fix is to use the disk partition tool that I planned to use but not with GUI. I will have to use the command line tool. The following commmands would bring the flash drive back to
its normal capacity. So open a cmd in windows and do the following commands.

```
>diskpart
>list disk
>select disk 1
>list partition
>clean
>list partition
>create partition primary
>list partition
>format fs=fat32 quick
>list partition
>exit
```

`diskpart` command opens the disk partition tool in cmd. `list disk` lists the available disks. The hard drive should be listed as `Disk 0`. The flash should be listed as `Disk 1`. But the
computer has more than one hard drive then the flash drive should listed as having the last number. The actual hard disk capacity and flash drive capcity would also be listed so it will 
not a problem identifying the disk number for the flash drive. For me it was `Disk 1`. The flash drive is then selected with this disk number with `select disk 1` command. If the disk number
is different then that number will be used in this command. `list partition` allows us to see if there is any paritition and that paritition size. Hence it os not  mandatory to use this command.
`clean` deletes the partition. `create patition primary` creats a parition with the full capacity of the flash drive. `format fs=fa32 quick` does a quick format of the flash drive with FAT32.

There might be an error with `clean` command. If there is any error simply do a quick format with right click on the drive icon->format. Then proceed with the commands.