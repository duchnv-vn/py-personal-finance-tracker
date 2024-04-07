#!bin/bash

LAYER_NAME=$1
SERVICE_NAME=$2
LAYER_DIR=$SERVICE_NAME/layers/$LAYER_NAME
ZIP_NAME="$LAYER_NAME"LambdaLayer

cd ./$LAYER_DIR

zip -r $ZIP_NAME .

mv ./$ZIP_NAME.zip ../zip-files

exit 0