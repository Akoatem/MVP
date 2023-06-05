import json
from .models import *

def cookieCart(request):
    #Create empty cart for now for non-logged in user
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
            
        print('Cart:', cart)
        items = []
        order = {'get_cart_total':0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']
        
        # to update cart items to see in cart page
        for i in cart:
            #We use try block to prevent items in cart that may have been removed from causing error
            try:
                cartItems += cart[i]["quantity"]
                
                product = Product.objects.get(id=i)
                total =(product.price * cart[i]["quantity"] )
                
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']
                # To build our cart with actual items on it
                item = {
                    'id':product.id,
                    'product':{'id':product.id,'name':product.name, 'price':product.price, 
                    'imageURL':product.imageURL}, 'quantity':cart[i]['quantity'],
                    'digital':product.digital,'get_total':total,
                    }
                items.append(item)
                
                if product.digital == False:
                    order['shipping'] = True
            except:
                pass
        return {'cartItems':cartItems ,'order':order, 'items':items}
    
def cartData(request):
    # This is for authenticated user
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
     # This is for non authenticated user
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return {'cartItems':cartItems ,'order':order, 'items':items}


def guestOrder(request, data):
    # logic for authenticated users
        print('User is not logged in')
        # To submit the data into the back-end
        print('COOKIES:', request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']
        
        # To get the items by accessing the cookie data
        cookieData = cookieCart(request)
        items = cookieData['items']
        
        # for guest user who want to shop in the website but never created and account
        # when the user send an email, this will be check in our database it will be attach
        # we can see how many times a guest user has shop with us
        customer, created = Customer.objects.get_or_create(
				email=email,
				)
        customer.name = name
        customer.save()

        order = Order.objects.create(
            customer=customer,
            complete=False,
			)
        # To add the items in the database
        
        for item in items:
            product = Product.objects.get(id=item['id'])
            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity'],
            )
        return  customer, order
