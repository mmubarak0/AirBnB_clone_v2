#!/usr/bin/python3
"""Fabric script that extract a .tgz of the contents of the web_static."""

from fabric.api import local, env, run, put, hide
import re
import os
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ["54.236.25.195", "54.172.57.3"]


def do_deploy(archive_path):
    """Extract the archive file."""
    with hide('output'):
        if os.path.isfile(archive_path):
            try:
                put(archive_path, '/tmp/')
                run(f"tar -zxvf /tmp/{archive_path[9:]} \
-C /data/web_static/releases/")
                run(f"rm -rf /data/web_static/releases/{archive_path[9:-4]}")
                run(f"mv -f /data/web_static/releases/{archive_path[9:19]} \
/data/web_static/releases/{archive_path[9:-4]}")
                run(f"rm -f /tmp/{archive_path[9:]}")
                run("rm -f /data/web_static/current")
                run(f"ln -s /data/web_static/releases/{archive_path[9:-4]} \
/data/web_static/current")
                return True
            except Exception:
                return False
        else:
            return False
