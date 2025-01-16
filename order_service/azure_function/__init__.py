import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        order_data = req.get_json()
        logging.info(f"Processing order: {order_data}")

        # Simulate order processing
        logging.info(f"Order {order_data['order_id']} processed successfully.")

        return func.HttpResponse("Order processed successfully.", status_code=200)
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse("Failed to process order.", status_code=500)
