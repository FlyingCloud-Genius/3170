import random
import mysql.connector


LnameList = ["Johnson", "Williams", "Jones", "Brown", "Davis", 
        "Miller", "Wilson", "Moore", "Moore", "Anderson"]
FnameList = ["Jon", "Jack", "Kevin", "Oscar", "Petter", "Quentin", 
        "Emily", "Anna", "Kayla", "Zoe", "Sofia", "Amelia"]
majorList = ["Computer Science and Engineering", "Electronic Information Engineering", 
        "New Energy Science and Engineering", "Mathematics and Applied Mathematics", 
        "Statistics", "Bioinformatics", "Marketing and Communication", 
        "Global Business Studies", "Economics", "Finance", "Professional Accountancy"]
UniList = ["Harvard University", "Stanford University", "University of Cambridge", 
        "Massachusetts Institute of Technology", "University of California, Berkeley", 
        "Princeton University", "University of Oxford", "Columbia University", 
        "California Institute of Technology", "University of Chicago"]

conn = mysql.connector.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
cursor = conn.cursor()


def generate_email():
    email = ""
    for i in range(9):
        email += str(random.randint(0,9))
    email += "@link.cuhk.edu.cn"
    return email

stuList = []

for i in range(100):
    stu_id = str(i).zfill(10)
    stu_fname = FnameList[random.randint(0, len(FnameList)-1)]
    stu_lname = LnameList[random.randint(0, len(LnameList)-1)]
    stu_gender = random.randint(0,2)
    stu_birthday = str(random.randint(1995,2000)) + "-" + str(random.randint(1,12)) + "-" + str(random.randint(1,28))
    stu_major = majorList[random.randint(0,len(majorList)-1)]
    stu_email = generate_email()
    stu_c_uni = UniList[random.randint(0, len(UniList)-1)]
    reg_id = str(i).zfill(10)
    stu = (stu_id, stu_fname, stu_lname, stu_gender, stu_birthday, 
        stu_major, stu_email, stu_c_uni, reg_id)
    stuList.append(stu)
    print(stu)


sql = "INSERT INTO student (stu_id, stu_fname, stu_lname, stu_gender, stu_birthday, \
        stu_mojor, stu_email, stu_c_uni, reg_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
for i in range(len(stuList)):
    val = stuList[i]
    cursor.execute(sql, val)
    conn.commit()