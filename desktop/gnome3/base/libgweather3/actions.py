#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                         --enable-introspection=yes")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/icons/gnome/")
    pisitools.remove("/usr/share/libgweather/locations.dtd")
    pisitools.remove("/usr/share/libgweather/Locations.xml")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

