cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')

# Commit the changes
conn.commit()