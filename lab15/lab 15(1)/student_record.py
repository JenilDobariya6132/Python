import sqlite3
# Connect to database (or create it)
conn = sqlite3.connect('student_record.db')
# Create a cursor object using the cursor() method
cursor = conn.cursor()
# Create students table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')

# Commit the changes
conn.commit()
# Insert multiple employee records
student_record = [
    (92301733016,'ASHUTOSH KUMAR SINGH','PWP',95),
    (92301733017,'HARSH VISHALBHAI TRIVEDI','PWP',85),
    (92301733027,'VIRAJ PRAKASHBHAI VAGHASIYA','PWP',90),
    (92301733046,'SHIVAM ATULKUMAR BHATT', 'PWP',93),
    (92301733058,'DEVENDRASINH DOLATSINH JADEJA','PWP',75)
]
# Using executemany to insert multiple records
cursor.executemany('''INSERT INTO student_record (Enrollment, name, subject,Mark) 
                      VALUES (?, ?, ?,?)''', student_record)

# Commit the changes
conn.commit()
