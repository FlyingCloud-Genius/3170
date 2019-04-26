import pymysql

def buildDB():
    conn = pymysql.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
    cursor = conn.cursor()

    cursor.execute("use orderFactDB;")

    sql = ['create table product(PID char(2), PName varchar(20), PType varchar(10), PSupplierName varchar(20), primary key (PID));',
    
    'create table customer(CID char(2), CName varchar(20), CType varchar(20), CZip int, primary key (CID));',
    
    'create table depot(depotID char(2), depotSize varchar(10), depotZip int, primary key (depotID));',
    
    'create table orderClerk(OCID char(3), OCName varchar(10), OCTitle varchar(20), OCEducationLevel varchar(20), OCYearOfHire int, primary key (OCID));',
    
    'create table orderFact(OCID char(3), CID char(2), depotID char(2), PID char(2), orderDate date, orderTime time, quantity int, primary key (CID, PID), foreign key (PID) references product(PID), foreign key (CID) references customer(CID), foreign key (OCID) references orderClerk(OCID), foreign key (depotID) references depot(depotID));']

    for i in sql:
        cursor.execute(i)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    buildDB()