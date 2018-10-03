import sqlite3
import os
dbname = '{0}/dbsqlite.db'.format(os.path.dirname(__file__)) # Sqlite database name, including path

#6.7 All restaurants
def listAllrestaurants():
    global dbname
    try:
        db = sqlite3.connect(dbname)  # Connect everytime

        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("SELECT * FROM Restaurant;")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row) )        #Display elements in row
        cursor.close()
        db.close()

    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

#6.8 All restaurants in NY
def listAllrestaurantsNY():
    global dbname
    try:
        db = sqlite3.connect(dbname)  # Connect everytime
        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("SELECT * FROM Restaurant where city = 'NY';")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row))
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

#6.9 Names and addresses for customers living in NY, by customer name
def listAllrestaurantsNYByName():
    try:
        db = sqlite3.connect(dbname)  # Connect everytime
        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("SELECT customerName,customerCity FROM customer WHERE customerCity LIKE '%NY%' ORDER BY customerName;")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row))
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# 6.13 Average price of Tables
def averagePriceTables():
    global dbname
    try:
        db = sqlite3.connect(dbname)  # Connect everytime
        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("SELECT restaurantId, AVG(price) AS AvgPrice FROM Tables GROUP BY restaurantId;")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row))
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# 6.16 List the price and type of all Tables at the GrosveIdr restaurant
def priceTypeGrosveIdr():
    global dbname

    try:
        db = sqlite3.connect(dbname)             # Connect everytime
        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("SELECT price, type FROM Table WHERE restaurantId IN (SELECT restaurantId FROM restaurant WHERE hotenName = 'GrosveIdr');")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row))
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# 6.19 What is the total income from bookings for the Pepe restaurant today?
def incomeGrosveIdrToday():
    global dbname

    try:
        db = sqlite3.connect(dbname)  # Connect everytime
        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("SELECT SUM(price) asTotalIncome FROM Tables WHERE TableId IN (SELECT tableId FROM Booking WHERE"+
                       " dateStart = '2016-11-11' and restaurantId IN " +
                        "(SELECT restaurantId FROM Restaurant WHERE restaurantName='Pepe'));")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row))
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

#6.23	List the number of Tables in each restaurant in NY
def numberTablesNY():
    global dbname

    try:
        db = sqlite3.connect(dbname)  # Connect everytime
        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("SELECT r.restaurantId, COUNT(tableId) AS count FROM Tables r, Restaurant h WHERE r.restaurantId = h.restaurantId AND city = 'NY' GROUP BY r.restaurantId;")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row))
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))


#6.25	What is the most commonly booked Table type for each restaurant in NY?
def commonTableNY():
    global dbname

    try:
        db = sqlite3.connect(dbname)  # Connect everytime
        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("SELECT type as MostlyBooked,max(CNT)as Idoftimesbooked FROM (Select Type, count(Type) as CNT " +
                        "FROM Booking b, restaurant h, Tables r " +
                        "where r.TableId=b.tableId and b.restaurantId=h.restaurantId and h.city like '%NY%' " +
                        "group by type) as T group by type;")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row))
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))


#6.28	Update the price of all Tables by 5%.
def updatePrice():
    global dbname

    try:
        db = sqlite3.connect(dbname)  # Connect everytime
        cursor = db.cursor()
        # Use all the SQL you like
        cursor.execute("Update Tables Set Price = price*1.05;")

        # print ( all the first cell of all the rows
        for row in cursor.fetchall():
            print ( ' '.join(str(i) for i in row))
        cursor.close()
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))





print ( " All restaurants")
listAllrestaurants()
print ( " All restaurants in NY")
listAllrestaurantsNY()
print ( " Names and addresses for customers living in NY, by customer name")
listAllrestaurantsNYByName()
print ( " Average price of Tables")
averagePriceTables()
print ( "------- What is the total income from bookings for the 'Pepe' restaurant today?")
incomeGrosveIdrToday()
print ( "List the number of Tables in each restaurant in NY")
numberTablesNY()
print ( "Most common Table type in NY")
commonTableNY()
print ( "Update prices by 5%")
updatePrice()

