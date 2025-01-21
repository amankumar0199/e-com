import json
import requests
from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
def place_order(request):
    AZURE_FUNCTION_URL = "https://demoorderprocessing.azurewebsites.net/api/order_processor"
    username = request.user.username

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            order_data = json.dumps({
                "order_id": order.id,
                "customer_name": order.customer_name,
                "product_name": order.product_name,
                "quantity": str(order.quantity),
            })

            try:
                # Send a POST request to the Azure Function
                response = requests.post(AZURE_FUNCTION_URL, json=order_data)
                response.raise_for_status()

                # If successful, update order status
                order.status = 'PROCESSED'
                order.save()
                return redirect('order_success')

            except requests.exceptions.RequestException as e:
                # Log the error and update order status
                print(f"Error sending order to Azure Function: {e}")
                order.status = 'FAILED'
                order.save()

                # Redirect to an error page
                return redirect('order_failure')


            # send_order(order_data)


    else:
        form = OrderForm()
    return render(request, 'orders/place_order.html', {'form': form, 'username':username})

def order_success(request):
    return render(request, 'orders/order_success.html')

def order_failure(request):
    return render(request, 'orders/order_failure.html', {"message": "Order processing failed. Please try again."})