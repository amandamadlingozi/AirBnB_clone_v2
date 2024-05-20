#!/usr/bin/python3
# Fabric script to generate a .tgz archive from the contents of the web_static folder

from fabric.api import local
import time
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

        # Generate the archive name
        timestamp = time.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(timestamp)

        # Create the archive
        command = "tar -cvzf {} web_static".format(archive_name)
        result = local(command)

        # Check if the archive was created successfully and return the path or None
        if result.succeeded:
            return archive_name
        else:
            return None

