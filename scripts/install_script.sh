#!/bin/bash

#DO NOT RUN DIRECTLY USE THE BLOODY MAKEFILE

dest_dir="/usr/local/packageArbiter/bin"

sudo mkdir -p $dest_dir

cp ./* $dest_dir

sudo rm -f $dest_dir/setup.py

sudo chown -R root:wheel /usr/local/packageArbiter

sudo chmod -R g+w $dest_dir

sudo chmod +x $dest_dir/run.sh

sudo chmod -R g+w /usr/local/packageArbiter/scripts

sudo chmod -R +x /usr/local/packageArbiter/scripts

ln -s /usr/local/packageArbiter/bin/run.sh /usr/bin/packageArbiter
