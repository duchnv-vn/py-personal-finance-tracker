import json


def createExpense(event, context):
    request_body = event["body"]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Created expenses successfully.",
            "success": True,
            "data": json.loads(request_body)
        })
    }
