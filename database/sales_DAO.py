from database.DB_connect import DBConnect
from model.sales import Sales


def get_sales(anno, brand, retailer):
    cnx = DBConnect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT gds.*, gds.Unit_sale_price*gds.Quantity as Ricavo
                FROM go_daily_sales gds, go_products gp, go_retailers gr 
                WHERE gds.Retailer_code = gr.Retailer_code and gds.Product_number = gp.Product_number
                and (YEAR(gds.`Date`) = COALESCE(%s, YEAR(gds.`Date`)))
                and (gp.Product_brand = COALESCE(%s, gp.Product_brand)) 
                and (gr.Retailer_name = COALESCE(%s, gr.Retailer_name)) 
                """
        cursor.execute(query, (anno, brand, retailer))

        for row in cursor:
            result.append(
                Sales(row["Retailer_code"],
                         row["Product_number"],
                         row["Order_method_code"],
                         row["Date"],
                         row["Quantity"],
                         row["Unit_price"],
                         row["Unit_sale_price"],
                         row["Ricavo"]
                    ))



        cursor.close()
        cnx.close()

    return result






