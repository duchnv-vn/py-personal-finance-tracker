import json
from dynamodbClient import find_all


def handler(event, context):
    request_body = event["body"]

    response = find_all()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Created expenses successfully.",
            "success": True,
            "data": response
        })
    }
