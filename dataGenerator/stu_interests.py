import random
import mysql.connector


interestList = ["running", "swimming", "dancing", "football",
     "basketball", "table tennis", "tennis", "volleyball", 
     "chess", "badminton", "computer game", "listening to music", 
     "watching movie", "painting", "reading fiction", "playing piano", 
     "playing guitar", "travelling"]
stu_interest_list = []

conn = mysql.connector.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
cursor = conn.cursor()

for i in range(100):
    stu_id = str(i).zfill(10)
    interests = random.sample(interestList, random.randint(2,3))
    for i in range(len(interests)):
        stu_interest_pack = (interests[i], stu_id)
        print(stu_interest_pack)
        stu_interest_list.append(stu_interest_pack)

sql = "INSERT INTO stu_interests (stu_interest, stu_id) VALUES (%s, %s)"
for i in range(len(stu_interest_list)):
    val = stu_interest_list[i]
    cursor.execute(sql, val)
    conn.commit()