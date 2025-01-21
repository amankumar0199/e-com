import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing a new order.")
    try:
        # Parse the incoming order data
        order_data = req.get_json()
        logging.info(f"Order data received: {order_data}")

        # Simulate order processing logic
        order_id = order_data.get("order_id")
        processed_time = "Order processed at some time."

        # Return a success response
        response = {
            "order_id": order_id,
            "status": "processed",
            "processed_at": processed_time
        }
        return func.HttpResponse(json.dumps(response), status_code=200, mimetype="application/json")

    except Exception as e:
        logging.error(f"Error processing order: {e}")
        return func.HttpResponse(f"Error: {e}", status_code=500)
