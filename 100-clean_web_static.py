#!/usr/bin/python3
# File: 100-clean_web_static.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Fabric script methods:
    do_pack(): packs web_static/ files into .tgz archive
    do_deploy(archive_path): deploys archive to webservers
    deploy(): do_packs && do_deploys
    do_clean(n=0): removes old versions and keeps n (or 1) newest versions only
Usage:
    fab -f 3-deploy_web_static.py do_clean:n=2 -i my_ssh_private_key -u ubuntu
"""
import os
from fabric.api import *

env.hosts = ['3.80.58.133', '34.148.138.30']


def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
