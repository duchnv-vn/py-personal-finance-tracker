#!bin/bash

LAYER_NAME=$1
SERVICE_DIR=$2
LAYER_DIR=$SERVICE_DIR/layers/$LAYER_NAME/python
ZIP_NAME="$LAYER_NAME"LambdaLayer

cd ./$LAYER_DIR

pip3 install -r requirements.txt -t ./libs

cd ..

zip -r9 $ZIP_NAME python -x python/requirements.txt

mv $ZIP_NAME.zip ../zip-files

exit 0
