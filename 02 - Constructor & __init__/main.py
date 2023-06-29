class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): # when this method is called instance are already created hence we use instance variable inside the function. 
        #it is always a prctice that we defne constructor function at the top so that the attributes can be used in methods below by just passing self as parameter to the methods
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)   #the moment we create object of the class it automatically sent to method init() as one arg
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
