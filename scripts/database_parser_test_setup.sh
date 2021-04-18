#!/bin/bash

# shellcheck disable=SC2164
cd ../tests

cat > test.yaml << "EOF"

-
  name: foolib
  version: 0.1
  config_dir: /etc/foolib

EOF