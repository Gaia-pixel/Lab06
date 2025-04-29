

class Retailer:

    retailer_code: int
    retailer_name: str
    type: str
    country: str

    def __init__(self, retailer_code, retailer_name, type, country):
        self.retailer_code = retailer_code
        self.retailer_name = retailer_name
        self.type = type
        self.country = country
