import csv
from cs50 import SQL
open("Flight_Booking.db", "w").close()
db=SQL("sqlite:///Flight_Booking.db")
db.execute("CREATE TABLE names(id INTEGER, person_name TEXT,username TEXT, phone_number INTEGER, departure_airport TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE airline(id INTEGER , airline_name TEXT, travel_class TEXT,passengers_number INTEGER, PRIMARY KEY(id))")
db.execute("CREATE TABLE arrival_airport(id INTEGER , airport_name TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE names_airline(names_id INTEGER, airline_id TEXT, FOREIGN KEY(names_id) REFERENCES names(id) FOREIGN KEY(airline_id) REFERENCES airline(id))")
db.execute("CREATE TABLE names_airport(names_id INTEGER, airport_id INTEGER, FOREIGN KEY(names_id) REFERENCES names(id), FOREIGN KEY (airport_id) REFERENCES arrival_airport(id))")
db.execute("CREATE TABLE airline_airport(airline_id INTEGER, airport_id INTEGER, FOREIGN KEY(airline_id) REFERENCES airline(id),FOREIGN KEY (airport_id) REFERENCES arrival_airport(id))")
 
with open("Flight Booking.csv","r") as booking:
    reader=csv.DictReader(booking)

    for row in reader:
        user_name = row["Username"]
        name = row["Names"]
        phone = row["Phone Number"]
        departure = row["Departure Airport"]
        arrival = row["Arrival Airport"]
        preference = row["Preferred Airline"]
        num = row["Number Of Passengers"]
        travel = row["Travel Class"]

        db.execute("INSERT INTO names(person_name,username,phone_number,departure_airport) VALUES(?,?,?,?);",name, user_name,phone,departure)
        db.execute("INSERT INTO airline(airline_name,travel_class,passengers_number) VALUES(?,?,?);",preference,travel,num)
        db.execute("INSERT INTO arrival_airport(airport_name) VALUES(?);",arrival)

        db.execute("INSERT INTO names_airline(names_id,airline_id) VALUES((SELECT id FROM names WHERE username = ?),(SELECT id FROM airline WHERE airline_name=?));", user_name,preference)
        db.execute("INSERT INTO names_airport(names_id, airport_id) VALUES((SELECT id FROM names WHERE username=?),(SELECT id FROM arrival_airport WHERE airport_name=?));",user_name,arrival)
        db.execute("INSERT INTO airline_airport(airline_id,airport_id) VALUES((SELECT id FROM airline WHERE airline_name=?),(SELECT id FROM arrival_airport WHERE airport_name=?));",preference,arrival)




