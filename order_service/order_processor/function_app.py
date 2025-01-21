import azure.functions as func
import json
import logging
from datetime import datetime

# Create the Azure Function App
app = func.FunctionApp()

# Define the route for order processing
@app.route(route="order_processor", auth_level=func.AuthLevel.ANONYMOUS)
def order_processor(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Order Processor function triggered.')

    try:
        # Parse the request body for order data
        req_body = req.get_json()
        logging.info(f"Received order data: {req_body}")

        # Extract necessary details from the request
        order_id = req_body.get('order_id')
        customer_name = req_body.get('customer_name', 'Unknown Customer')
        items = req_body.get('items', [])
        total_price = sum(item.get('price', 0) * item.get('quantity', 1) for item in items)

        # Simulate order processing (e.g., saving to database, notifying user, etc.)
        processed_time = datetime.utcnow().isoformat()
        logging.info(f"Order {order_id} processed for {customer_name} at {processed_time}")

        # Response payload
        response = {
            "order_id": order_id,
            "customer_name": customer_name,
            "items_processed": len(items),
            "total_price": total_price,
            "processed_at": processed_time,
            "status": "success"
        }

        # Return a successful response
        return func.HttpResponse(
            json.dumps(response),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error processing the order: {str(e)}")
        return func.HttpResponse(
            f"Error processing order: {str(e)}",
            status_code=500
        )
