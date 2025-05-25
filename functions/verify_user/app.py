import json

# For demo only; in production, use DynamoDB or another persistent store
otp_store = {}

def lambda_handler(event, context):
    print("Verifying user:", event)

    if "body" in event:
        body = json.loads(event["body"])
    else:
        body = event

    phone_number = body.get("phone_number")
    otp = body.get("otp")

    if not phone_number or not otp:
        return {"statusCode": 400, "body": "Phone number and OTP required"}

    # For demo, check in-memory store
    if otp_store.get(phone_number) == otp:
        return {"statusCode": 200, "body": "User is verified"}
    else:
        return {"statusCode": 401, "body": "Invalid OTP"}