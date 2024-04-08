from libs import boto3

dynamodb = boto3.resource('dynamodb')
personal_expense_table = dynamodb.Table("personal_expenses")


def find_all():
    response = personal_expense_table.query(
        KeyConditions={},
        Select='ALL_ATTRIBUTES'
    )

    return response
