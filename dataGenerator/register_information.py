import random

def create_name(i):
    length = random.randint(5,i)
    name = ""
    for j in range(length):
        name += chr(random.randint(65, 90) + random.randint(0,1)*32)
    return name

for i in range(100):
    reg_id = str(i).zfill(10)
    reg_password = str(random.randint(0, 100000000)*2**random.randint(0,20))
    reg_name = create_name(30)
    print(reg_name)

