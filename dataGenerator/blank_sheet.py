import mysql.connector

conn = mysql.connector.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
cursor = conn.cursor()

sql = "INSERT INTO blank_sheet (sheet_id) VALUES (%s)"

for i in range(10):
    sheet_id = "5" + str(i).zfill(9)
    cursor.execute(sql % sheet_id)
    conn.commit()
