#!/usr/bin/python3
"""Fabric script that generates a .tgz from the contents of the web_static."""

from fabric.api import local
import re
import os
from datetime import datetime


def do_pack():
    """Create archive file."""
    target = local("mkdir -p versions")
    name = str(datetime.now())
    year, month, day, hour, minute, second, frac = re.split("[: -.]", name)
    version = "".join([year, month, day, hour, minute, second, frac])
    tar = local(f"tar -cvzf versions/web_static_{version}.tgz web_static")
    if os.path.exists(f"./versions/web_static_{version}.tgz"):
        return os.path.normpath(f"/versions/web_static_{version}.tgz")
    else:
        return None
