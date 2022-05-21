#!/usr/bin/python3
# File: 1-pack_web_static.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Fabric script generates .tgz archive of all in web_static/ using 'do_pack'
Usage: fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archine from contents of web_static
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except IOError:
        return None
