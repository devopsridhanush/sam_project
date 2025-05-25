import json
import boto3
import os
import random

stepfunctions = boto3.client('stepfunctions')
# For demo only; use DynamoDB for production
otp_store = {}

def lambda_handler(event, context):
    print("Received event:", event)

    # Parse input from API Gateway (event['body'] is a JSON string)
    if "body" in event:
        body = json.loads(event["body"])
    else:
        body = event

    phone_number = body.get("phone_number")
    order_id = body.get("order_id")
    item = body.get("item")
    price = body.get("price")
    customer_email = body.get("customer_email")

    if not phone_number:
        return {"statusCode": 400, "body": "Phone number required"}

    # Generate OTP and (simulate) send via SMS
    otp = str(random.randint(100000, 999999))
    otp_store[phone_number] = otp
    print(f"Simulated sending OTP {otp} to {phone_number}")

    # For demo, return OTP in response (do NOT do this in production)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "OTP sent to your phone number.",
            "otp": otp  # For demo only
        }),
    }
