class Coffee:
    all_coffees = []

    def __init__(self, name):
        if isinstance(name, str) and (len(name) >= 3):
            self._name = name  # Use a private attribute with a leading underscore
            Coffee.all_coffees.append(name)
        else:
            raise Exception

    @property
    def name(self):  # Define a getter method for the name attribute
        return self._name
        

    def orders(self):
        matching_orders = []
        for order in Order.all:
            if order.coffee == self:
                matching_orders.append(order)
        return matching_orders
    
    def customers(self):
        matching_customers = set()
        for order in Order.all:
            if order.coffee == self:
                customer = order.customer
                matching_customers.add(customer)
        return list(matching_customers)
    
    def num_orders(self):
        coffee_orders = 0
        for order in Order.all:
            if order.coffee == self:
                coffee_orders += 1
        return coffee_orders
    
    def average_price(self):
        coffee_orders = 0
        coffee_sum = 0
        for order in Order.all:
            if order.coffee == self:
                coffee_orders += 1
                coffee_price = order.price
                coffee_sum += coffee_price
                average = coffee_sum / coffee_orders
        return average


class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(name)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str) and (len(new_name) >= 1) and (len(new_name) <= 15):
            self._name = new_name
        else:
            raise Exception
     
    def orders(self):
        matching_orders = []
        for order in Order.all:
            if order.customer == self:
                matching_orders.append(order)
        return matching_orders
    
    def coffees(self):
        matching_customers = set()
        for order in Order.all:
            if order.customer == self:
                coffee = order.coffee
                matching_customers.add(coffee)
        return list(matching_customers)
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        Order.all.append(order)
        return order


    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        if isinstance(price, float) and (price >= 1.0) and (price <= 10.0):
            self._price = price
        else:
            raise Exception
        Order.all.append(self)
    
    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception

