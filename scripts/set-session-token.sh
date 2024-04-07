#!bin/bash

source .env

TOKEN_CODE=$1

aws configure set aws_access_key_id $ACCESS_KEY_ID --profile $USER_PROFILE
aws configure set aws_secret_access_key $SECRET_ACCESS_KEY --profile $USER_PROFILE
aws configure set aws_session_token "" --profile $USER_PROFILE

CREDENTIAL_JSON=$(aws sts get-session-token \
    --serial-number $USER_PHONE_AUTHORIZATOR_SERIAL_NUMBER \
    --token-code $TOKEN_CODE \
    --profile $USER_PROFILE)

ACCESS_KEY_ID=$(echo $CREDENTIAL_JSON | jq -r ".Credentials.AccessKeyId")
SECRET_ACCESS_KEY=$(echo $CREDENTIAL_JSON | jq -r ".Credentials.SecretAccessKey")
SESSION_TOKEN=$(echo $CREDENTIAL_JSON | jq -r ".Credentials.SessionToken")

if [ ! -z "$SESSION_TOKEN" ]; then
    aws configure set aws_access_key_id $ACCESS_KEY_ID --profile $USER_PROFILE
    aws configure set aws_secret_access_key $SECRET_ACCESS_KEY --profile $USER_PROFILE
    aws configure set aws_session_token $SESSION_TOKEN --profile $USER_PROFILE
    echo "----- SET SESSION TOKEN SUCCESSFULLY -----"
else
    echo "----- ERROR: CANNOT GET SESSION TOKEN -----"
fi

exit 0
