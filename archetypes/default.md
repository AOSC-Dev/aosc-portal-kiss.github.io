---
categories:
  - news
title: "{{ replace (replaceRE "^\\d{4}-\\d{2}-\\d{2}-" "" .Name) "-" " " | title }}"
date: {{ .Date }}
important: false
draft: true
---

