def lambda_handler(event, context):
    print("Sending confirmation for order:", event.get("order_id"))
    
    # Simulate sending email confirmation
    event["confirmation_sent"] = True
    return event
