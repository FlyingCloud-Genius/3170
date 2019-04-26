import pymysql

def buildDB():
    conn = pymysql.connect(host = "120.78.82.130", port = 3306, user = "root", passwd = "cuhksz", db = "AES", charset = "utf8")
    cursor = conn.cursor()

    cursor.execute("use assignment;")

    sql = ["create table humanResource(EmployeeID char(3) not null, Name varchar(10), Title varchar(20), EducationLevel varchar(20), YearOfHire int, primary key (EmployeeID));",
    'insert into humanResource values("OC1", "Antonio", "Order Clerk", "High School", 2001);',
    'insert into humanResource values("OC2", "Wesley", "Order Clerk", "College", 2005);',
    'insert into humanResource values("OC3", "Lilly", "Order Clerk", "College", 2005);',
    
    "create table supplier(supplierID char(2) not null, supplierName varchar(20), primary key (supplierID));",
    'insert into supplier values("ST", "Super Tires");',
    'insert into supplier values("BE", "Batteries Etc");',

    'create table product(productID char(2) not null, productName varchar(20), productType varchar(10), supplierID char(2), primary key (productID), foreign key (supplierID) references supplier(supplierID));',
    'insert into product values("P1", "BigGripper", "Tire", "ST");',
    'insert into product values("P2", "TractionWiz", "Tire", "ST");',
    'insert into product values("P3", "SureStart", "Battery", "BE");',
    
    'create table depot(depotID char(2) not null, depotSize varchar(10), depotZip int, primary key (depotID));',
    'insert into depot values("D1", "Small", 60611);',
    'insert into depot values("D2", "Large", 60660);',
    'insert into depot values("D3", "Large", 60611);',

    'create table orderClerk(OCID char(3) not null, OCName varchar(10), primary key (OCID));',
    'insert into orderClerk values("OC1", "Tony");',
    'insert into orderClerk values("OC2", "Wesley");',
    'insert into orderClerk values("OC3", "Lily");',

    'create table customer(customerID char(2) not null, customerName varchar(20), customerType varchar(20), customerZip int, primary key (customerID));',
    'insert into customer values("C1", "Auto Doc", "Repair Shop", 60137);',
    'insert into customer values("C2", "Bo\'s car Repart", "Repair Shop", 60140);',
    'insert into customer values("C3", "JJ Auto Parts", "Reriailer", 60605);',

    'create table orderTable(orderID char(2) not null, customerID char(2), depotID char(2), OCID char(3), orderDate date, orderTime time, primary key (orderID), foreign key (customerID) references customer(customerID), foreign key (depotID) references depot(depotID), foreign key (OCID) references orderClerk(OCID));',
    'insert into orderTable values("O1", "C1", "D1", "OC1", "2013-1-1", "09:00:00");',
    'insert into orderTable values("O2", "C2", "D1", "OC2", "2013-1-2", "09:00:00");',
    'insert into orderTable values("O3", "C3", "D2", "OC3", "2013-1-2", "09:30:00");',
    'insert into orderTable values("O4", "C1", "D2", "OC1", "2013-1-3", "09:00:00");',
    'insert into orderTable values("O5", "C2", "D3", "OC2", "2013-1-3", "09:15:00");',
    'insert into orderTable values("O6", "C3", "D3", "OC3", "2013-1-3", "09:30:00");',
    'insert into orderTable values("O7", "C1", "D2", "OC3", "2013-1-3", "09:45:00");',
    'insert into orderTable values("O8", "C1", "D2", "OC3", "2013-1-3", "09:45:00");',

    'create table orderVia(productID char(2), orderID char(2), quantity int, primary key (productID, orderID), foreign key (productID) references product(productID), foreign key (orderID) references orderTable(orderID));',
    'insert into orderVia values("P1", "O1", 4);',
    'insert into orderVia values("P2", "O1", 8);',
    'insert into orderVia values("P1", "O2", 12);',
    'insert into orderVia values("P2", "O3", 4);',
    'insert into orderVia values("P3", "O4", 7);',
    'insert into orderVia values("P3", "O5", 5);',
    'insert into orderVia values("P2", "O6", 8);',
    'insert into orderVia values("P1", "O6", 4);',
    'insert into orderVia values("P1", "O7", 6);',
    'insert into orderVia values("P2", "O7", 6);',
    'insert into orderVia values("P1", "O8", 6);',
    'insert into orderVia values("P2", "O8", 6);']

    for i in sql:
        cursor.execute(i)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    buildDB()