from mysql import connector

def Connect_to_server():
    try:
        ser = connector.connect(
            host="localhost",
            user="root",           # Enter mysql Username
            passwd="Example@01",   # Enter mysql password
        )
        return ser
    except:
        print("Error while connecting to MYSQL server")

def Connect_to_DB():
    mydb = connector.connect(
                host="localhost",
                user="root",
                passwd="Example@01",
                database="webscraping"
            )

    return mydb

def Create_DB():
    ser = Connect_to_server()
    server = ser.cursor()
    server.execute("SHOW DATABASES")
    if (('webscraping',) in [i for i in server]):
        print("Database is already exits")
        Create_table()
    else:
        server.execute("CREATE DATABASE webscraping")
        print("Database has been created successfully.")
        Create_table()

def Create_table():
    mydb = Connect_to_DB()
    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE TABLE errors ( \
                        id INT AUTO_INCREMENT PRIMARY KEY, \
                        device VARCHAR(255),  \
                        inv_name VARCHAR(255), \
                        alarm VARCHAR(255), \
                        o_date DATETIME, \
                        c_date DATETIME, \
                        msg VARCHAR(255) \
                    )")

        print("Table has been created succesfully.")
    except:
        print("Table 'errors' already exists")

def Insert_into_table(value):
    mydb = Connect_to_DB()
    mycursor = mydb.cursor()
    sql = "INSERT INTO errors (device, inv_name, alarm, o_date, c_date, msg) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sql, value)

    mydb.commit()

def Fetch_data(name):
    mydb = Connect_to_DB()
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM {name}")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

Create_DB()