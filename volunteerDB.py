import sqlite3

conn = sqlite3.connect("volunteers.db")

crsr = conn.cursor()

conn.execute('''
             CREATE TABLE IF NOT EXISTS volunteers (
                 TelegramID INTEGER PRIMARY KEY,
                 FullName TEXT,
                 University TEXT,
                 Faculty TEXT
             )''')

conn.commit()

crsr.execute("INSERT INTO volunteers VALUES (35635245, 'Быков Данил Игоревич','СПбГЭТУ \"ЛЭТИ\"','ФКТИ')")

conn.commit()

conn.close()