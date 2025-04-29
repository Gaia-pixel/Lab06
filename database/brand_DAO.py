from database.DB_connect import DBConnect


def get_brand():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT gp.Product_brand as brand
                    FROM go_sales.go_products gp """
            cursor.execute(query)

            for row in cursor:
                result.append(
                    row["brand"])

            cursor.close()
            cnx.close()

        return result