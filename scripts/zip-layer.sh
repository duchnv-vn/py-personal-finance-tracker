#!bin/bash

LAYER_NAME=$1
SERVICE_DIR=$2
LAYER_DIR=$SERVICE_DIR/layers/$LAYER_NAME
ZIP_NAME="$LAYER_NAME"LambdaLayer

cd ./$LAYER_DIR

pip3 install -r requirements.txt -t ./python_libs

zip -r $ZIP_NAME .

mv ./$ZIP_NAME.zip ../zip-files

exit 0
