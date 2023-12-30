---
categories:
  - warning
title: "[紧急] kmod 更新后会导致系统无法启动"
date: 2023-12-31T02:26:59+08:00
important: true
draft: false
---

我们发现近期引入的软件包 `kmod` 的更新会导致无法正常加载 xz 压缩的内核模块，并且影响初始化内存盘 (initramfs) 引导期间的启动过程，最终导致系统无法启动。
此问题具体表现为启动时报告以下错误信息：
```
decompression failed with status 6
systemd[1]: Failed to start systemd-module-load.service.
dracut: FATAL: iscsiroot requested but kernel/initrd does not support iscsi
```

如果您恰好更新过系统，请立即将 kmod 降级到版本 30-1 :
```
sudo oma install kmod:30-1
```
如果您尚未更新系统，请暂时不要更新，或者保持 `kmod` 软件包的版本为 `30-1`，并锁定该软件包： `sudo apt-mark hold kmod`  。我们会尽快找到问题根源，并尽早发布该软件包的更新。

---
~Cyan
