import sqlite

#make a connection
conn = sqlite.connect('cannabis_data.db')

# make a cursor
curs = conn.cursor()

# create a table
#create_table = """
#CREATE TABLE cannabis (
#    Strain string,
#    Type string,
#    Rating float,
#    Description string,
#    flavors string,
#    positive string,
#    negative string,
#    medical string
#);
#"""

#create a function to query data
#def q_all(query):
#    curs = conn.cursor()
#    curs.execute(query)
#    rows = curs.fetchall()
#    curs.close()
#    return rows

#Create the table via function
