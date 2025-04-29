from database.DB_connect import DBConnect


def get_anni():
    cnx = DBConnect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT YEAR(s.`Date`) as year 
                       FROM go_daily_sales s
                       ORDER BY year DESC """
        cursor.execute(query)

        for row in cursor:
            result.append(
                row["year"])

        cursor.close()
        cnx.close()

    return result
