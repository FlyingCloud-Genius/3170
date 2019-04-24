import pymysql
import random

def data_generator():
    conn = pymysql.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
    
    cursor = conn.cursor()

    current_id = 7000000000
    first_name = ["Johnson", "Williams", "Jones", "Brown", "Davis", 
    "Miller", "Wilson", "Moore", "Moore", "Anderson", "Mike", "Emily", "Ben", "Chandler", "Pheeby"]

    last_name = ["Jon", "Jack", "Kevin", "Oscar", "Petter", "Quentin", 
    "Emily", "Anna", "Kayla", "Zoe", "Sofia", "Amelia", "Yang", "William", "Bing", "Green", "Tribiony"]

    for i in range(10):
        email = random.randint(10000000, 99999999)
        random_phone = random.randint(18600000000, 18699999999)
        randomFName = random.randint(0, len(first_name) - 1)
        randomLName = random.randint(0, len(last_name) - 1)
        effect_row = cursor.execute('insert into guardian values("{}", "{}", "{}", "{}", "{}");'.format(str(current_id), str(email)+"@gmail.com", first_name[randomFName], last_name[randomLName], str(random_phone)))
        current_id += 1
        
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    data_generator()   
