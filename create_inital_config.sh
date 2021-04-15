#!/usr/bin/env bash

config_dir="/etc/packageArbiter"

sudo mkdir $config_dir



# shellcheck disable=SC2164
cd $config_dir

sudo touch ./config.yaml


sudo chown -R root:wheel $config_dir


