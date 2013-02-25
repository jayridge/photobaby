#!/bin/bash
###----------------------
# Simple bootstrap script

REPO=photobaby
OWNER=jayridge

###----------------------
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y git

SRC_DIR=/usr/local/src
GIT_DIR=/usr/local/src/${REPO}

if [ ! -d $SRC_DIR ]; then
    sudo mkdir -p -m 0777 $SRC_DIR
    sudo chmod 0777 $SRC_DIR
fi

if [ ! -d $GIT_DIR ]; then
    cd $SRC_DIR
    git clone https://github.com/${OWNER}/${REPO}.git
fi

sh $GIT_DIR/setup/new_computer.sh

