import pymysql
import random

def data_generator():
    conn = pymysql.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
    cursor = conn.cursor()

    list1 = []
    list2 = []

    for i in range(500):
        current_guardian_id = random.randint(7000000000, 7000000009)
        current_exam_id = random.randint(8000000000, 8000000099)
        if addNewConnection(list1, list2, current_guardian_id, current_exam_id):
            list1.append(current_guardian_id)
            list2.append(current_exam_id)
        else:
            continue
        effect_row = cursor.execute('insert into guard values("{}", "{}");'.format(str(current_guardian_id), str(current_exam_id)))

        
    conn.commit()
    cursor.close()
    conn.close()

def addNewConnection(list1, list2, current_guardian_id, current_exam_id):
    for index in range(len(list1)):
            if list1[index] == current_guardian_id and list2[index] == current_exam_id:
                return False
    return True

if __name__ == "__main__":
    data_generator()   
