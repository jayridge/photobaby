#!/bin/bash

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y git 

SRC_DIR=/usr/local/src
mkdir -p $SRC_DIR
cd $SRC_DIR
git clone https://github.com/jayridge/photobaby.git
