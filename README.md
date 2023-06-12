# MVP
## Ecommerce website/App
## AKO SHOP “MVP specification”
Architecture

The minimum viable product (MVP) for the Ako Shop ecommerce/App would typically include the essential features that allow users to create, manage, update and delete items in the shopping cart, it alway give the options for non register user to add, delete and make payment in the checkout page. There are various payments option for both users and guest users. Here are some key features that should be included in an MVP for the Ako Shop ecommerce/App:
1. Users should be able to create new account and login to have access to manage product, order and item order.
2. Non register users would have the ability to add items, delete items in the shopping cart and also make payment
3. Gives the option of continue shopping for both register and non register users at cart stage. The quantity of items can be added or removed by using the down and up arrows.
4. Provide section for shipping address for registered users and non registered user, but for digital products the shipping address is hiden.

## STEPS FOR THE DEVELOPMENT IN DJANGO FRAMEWORK
## SETUP THE APP AND INSTALL FRAMEWORK
### Part 1 | Configure App
1. install the virtual enviroment and Django installed and created our first project using  django-admin startproject “ecommerce”.
2. Create the first app files with python manage.py startapp “store". 
3. Add app to settings.py

### Part 2 | Templates
1. create a folder to store our templates. Our html files will be stored within our app inside a folder called "templates".
2. inside the templates folder create another folder with the same name as the app. In this case if you called your app "store", like I did, then that should be the name of the folder.
3. Main.html → Template which all will inherit from
4. Store.html → Home page/store front with all products
5. Cart.html → Users shopping cart
6.  Checkout.html → Checkout page

### Part 3 | Views & URLs
1. Inside your apps views.py file created 3 views, store, cart, checkout. I created some "url paths" to call these views.
2. I Created a file called "urls.py" inside your app. Inside the app import “path” along with the “views” and create a urlpatterns list. Inside "urlpatterns " create 3 paths, one for each view and give them a name.
3. Base URLs Configuration. import "inlcude" just after "path" and add a path that points to the new urls.py we created inside "store". from django.contrib import admin, from django.urls import path, include

### Part 4 | Static Files
1. Created a folder called "static" in the  root directory.
2. Inside the new “static” folder, I created a folder called "CSS" and another called "Images". These files will hold all of our CSS and Images.
3. Inside the CSS folder, I created a file call main.css.
4. i configured things in settings.py and then add this link os.path.join(BASE_DIR, 'static') to our template.

## DATA STRUCTURE and Algorithm 
### Part 1 | Models
1. Database Models
2. ![models](https://github.com/Akoatem/MVP/assets/71437843/28c53851-1891-4bf6-9e15-0649e0029872)
3. User- Built in Dango user model. An instance of this model will be created for each customer that registers with our website. This model will give us the ability to later use Djangos default authentication system without having to manually set this up ourselves.
4. Customer - Along with a User model each customer will contain a Customer model that holds a one to one relationship to each user. (OneToOneField). 
5. Product - The product model represents products we have in store.
6. Order - The order model will represent a transaction that is placed or pending. The model will hold information such as the transaction ID, data completed and order status. This model will be a child or the customer model but a parent to Order Items.
7. OrderItem- An order Item is one item with an order. So for example a shopping cart may consist of many items but is all part of one order. Therefore the OrderItem model will be a child of the PRODUCT model AND the ORDER Model.
8. ShippingAddress- Not every order will need shipping information. For orders containing physical products that need to be shipping we will need to create an instance of the shipping model to know where to send the order. Shipping will simply be a child of the order model when necessary.

### Part 2 | Render Products
1. Query Products- In our apps views.py file, I first imported all our models and then query the products within our store view. I  added "products" into the context dictionary.
2. Render Products - Loop Through Products, Replace Fields for Product Price and Product Name
3. Product Image Field
4. ImageField()
5. User Cart- attach a customer to our user, and add some order items to go with the order which we will manually create from the admin panel.


## AKO SHOP ECOMMERCE WEBSITE/APP

<img width="960" alt="Screenshot (53)" src="https://github.com/Akoatem/MVP/assets/71437843/612638db-e985-4a2c-b1e8-594aae2181cd">
<img width="967" alt="Screenshot (57)" src="https://github.com/Akoatem/MVP/assets/71437843/765460f6-ea3c-43b4-94a0-7ae95fc6dc03">
<img width="967" alt="Screenshot (54)" src="https://github.com/Akoatem/MVP/assets/71437843/143f3b0c-dce1-4a3a-9bd1-ac1bc89cbd00">
<img width="963" alt="Screenshot (55)" src="https://github.com/Akoatem/MVP/assets/71437843/112a692d-62ed-491e-b3ff-4842caba2062">
<img width="942" alt="Screenshot (56)" src="https://github.com/Akoatem/MVP/assets/71437843/20898f14-fb4c-47ea-aa86-d37f5fe7d5fc">


# I AM STILL WORKING ON THE PROJECT TO ADD MORE FUNCTIONALITIES
