---
layout: post
title: 'Termination of RPM Package Releases'
type: news
important: true
---

With deep apologies, I must announce that the RPM port of AOSC OS has failed due to the lack of attention and manpower, in addition to the confusing situation that Zypper and RPM are going through in the recent year (updates, RPM dependencies, and PackageKit), it seems no longer viable to maintain such a port (let alone there is absolutely no user for this port).

RPM packages (/os-*/os3-rpm) were removed from the [repository server](https://repo.aosc.io) just shy of 50 minutes ago.

On the bright side, however. We will continue with completing Autobuild3's RPM backend, and possibly bring Pacman support in the forseeable future.

— Mingcong (Jeff) Bai