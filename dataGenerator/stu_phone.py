import random
import mysql.connector

phoneList = []


conn = mysql.connector.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
cursor = conn.cursor()

for i in range(200):
    if i<100:
        stu_id = str(i).zfill(10)
    else:
        stu_id = str(random.randint(0,99)).zfill(10)
    stu_phone = str(random.randint(10000000000,19999999999))
    stu_phone_pack = (stu_phone, stu_id)
    print(stu_phone_pack)
    phoneList.append(stu_phone_pack)

sql = "INSERT INTO stu_phones (stu_phone, stu_id) VALUES (%s, %s)"
for i in range(len(phoneList)):
    val = phoneList[i]
    cursor.execute(sql, val)
    conn.commit()