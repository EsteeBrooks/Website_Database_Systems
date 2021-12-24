import mysql.connector
import re
from mysql.connector import FieldType

def create_entity(cursor, table, values):
   
   if len(values) == 1:
      values = "(" + str(values) + ")"
      
   query = "insert into " + table + " values " + str(values) + ";"
   print("Query:", query)
      
   # Executing the query
   # Checking for errors (perhaps due to foreign key / referential integrity constraints)
   # Reporting that error back to the user
   try:
      cursor.execute(query)
   except mysql.connector.Error as e:
      print("Error interacting with mySQL", e, '\n')
      return -1
    
   # Determining the success or failure of the operation
   # Closing or disconnecting the connection
   # return key_val
   
def update_entity(cursor, table, values, condition):
   set_statement = ""
   count = 1
   for v in values:
      set_statement += str(v) + "='" + str(values[v]) + "'"
      # add a comma in case there are multiple values to update
      if count < len(values):
         set_statement += ","
      count += 1
      
   query = "update " + table + " set " + set_statement + " where " + str(condition[0]) + str(condition[1]) + str(condition[2]) + ";"

   print("Query:", query)
   # Executing the query
   # Checking for errors (perhaps due to foreign key / referential integrity constraints)
   # Reporting that error back to the user
   try:
      cursor.execute(query)
   except mysql.connector.Error as e:
      print("Error interacting with mySQL", e, '\n')
      return -1
   # Determining the success or failure of the operation
   # Closing or disconnecting the connection
   # return key_val
   
def delete_entity(cursor, table, key_col, key_val):
   # Creating a SQL query to delete the specified row from the table, which requires the name of the table, the name of the key column (typically - but not necessarily - the primary key), and the value(s) of that column (typically some kind of id) for which we wish to delete the record
   query = "delete from " + table + " where " + str(key_col) + " = '" + str(key_val) + "'"
   # query = "delete from student where ID = 2468"
   print("Query:", query)
   
   # Executing the query
   # Checking for errors (perhaps due to foreign key / referential integrity constraints)
   # Reporting that error back to the user
   try:
      cursor.execute(query)
   except mysql.connector.Error as e:
      print("Error interacting with mySQL", e, '\n')
      return -1
   # Determining the success or failure of the operation
   # Closing or disconnecting the connection
   # return key_val


def count_entity(cursor, table):
   query = "select * from " + table
   print("Query:", query)
   try:
      cursor.execute(query)
      rows = cursor.fetchall()
      print("Rows in result:", cursor.rowcount)  # Executing the query
      for row in rows:
         for elem in row:
            print("%-15s" % format(str(elem)), end="")
            print()
   except mysql.connector.Error as e:
      print("Error interacting with mySQL", e, '\n')

def delete_politician(cursor, student_ID):
   return delete_entity(cursor, "student", "ID", student_ID)


def main():
   # create connection in main:
   conn = mysql.connector.connect(host="localhost", user="root", passwd="Lokshon1!", database="ISGOV3")
   cursor = conn.cursor()

   # good test code:
   '''
   count_entity(cursor, "student")
   delete_student(cursor, "2468")
   conn.commit()
   count_entity(cursor, "student")
   create_entity(cursor, "student", (90000, "Johnson", "History", 0, 7))
   count_entity(cursor, "student")
   update_entity(cursor, "student", {"dept_name": "Comp. Sci.", "tot_cred": 5}, ("ID", "=", 23121))
   count_entity(cursor, "student")
   '''
   count_entity(cursor, "position")
   #delete_entity(cursor, "position", "position_id", 5)
   #count_entity(cursor, "position")
   create_entity(cursor, "position", ("Far-right"))
   count_entity(cursor, "position")
   conn.close()


main()
