---
title: Using Crontab
categories:
  - notes
---

My university workstation is a red hat desktop. It has only one hard disk of 1TB. However, I only get 25GB disk quota for home space. The OS uses all of the hard disk. 
So I do not have any personal space for storing data on my local hard disk. There are plenty of space in the /tmp/ directory but the files which are more than 10 days old are
deleted automatically by the OS. If I am able to trick the OS into thinking that the files in /tmp/ are always new then the files will not be deleted and I could use the /tmp/ 
directory as my own local space for storing data. This can be achieved using the command `touch` which updates the timestamp of a file. 

If I can update the timestamp of the files everyday the OS will never find any file older than 10 days. Using `crontab` I can run the `touch` command everyday at midnight.

The touch command is written in a script `crontab.sh`
```
#!/bin/bash

# directory to be updated
DIR="/tmp/mydir"
cd /tmp/mydir

# update the time stamp of all the files and directories
find . -exec touch -am {} +

echo "...Done updating..."
```

crontab entry (use `crontab -e to edit`, `crontab -l` to display existing entry).
```
1 0 * * * /nfs/users/username/linux/start-scripts/crontab.sh >/dev/null 2>&1
```

### Observation
If there are way too many files then applying `touch` command to every file can take some time. From my experience 7 or 8GB of data takes only about 5-7 seconds.
