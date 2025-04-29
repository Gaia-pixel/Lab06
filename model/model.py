from database import sales_DAO, anno_DAO, brand_DAO, retailer_DAO

class Model:
    def __init__(self):
        pass

    def get_anni(self):
        return anno_DAO.get_anni()

    def get_brand(self):
        return brand_DAO.get_brand()

    def get_retailer(self):
        return retailer_DAO.get_retailer()

    def get_sales(self, anno, brand, retailer):
        elencoVendite = sales_DAO.get_sales(anno, brand, retailer)
        elencoVendite.sort(reverse=True)
        return elencoVendite

