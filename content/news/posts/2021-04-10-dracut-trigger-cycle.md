---
categories:
  - warning
title: "Dracut Trigger Cycle Error"
date: 2021-04-10T17:03:31+08:00
important: false
---

If you met the following error when upgrading system:

    Setting up xine-lib (1.2.10-2) ...
    dpkg: cycle found while processing triggers:
    chain of packages whose triggers are or may be responsible:
      dracut -> dracut
    packages' pending triggers which are or may be unresolvable:
      dracut: /usr/lib/modprobe.d
    dpkg: error processing package dracut (--configure):
    triggers looping, abandoned

You may re-execute `# apt full-upgrade` and let it finish the trigger of dracut.

----

— Jack Wu (Original Author: Mag Mell)
