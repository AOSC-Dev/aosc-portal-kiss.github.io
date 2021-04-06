---
categories:
  - warning
title: Switch to `shadowsocks-rust`
date: 2021-03-28T09:51:00+08:00
important: false
---

The upstream of `shadowsocks-libev` has announced the project is now ["Bug-fix-only"](https://github.com/shadowsocks/shadowsocks-libev),
and recommended users of `shadowsocks-libev` using `shadowsocks-rust` instead.

    # apt update && apt install shadowsocks-rust

If you had enabled `shadowsocks-libev` local proxy service before, you can use the following commands to switch to `shadowsocks-rust` service.

    # systemctl disable --now shadowsocks-libev@[config]
    # systemctl enable --now shadowsocks-rust-local@[config]

----

—— Jack Wu
