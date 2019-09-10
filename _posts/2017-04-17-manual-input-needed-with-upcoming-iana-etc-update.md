---
layout: post
title: 'Manual Input Needed with Upcoming iana-etc Update'
type: news
important: true
---

A recent change to the `iana-etc` package has addressed an issue where it could be impossible to initiate `telnet` connections on AOSC OS.

However, the file `/etc/services` - contained within `iana-etc` has been marked as a configuration file, therefore, `DPKG` could ask if the file should be replaced with the one provided with the package (which contain the fix to this issue). Please choose "Yes", or press the `i` key when prompted.

We apologize for your inconvenience.