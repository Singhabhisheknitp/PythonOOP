class Item:
    pay_rate = 0.8 # The pay rate after 20% discount its a gloabl attribute that means the value will be common across all the instances, unlike object related attributes which are different for different objects and cretaed while we create the instances of the object
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)  # this again is a global attribute of the class that you can access through calling on class directly & not the onject. it is just creating list of the objects  

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self): # what output you want while printing the objects of the class. default would be something like <class '__main__.Item'>
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
# we can always assign some additional attribute outside than constructor 
#for example item2.has_numpad= False
# we can also chnage the instance initialised variable done by constructor initially 
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)  # this will call the __repr__() method one by one for all instances
#please note here the class atrribute is also gets automatically assigned as instance attribute however its not printed but we can always use the same with item1. pay_rate
