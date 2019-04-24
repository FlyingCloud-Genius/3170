import random
import mysql.connector

emailList = ["admissions@harvard.edu.us", "admissions@stanford.edu.cn", 
        "admissions@cambridge.edu.uk", "admissions@mit.edu.us", "admissions@ucb.edu.us", 
        "admissions@princeton.edu.us", "admissions@oxford.edu.uk", 
        "admissions@columbia.edu.us", "admissions@cit.edu.us", 
        "admissions@chicago.edu.us"]

UniList = ["Harvard University", "Stanford University", 
        "University of Cambridge", "Massachusetts Institute of Technology", 
        "University of California, Berkeley", "Princeton University", 
        "University of Oxford", "Columbia University", 
        "California Institute of Technology", "University of Chicago"]

addressList = ["Massachusetts Hall Cambridge, MA 02138", "Stanford University, 450 Serra Mall Stanford, CA 94305–2004", 
            "The Old Schools, Cambridge CB2 1TN, UK", "Director of Adimissions, Massachusetts Institute of Technology, \
            77 Massachusetts Avenue, Cambridge, MA02139, USA", "University of California Undergraduate Application \
            Processing Service P.O. Box 4010 Concord CA 94524-4010 USA", "Princeton University, Princeton, NJ 08544", 
            "Oxford University Press Great Clarendon Street Oxford OX2 6DP", "2960 Broadway, New York, NY 10027-69021200 \
            E California Blvd Pasadena.CA 91125", "116th and Broadway, New York, NY 10027, 212-854-1754", "The University \
            of Chicago, Edward H. Levi Hall, 5801 South Ellis Avenue, Chicago, Illinois 60637"]

uni_list = []
conn = mysql.connector.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
cursor = conn.cursor()

for i in range(10):
    uni_id = "1" + str(i).zfill(9)
    uni_email = emailList[i]
    uni_name = UniList[i]
    uni_phone = random.randint(10000000000,19999999999)
    uni_address = addressList[i]
    reg_id = "1" + str(i).zfill(9)
    required_GRE_score = random.choice([320,325,330])
    uni = (uni_id, uni_email, uni_name, uni_phone, 
        uni_address, reg_id, required_GRE_score)
    print(uni)
    uni_list.append(uni)

sql = "INSERT INTO university (uni_id, uni_email, uni_name, uni_phone, \
        uni_address, reg_id, required_GRE_score) VALUES (%s, %s, %s, %s, %s, %s, %s)"
for i in range(len(uni_list)):
    val = uni_list[i]
    cursor.execute(sql, val)
    conn.commit()