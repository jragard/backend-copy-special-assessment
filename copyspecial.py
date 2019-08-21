#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "???"


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = []
    paths = os.listdir(dirname)  # list of paths in that dir
    for fname in paths:
        # Yay regex!
        match = re.search(r'__(\w+)__', fname)
        if match:
            result.append(os.path.abspath(os.path.join(dirname, fname)))
    return result


def copy_to(paths, to_dir):
    """Copy all of the given files to the given dir, creating it if necessary."""
    if not os.path.exists(to_dir):
        os.makedirs(to_dir)
    for path in paths:
        fname = os.path.basename(path)
        shutil.copy(path, os.path.join(to_dir, fname))
        # could error out if already exists os.path.exists():


def zip_to(paths, zipfile):
    """Zip up all of the given paths into a new zipfile."""
    # compose a cmd line string
    cmd = ["zip", "-j", zipfile]
    cmd.extend(paths)
    print("Command I'm going to do: \n{}".format(' '.join(cmd)))

    # use subprocess to launch zip cmd line utility.
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        print(e.output)
        exit(e.returncode)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('dirs', help='src dirs to read special files from')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    args = parser.parse_args()

    if not args:
        print(parser.usage())
        exit(1)

    fromdir = args.dirs
    if not fromdir:
        print(parser.usage())
        exit(1)

    # Gather all the special files
    paths = []
    paths.extend(get_special_paths(fromdir))

    todir = args.todir
    tozip = args.tozip

    if todir:
        copy_to(paths, todir)
    elif tozip:
        zip_to(paths, tozip)
    else:
        print('\n'.join(paths))

    print('Completed.')


if __name__ == "__main__":
    main()
