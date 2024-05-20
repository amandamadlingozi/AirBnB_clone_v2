#!/usr/bin/python3
# Fabric script that deletes out-of-date archives

from fabric.api import env, local, run
from fabric.context_managers import lcd, cd

# Defining the list of hosts
env.hosts = ['<IP web-01>', '<IP web-02>']

def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Arguments:
    number -- number of archives to keep (including the most recent)
    0 or 1 means keep only the most recent version
    """
    number = int(number)

    if number <= 1:
        number = 1

        # Cleaning local archives
        with lcd("versions"):
            local_archives = sorted(local("ls -tr", capture=True).split())
            archives_to_delete = local_archives[:-number]
            for archive in archives_to_delete:
                local("rm ./{}".format(archive))

                # Cleaning remote archives
                with cd("/data/web_static/releases"):
                    remote_archives = sorted(run("ls -tr").split())
                    remote_archives = [archive for archive in remote_archives if "web_static_" in archive]
                    archives_to_delete = remote_archives[:-number]
                    for archive in archives_to_delete:
                        run("rm -rf ./{}".format(archive))


