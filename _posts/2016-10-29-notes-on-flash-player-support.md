---
layout: post
title: 'Notes on Flash Player Support'
type: news
important: false
---

With the recently released Google Chrome (`google-chrome`) 54, Pepper API-based Flash Player plugin no longer comes bundled with the browser - however, Adobe has generously released a standalone version of Flash Player plugin for the Pepper API - and released under the terms of LGPL.

That means we may now ship the Flash Player plugin as a package in our repository, you would need to install the following packages for Flash functionality:

- Firefox: install `flashplayer-ppapi` and `freshplayerplugin`.
- Chromium and Google Chrome: install `flashplayer-ppapi`.