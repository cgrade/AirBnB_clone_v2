#!/usr/bin/python3
from fabric.api import *
import os


env.hosts = ['54.224.21.248', '100.25.28.51']
env.user = 'ubuntu'


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, '/tmp/')

    # Get the archive filename without extension
    archive_filename = os.path.basename(archive_path)
    archive_filename_noext = os.path.splitext(archive_filename)[0]

    # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    run('mkdir -p /data/web_static/releases/{}'.format(archive_filename_noext))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_filename, archive_filename_noext))

    # Delete the archive from the web server
    run('rm /tmp/{}'.format(archive_filename))

    # Delete the symbolic link /data/web_static/current from the web server
    run('rm -f /data/web_static/current')

    # Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(archive_filename_noext))

    return True
