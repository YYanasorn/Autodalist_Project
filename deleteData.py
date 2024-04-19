import sqlite3
import time

# Connect to the SQLite database
conn = sqlite3.connect('mysite/db.sqlite3')
c = conn.cursor()

try:
    # Start a transaction
    c.execute('BEGIN TRANSACTION')

    # Delete existing data
    c.execute('DELETE FROM app_parameter')

    # Commit the delete operation
    conn.commit()
except sqlite3.Error as e:
    # Roll back the transaction if an error occurs
    conn.rollback()
    print("Error:", e)
finally:
    # Close the connection
    conn.close()
