#!bin/bash

LAYER_NAME=$1
SERVICE_NAME_DIR=$2
LAYER_DIR=$SERVICE_NAME_DIR/layers/$LAYER_NAME/python

mkdir -p ./$LAYER_DIR

cd ./$LAYER_DIR

mkdir libs
touch requirements.txt
touch __init__.py

exit 0