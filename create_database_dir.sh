#!/usr/bin/env bash

db_dir="/var/packageArbiter/package_db"

sudo mkdir -p $db_dir

# shellcheck disable=SC2164
cd $db_dir

sudo touch ./package_db.yaml