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

from fabric.api import *
from fabric.operations import run, put, sudo

env.hosts = ['3.80.58.133', '34.148.138.30']


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.
    """
    from os.path import exists

    if not exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    filename = archive_path.split('/')[1]
    run("mkdir -p /data/web_static/releases/{}".format(filename[0:-4]))
    run("tar -xzf {} -C {}".format("/tmp/" + filename,
        "/data/web_static/releases/" + filename[0:-4]))
    run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(filename[0:-4], filename[0:-4]))
    run("rm -rf /data/web_static/releases/{}/web_static")
    run("rm -f /tmp/{}".format(filename))
    run("rm /data/web_static/current")
    run('ln -sf /data/web_static/releases/{}\
        /data/web_static/current'.format(filename[0:-4]))
    sudo('service nginx restart')
    return True
