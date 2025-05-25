import time

def lambda_handler(event, context):
    print("Processing payment for order:", event.get("order_id"))

    # Test for modifying the lambda function code

    # Simulate payment processing delay
    time.sleep(2)

    # Mock payment confirmation
    event["payment_status"] = "confirmed"
    return event
