#!/bin/bash


# shellcheck disable=SC2164
cd /usr/local/packageArbiter/cache/

touch ./foolib.tar

sudo chown root:wheel ./foolib.tar

sudo chmod g+w ./foolib.tar