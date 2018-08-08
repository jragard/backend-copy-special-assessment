#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse


def get_special_paths(dir):
    os.chdir(dir)
    dirlist = os.listdir(dir)
    abs_path = os.getcwd()
    special_files = []
    final_files_list = []

    for file in dirlist:
        special_match = re.search(r'_\_\w*\_\_', file)
        if special_match:
            special_files.append(file)

    for file in special_files:
        final_files_list.append(abs_path + '/' + file)
        
    return final_files_list


def copy_to(paths, dir):

    for path in paths:
        if os.path.exists(dir):
            shutil.copy(path, dir)
        else:
            os.makedirs(dir)
            shutil.copy(path, dir)
    
# zip -j tmp.zip /Users/jeffreyagard/Desktop/python/backend-copy-special-assessment/zz__something__.jpg   
def zip_to(paths, zippath):
    string = ""
    for path in paths:
        string+= " " + path
    # print "string ", string
    print "Command I'm going to do:"
    command = "zip -j " + zippath + string
    print command
    cmd_output = commands.getstatusoutput(command)

    if cmd_output != 0:
        print cmd_output[1]   

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='dir to search for special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    special_paths = get_special_paths(args.from_dir)
    
    if args.todir == None and args.tozip == None:
        for path in special_paths:
            print path
    elif args.todir != None and args.tozip == None:
        copy_to(special_paths, args.todir)
    elif args.todir == None and args.tozip != None:
        zip_to(special_paths, args.tozip)
    elif args.todir != None and args.tozip != None:
        copy_to(special_paths, args.todir)
        zip_to(special_paths, args.tozip)




        

    
   

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
  
if __name__ == "__main__":
    main()
