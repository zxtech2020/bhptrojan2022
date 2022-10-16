#!/usr/bin/env python3
#
# Hi There!
#aronlab
# need debug

#utf-8

import os

def run(**args):
    print("[*] In dirlister module.")
    files=os.listdir(".")
    return str(files)
  