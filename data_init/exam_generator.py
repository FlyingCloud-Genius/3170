import pymysql
import random

def data_generator():
    conn = pymysql.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
    
    cursor = conn.cursor()

    current_id = 8000000000

    location = ["Shenzhen", "Hong Kong", "Shanghai", "Los Angeles", "Singapore", "Kuala Lumpur", "Tokyo", "Beijing", "London", "Berlin", "New York", "Seattle", "Wuhan", "Seoul", "New Delhi"]

    for i in range(100):
        email = random.randint(10000000, 99999999)
        random_phone = random.randint(18600000000, 18699999999)
        random_dateTime = getRandomDateTime()
        random_location = random.randint(0, len(location) - 1)
        effect_row = cursor.execute('insert into GRE_exam values("{}", "{}", "{}");'.format(str(current_id), location[random_location], random_dateTime))
        current_id += 1
        
    conn.commit()
    cursor.close()
    conn.close()


def getRandomDateTime():
    randomYear = random.randint(2018, 2022)
    randomMonth = random.randint(1, 12)
    randomDay = random.randint(1, 28)
    randomHour = random.randint(8, 16)
    randomDateTime = str(randomYear) + "-" + str(randomMonth) + "-" + str(randomDay) + " " + str(randomHour) + ":00:00"
    return randomDateTime

if __name__ == "__main__":
    data_generator()   
