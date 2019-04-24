import random
import mysql.connector

majorList = ["Computer Science and Engineering", "Electronic Information Engineering", 
        "New Energy Science and Engineering", "Mathematics and Applied Mathematics", 
        "Statistics", "Bioinformatics", "Marketing and Communication", 
        "Global Business Studies", "Economics", "Finance", "Professional Accountancy"]

uni_major_list = []

conn = mysql.connector.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
cursor = conn.cursor()


for i in range(10):
    university = "1" + str(i).zfill(9)
    open_majors = random.sample(majorList, 4)
    for i in range(len(open_majors)):
        open_major = open_majors[i]
        enrollment = random.randint(0, 50)
        uni_major_pack = (open_major, university, enrollment)
        print(uni_major_pack)
        uni_major_list.append(uni_major_pack)


sql = "INSERT INTO uni_open_major (open_major, uni_id, enrollment) VALUES (%s, %s, %s)"
for i in range(len(uni_major_list)):
    val = uni_major_list[i]
    cursor.execute(sql, val)
    conn.commit()