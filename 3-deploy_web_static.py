#!/usr/bin/python3
# File: 3-deploy_web_static.py
# Author: Alex Orland Arévalo Tribaldos
# email: <3915@holbertonschool.com>

"""
Fabric script methods:
    do_pack: packs web_static/ files into .tgz archive
    do_deploy: deploys archive to webservers
    deploy: do_packs && do_deploys
Usage:
    fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""
import os
import os.path
from datetime import datetime
from fabric.api import *
from fabric.operations import env, put, run, local

env.hosts = ['3.80.58.133', '34.148.138.30']
env.user = 'ubuntu'
created_path = None


@runs_once
def do_pack():
    """
    Generates a .tgz archine from contents of web_static
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("mkdir -p versions")
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Using fabric to distribute archive
    """
    try:
        filename = archive_path.split("/")[-1]
        onlyname = filename.split(".")[0]
        uncompress_path = "/data/web_static/releases/{}".format(onlyname)
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}/'.format(uncompress_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(filename, uncompress_path))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {0}/web_static/* {0}/'.format(uncompress_path))
        run('sudo rm -rf {}/web_static'.format(uncompress_path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}/ /data/web_static/current'.format(uncompress_path))
        print('New version deployed!')
        return True
    except BaseException:
        print('Do it again')
        return False


def deploy():
    """
    Deploy function that creates/distributes an archive
    """
    archive_path = do_pack()
    if archive_path is None:
        print('Something happen')
        return False
    print('New tar created...starting deployment in 3,2,1....!')
    return do_deploy(archive_path)
