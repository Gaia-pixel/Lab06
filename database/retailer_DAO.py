from database.DB_connect import DBConnect
from model.retailer import Retailer


def get_retailer():
    cnx = DBConnect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                          FROM go_retailers """
        cursor.execute(query)

        for row in cursor:
            result.append(
                Retailer(row["Retailer_code"],
                             row["Retailer_name"],
                             row["Type"],
                             row["Country"]))

        cursor.close()
        cnx.close()

    return result

