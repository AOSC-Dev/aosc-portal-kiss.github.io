---
layout: post
title: 'Updates Withdrawn from Stable'
type: news
important: true
---

Within the past 24 hours, 73 updates were accidentally uploaded to the Stable
repository (intended for Stable-Proposed). In particular, an update to LDNS
(`ldns`, 1.7.0-3 => 1.7.1) have broken OpenSSH (`openssh`), OpenSSH-HPN
(`openssh-hpn`), and DNSCrypt Proxy (`dnscrypt`). To mitigate this issue,
please issue the following command:

```
# apt install ldns=1.7.0-3
```

We are not aware of any other issue caused by this incident. We will be merging
changes from Stable-Proposed on Friday or Tuesday, UTC time. Before then, if you
you have applied the mitigation from above, you should not run into other issues.

However, as the updates were withdrawn, some packages installed on your system
will now show up with `local` markers, meaning that a specific version of a
package installed on your system is not found on the repository enabled by
your configuration. The Stable-Proposed merge in the coming days will result in
a wave of updates which will render your system consistent with the repository
again. In short, these `local` markers are temporary and should not affect
system functionality.

We apologise for any inconvenience that we may have caused. If you run into other
issues after updating your system, please don't hesistate to
[inform us](https://github.com/AOSC-Dev/aosc-os-abbs/issues/new/choose/).

----

Attachment: List of Packages Affected by the Withdrawal

```
stable: babl 0.1.74-0 (amd64)                   => stable-proposed
stable: brial 1.2.7-0 (amd64)                   => stable-proposed
stable: chromium 80.0.3987.116-0 (amd64)        => stable-proposed
stable: cimg 2.8.4-0 (amd64)                    => stable-proposed
stable: clblast 1.5.1-0 (amd64)                 => stable-proposed
stable: cln 1.3.6-0 (amd64)                     => stable-proposed
stable: exempi 2.5.1-0 (amd64)                  => stable-proposed
stable: folks 0.13.2-0 (amd64)                  => stable-proposed
stable: fox 1.7.67-0 (amd64)                    => stable-proposed
stable: fplll 5.3.2-0 (amd64)                   => stable-proposed
stable: gdk-pixbuf 2.38.2-0 (amd64)             => stable-proposed
stable: glib-networking 2.62.3-0 (amd64)        => stable-proposed
stable: gloox 1.0.23-0 (amd64)                  => stable-proposed
stable: gnupg 2.2.19-0 (amd64)                  => stable-proposed
stable: gnutls 3.6.12-0 (amd64)                 => stable-proposed
stable: goffice 0.10.46-0 (amd64)               => stable-proposed
stable: google-chrome 80.0.3987.116-0 (amd64)   => stable-proposed
stable: gsasl 1.8.1-0 (amd64)                   => stable-proposed
stable: gsoap 2.8.98-0 (amd64)                  => stable-proposed
stable: gssdp 1.2.2-0 (amd64)                   => stable-proposed
stable: gupnp 1.2.2-0 (amd64)                   => stable-proposed
stable: http-parser 2.9.3-0 (amd64)             => stable-proposed
stable: ibus-hangul 1.5.3-0 (amd64)             => stable-proposed
stable: ibus-table 1.9.25-0 (amd64)             => stable-proposed
stable: krusader 2.7.2-0 (amd64)                => stable-proposed
stable: ktorrent 5.1.2-0 (amd64)                => stable-proposed
stable: ldns 1.7.1-0 (amd64)                    => stable-proposed
stable: libabw 0.1.3-0 (amd64)                  => stable-proposed
stable: libasr 1.0.4-0 (amd64)                  => stable-proposed
stable: libcap-ng 0.7.10-0 (amd64)              => stable-proposed
stable: libcdr 0.1.6-0 (amd64)                  => stable-proposed
stable: libepoxy 1.5.4-0 (amd64)                => stable-proposed
stable: libfdk-aac 2.0.1-0 (amd64)              => stable-proposed
stable: libgcrypt-static 1.8.5-0 (amd64)        => stable-proposed
stable: libgee 0.20.3-0 (amd64)                 => stable-proposed
stable: libgovirt 0.3.7-0 (amd64)               => stable-proposed
stable: libgpiod 1.4.2-0 (amd64)                => stable-proposed
stable: libgusb 0.3.3-0 (amd64)                 => stable-proposed
stable: libjpeg-turbo 2.0.4-0 (amd64)           => stable-proposed
stable: liblangtag 0.6.3-0 (amd64)              => stable-proposed
stable: libmicrohttpd 0.9.70-0 (amd64)          => stable-proposed
stable: libmirage 3.2.4-0 (amd64)               => stable-proposed
stable: libmtp 1.1.17-0 (amd64)                 => stable-proposed
stable: libpcap 1.9.1-0 (amd64)                 => stable-proposed
stable: libphonenumber 8.11.4-0 (amd64)         => stable-proposed
stable: libpst 0.6.74-0 (amd64)                 => stable-proposed
stable: libpwquality 1.4.2-0 (amd64)            => stable-proposed
stable: libqmi 1.24.4-0 (amd64)                 => stable-proposed
stable: librsvg 2.46.4-0 (amd64)                => stable-proposed
stable: libshake 0.3.1-0 (amd64)                => stable-proposed
stable: libsigrokdecode 0.5.3-0 (amd64)         => stable-proposed
stable: libsmbios 2.4.3-0 (amd64)               => stable-proposed
stable: libsolv 0.7.11-0 (amd64)                => stable-proposed
stable: libsoup 2.68.3-0 (amd64)                => stable-proposed
stable: libtorrent-rasterbar 1.2.4-0 (amd64)    => stable-proposed
stable: libuv 1.34.2-0 (amd64)                  => stable-proposed
stable: libvisio 0.1.7-0 (amd64)                => stable-proposed
stable: linux-kernel-5.5.4 5.5.4-1 (amd64)      => stable-proposed
stable: mbedtls 2.16.4-0 (amd64)                => stable-proposed
stable: mesa 19.3.4-0 (amd64)                   => stable-proposed
stable: mtdev 1.1.6-0 (amd64)                   => stable-proposed
stable: netcdf 4.7.3-0 (amd64)                  => stable-proposed
stable: ntl 11.4.3-0 (amd64)                    => stable-proposed
stable: pango 1.44.7-0 (amd64)                  => stable-proposed
stable: protobuf-c 1.3.3-0 (amd64)              => stable-proposed
stable: snappy 1.1.8-0 (amd64)                  => stable-proposed
stable: source-highlight 3.1.9-0 (amd64)        => stable-proposed
stable: talloc 2.3.1-0 (amd64)                  => stable-proposed
stable: tevent 0.10.2-0 (amd64)                 => stable-proposed
stable: tpm2-tss 2.3.3-0 (amd64)                => stable-proposed
stable: vte-gtk3 0.58.3-0 (amd64)               => stable-proposed
stable: zfs 0.8.3-0 (amd64)                     => stable-proposed
stable: zfs 0.8.3-1 (amd64)                     => stable-proposed
```

----

— Mingcong Bai
