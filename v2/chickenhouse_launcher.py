#! /usr/bin/env python

# -*- coding: utf-8 -*-
# author: pBouillon - https://pierrebouillon.tech/

import os
from os      import fork
from os      import setsid
from os      import umask

def daemonize ():
    """Daemonize the script

    Does the first fork
    Then does the second
    Finally change the output of stderr in a log file
    """
    pid = fork ()
    if pid < 0:
        exit ('An error occured on the first fork')
    elif pid!=0:
        exit ()

    setsid()
    if pid < 0:
        exit ('An error occured on the second fork')
    elif pid!=0:
        exit ()

    sys.stderr = open ('./logs.txt', 'w+')

if __name__ == '__main__':
    daemonize ()
    controller = ChickenHouse_controller ()
    controller.poll ()
