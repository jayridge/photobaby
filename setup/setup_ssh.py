#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import errno
import getpass
import urllib2
import json

def usage():
    print >> sys.stderr, "usage: %s repo_name repo_owner" % (sys.argv[0])
    exit(1)

if getpass.getuser() != "ubuntu":
    print >> sys.stderr, "error: must run as user ubuntu"
    usage()
if len(sys.argv) != 3:
    usage()
REPO_NAME = sys.argv[1]
REPO_OWNER = sys.argv[2]


def authorized_keys(repo_name, repo_owner):
    keys = []
    resp = urllib2.urlopen("https://api.github.com/repos/%s/%s/collaborators" % (repo_owner, repo_name)).read()
    collabs = json.loads(resp)
    for user in collabs:
        login = user.get("login")
        resp = urllib2.urlopen("https://api.github.com/users/%s/keys" % (login)).read()
        for e in json.loads(resp):
            keys.append(e.get("key"))
    return '\n'.join(keys)

def setup_ssh(repo_name, repo_owner):
    dir = '/home/ubuntu/.ssh'
    if not os.path.exists(dir):
        os.mkdir(dir, 0700)
    keys = authorized_keys(repo_name, repo_owner)
    keys_file = '/home/ubuntu/.ssh/authorized_keys'
    f = open(keys_file, 'a')
    f.write(keys + '\n')
    f.close()
    os.chmod(keys_file, 0600)

setup_ssh(REPO_NAME, REPO_OWNER)
