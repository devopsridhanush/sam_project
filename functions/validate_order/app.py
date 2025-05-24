def lambda_handler(event, context):
    print("Validating order:", event)

    # Simulate validation (always successful here)
    validation_result = {"is_valid": True}

    # Merge validation result into event and return
    event.update(validation_result)
    return event
