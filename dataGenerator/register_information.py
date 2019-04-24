import random
import mysql.connector

# def create_student_name():
#     LnameList = ["Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Moore", "Anderson"]
#     FnameList = ["Jon", "Jack", "Kevin", "Oscar", "Petter", "Quentin", "Emily", "Anna", "Kayla", "Zoe", "Sofia", "Amelia"]
#     name = FnameList[random.randint(0,len(FnameList))-1] + " " + LnameList[random.randint(0,len(LnameList))-1]
#     return name

conn = mysql.connector.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")

cursor = conn.cursor()

regList = []
# UniList = ["Harvard University", "Stanford University", "University of Cambridge", "Massachusetts Institute of Technology", "University of California, Berkeley", "Princeton University", "University of Oxford", "Columbia University", "California Institute of Technology", "University of Chicago"]

for i in range(100):
    reg_id = str(i).zfill(10)
    reg_password = str(random.randint(0, 100000000)*2**random.randint(0,20))
    # reg_name = create_student_name()
    reg = (reg_id, reg_password)
    regList.append(reg)

for i in range(10):
    reg_id = "1" + str(i).zfill(9)
    reg_password = str(random.randint(0, 100000000)*2**random.randint(0,20))
    # reg_name = UniList[i]
    reg = (reg_id, reg_password)
    regList.append(reg)

sql = "INSERT INTO reg_info (reg_id, reg_password) VALUES (%s, %s)"
for i in range(len(regList)):
    val = regList[i]
    cursor.execute(sql, val)
    conn.commit()
    
