#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--prefix=/usr \
			 --disable-examples \
			 --disable-static \
			 --enable-polkit \
			 --disable-volume-search \
			 --with-daemon-user=colord \
			 --enable-introspection \
			 --enable-vala \
			 --libexecdir=/usr/libexec ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
