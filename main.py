import sqlite3
import os
dbname = '{0}/dbsqlite.db'.format(os.path.dirname(__file__)) # Sqlite database name, including path

# Connect to database, and returns the database and cursor objects
def connect(dbname):
    db = sqlite3.connect(dbname)  # Connect to database
    cursor = db.cursor()
    return db,cursor


def displayContent(cursor):
    for row in cursor.fetchall():
        print(' '.join(str(i) for i in row))  # Display elements in row
    cursor.close()


# All restaurants
def listAllRestaurants():
    global dbname
    try:
        db,cursor = connect(dbname)
        # Use all the SQL you like
        cursor.execute("SELECT * FROM Restaurant;")

        # Display all data
        displayContent(cursor)

        db.close()


    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# All restaurants in NY
def listAllRestaurantsNY():
    global dbname
    try:
        db, cursor = connect(dbname)
        # Use all the SQL you like
        cursor.execute("SELECT * FROM Restaurant where city = 'NY';")

        # Display
        displayContent(cursor)
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# Names and addresses for customers living in NY, by customer name
def listAllRestaurantsNYByName():
    try:
        db, cursor = connect(dbname)

        # Use all the SQL you like
        cursor.execute("SELECT customerName,customerCity FROM customer WHERE customerCity LIKE '%NY%' ORDER BY customerName;")

        # Display
        displayContent(cursor)
        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# Average price of Tables
def averagePriceTables():
    global dbname
    try:
        db, cursor = connect(dbname)
        # Use all the SQL you like
        cursor.execute("SELECT restaurantId, AVG(price) AS AvgPrice FROM Tables GROUP BY restaurantId;")

        # Display
        displayContent(cursor)

        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# List the price and type of all Tables at the GrosveIdr restaurant
def priceTypeGrosveIdr():
    global dbname

    try:
        db, cursor = connect(dbname)

        # Use all the SQL you like
        cursor.execute("SELECT price, type FROM Table WHERE restaurantId IN (SELECT restaurantId FROM restaurant WHERE hotenName = 'GrosveIdr');")

        # Display
        displayContent(cursor)

        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# What is the total income from bookings for the Pepe restaurant today?
def incomePeterToday():
    global dbname

    try:
        db, cursor = connect(dbname)

        # Use all the SQL you like
        cursor.execute("SELECT SUM(price) asTotalIncome FROM Tables WHERE tableId IN (SELECT tableId FROM Booking WHERE"+
                       " restaurantId IN " +
                        "(SELECT restaurantId FROM Restaurant WHERE restaurantName=\"Peter\'s\"));")

        # Display
        displayContent(cursor)

        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))

# List the number of Tables in each restaurant in NY
def numberTablesNY():
    global dbname

    try:
        db, cursor = connect(dbname)

        # Use all the SQL you like
        cursor.execute("SELECT r.restaurantId, COUNT(tableId) AS count FROM Tables r, Restaurant h WHERE r.restaurantId = h.restaurantId AND city = 'NY' GROUP BY r.restaurantId;")

        # Display
        displayContent(cursor)

        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))


# What is the most commonly booked Table type for each restaurant in NY?
def commonTableNY():
    global dbname

    try:
        db, cursor = connect(dbname)

        # Use all the SQL you like
        cursor.execute("SELECT type as MostlyBooked,max(CNT)as Idoftimesbooked FROM (Select Type, count(Type) as CNT " +
                        "FROM Booking b, restaurant h, Tables r " +
                        "where r.TableId=b.tableId and b.restaurantId=h.restaurantId and h.city like '%NY%' " +
                        "group by type) as T group by type;")

        # Display
        displayContent(cursor)

        db.close()
    except sqlite3.Error as e:
        print ('Connection failed with error code ' + str(e.args[0]) + " " + str(e.args[1]))



print ( " All restaurants")
listAllRestaurants()
print ( " All restaurants in NY")
listAllRestaurantsNY()
print ( " Names and addresses for customers living in NY, by customer name")
listAllRestaurantsNYByName()
print ( " Average price of Tables")
averagePriceTables()
print ( "------- What is the total income from bookings for the 'Peter' restaurant today?")
incomePeterToday()
print ( "List the number of Tables in each restaurant in NY")
numberTablesNY()
print ( "Most common Table type in NY")
commonTableNY()


