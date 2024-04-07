#!bin/bash

LAYER_NAME=$1
SERVICE_NAME_DIR=$2
LAYER_DIR=$SERVICE_NAME_DIR/layers/$LAYER_NAME
ZIP_NAME="$LAYER_NAME"LambdaLayer

mkdir -p ./$LAYER_DIR

cd ./$LAYER_DIR

mkdir python_libs
touch requirements.txt

exit 0