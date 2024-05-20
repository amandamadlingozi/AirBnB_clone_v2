#!/usr/bin/python3
# Fabric script that distributes an archive to web servers

from fabric.api import env, put, run
import os

# Defining list of hosts
env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Geting archive file name and the folder name without the extension
        archive_file = archive_path.split("/")[-1]
        archive_folder = archive_file.split(".")[0]

        # Uploading the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(archive_file))

        # Creating the directory where the archive will be uncompressed
        run("mkdir -p /data/web_static/releases/{}/".format(archive_folder))

        # Uncompressing the archive to the folder
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_file, archive_folder))

        # Deleting the archive from the web server
        run("rm /tmp/{}".format(archive_file))

        # Moving contents of the web_static folder to the right location
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_folder, archive_folder))

        # Deleting the empty web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_folder))

        # Deleting the existing symbolic link
        run("rm -rf /data/web_static/current")

        # Creating a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_folder))

        return True
    except:
        return False
    
