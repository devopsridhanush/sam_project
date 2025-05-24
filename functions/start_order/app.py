import json
import boto3
import os

stepfunctions = boto3.client('stepfunctions')

def lambda_handler(event, context):
    print("Received event:", event)

    # Sample order details
    order_data = {
        "order_id": "1234",
        "item": "Laptop",
        "price": 1000,
        "customer_email": "john@example.com"
    }

    # Get the Step Function ARN from environment variables
    state_machine_arn = os.environ.get("STATE_MACHINE_ARN")

    # Start Step Function execution
    response = stepfunctions.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(order_data)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Order received. Step Function started.",
            "executionArn": response["executionArn"]
        }),
    }
