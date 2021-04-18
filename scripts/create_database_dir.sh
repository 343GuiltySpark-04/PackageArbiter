#!/bin/bash

db_dir="/usr/local/packageArbiter/db"

sudo mkdir -p $db_dir

# shellcheck disable=SC2164
cd $db_dir

sudo touch ./db.yaml

sudo chown root:wheel ./db.yaml

sudo chmod g+w ./db.yaml
