import random
import mysql.connector

attendanceList = []

conn = mysql.connector.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
cursor = conn.cursor()

for i in range(100):
    exam_id = "8" + str(i).zfill(9)
    students = random.sample(range(100), random.randint(1,5))
    for j in range(len(students)):
        stu_id = str(students[j]).zfill(10)
        attendance = (stu_id, exam_id)
        print(attendance)
        attendanceList.append(attendance)

sql = "INSERT INTO attendance (stu_id, exam_id) VALUES (%s, %s)"
for i in range(len(attendanceList)):
    val = attendanceList[i]
    cursor.execute(sql, val)
    conn.commit()
    