#!/bin/bash

cache_dir="/usr/local/packageArbiter/cache"

sudo mkdir -p $cache_dir

# shellcheck disable=SC2164
cd $cache_dir

sudo chown -R root:wheel ../cache

sudo chmod -R g+w ../cache
