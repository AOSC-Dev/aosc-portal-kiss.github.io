---
categories:
  - warning
title: "[SOLVED] GDM Not Working on GNOME 40 test test test test test"
date: 2021-04-06T18:34:00+08:00
important: false
---

The testing update of GNOME 40 is now available, and you can enable `gnome-40` topic in ATM to get the update.
However, GDM cannot start due to incorrect configuration of authentication, you may use LightDM / SDDM instead
to start your GNOME / GNOME on Xorg session.

We will release a fix for GDM after this problem is solved.

2021-04-07 Update:

    gnome-40-main amd64
    ^ [gdm](https://packages.aosc.io/packages/gdm) 40~rc ⇒ 40.0
    ^ [gdm-dbg](https://packages.aosc.io/packages/gdm-dbg) 40~rc ⇒ 40.0

The update above has solved the issue.

----

— Jack Wu (Original Author: Mingcong Bai)
