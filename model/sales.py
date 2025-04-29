from datetime import datetime

class Sales():
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime.date
    Quantity: int
    Unit_price: float
    Unit_sale_price: float
    Ricavo: float

    def __init__(self, Retailer_code, Product_number, Order_method_code, Date, Quantity, Unit_price, Unit_sale_price, Ricavo):
        self.Retailer_code = Retailer_code
        self.Product_number = Product_number
        self.Order_method_code = Order_method_code
        self.Date = Date
        self.Quantity = Quantity
        self.Unit_price = Unit_price
        self.Unit_sale_price = Unit_sale_price
        self.Ricavo = Ricavo


    def __str__(self):
        return f"Data: {self.Date}, Ricavo: {self.Ricavo}, Retailer: {self.Retailer_code}, Product: {self.Product_number}"