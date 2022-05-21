#!/usr/bin/python3
# File: 2-do_deploy_web_static.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Fabric script method:
    do_deploy: deploys archive to webservers
Usage:
    fab -f 2-do_deploy_web_static.py
    do_deploy:archive_path=versions/web_static_20170315003959.tgz
    -i my_ssh_private_key -u ubuntu
"""

import os
from fabric.api import *
from fabric.operations import run, put, sudo

env.hosts = ['3.80.58.133', '34.148.138.30']


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        folder = archive.split(".")
        run("mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, folder[0]))
        run("rm /tmp/{}".format(archive))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))
        run("rm -rf {}/{}/web_static".format(path, folder[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, folder[0]))
        return True
    except IOError:
        return False
