#!bin/bash

declare -A variables=()

variables["service"]=SERVICE_NAME
variables["stage"]=STAGE_NAME
variables["region"]=REGION_NAME
variables["functions"]=FUNCTION_NAMES

for argument in "$@"; do
    if [[ $argument == *"="* ]]; then
        argument_label=${argument%=*}
    else
        echo "Invalid option $argument"
        exit 1
    fi

    if [[ -n ${variables[$argument_label]} ]]; then
        declare ${variables[$argument_label]}="${argument#$argument_label=}"
    fi
done

if [ -z "$SERVICE_NAME" ]; then
    echo "Missing service name"
    echo "----- STOPPED -----"
    exit 1
elif [ -z "$STAGE_NAME" ]; then
    echo "Missing stage name"
    echo "----- STOPPED -----"
    exit 1
fi

source .env.$STAGE_NAME

REGION_NAME="${REGION_NAME:-$DEFAULT_REGION}"
SERVICE_DIR=$SERVICE_NAME-service

for layer_path in "$SERVICE_DIR/layers"/*; do
    layer_name="${layer_path#*/layers/}"

    if [[ $layer_name == "zip-files" ]]; then
        continue
    fi

    npm run layer:zip $layer_name $SERVICE_DIR
done

cd ./$SERVICE_DIR

if [ ! -z "$FUNCTION_NAMES" ]; then
    IFS=',' read -a FUNCTIONS_ARRAY <<<"$FUNCTION_NAMES"

    for FUNCTION_NAME in "${FUNCTIONS_ARRAY[@]}"; do
        echo "----- DEPLOYING FUNCTION $FUNCTION_NAME -----"
        AWS_PROFILE=$USER_PROFILE \
            sls deploy \
            --function $FUNCTION_NAME \
            --stage $STAGE_NAME \
            --region $REGION_NAME
        echo "----- DEPLOYED FUNCTION $FUNCTION_NAME SUCCESSFULLY -----"
    done
else
    echo "----- DEPLOYING ALL FUNCTIONS -----"
    AWS_PROFILE=$USER_PROFILE \
        sls deploy \
        --stage $STAGE_NAME \
        --region $REGION_NAME
    echo "----- DEPLOYING ALL FUNCTIONS SUCCESSFULLY -----"
fi

exit 0
