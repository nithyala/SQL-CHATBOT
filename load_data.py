import mysql.connector

# --- Fill in your Aiven details ---
conn = mysql.connector.connect(
    host="mysql-9ae36-sqll.i.aivencloud.com",
    port=25738,
    user="avnadmin",
    password="PASTE_YOUR_AIVEN_PASSWORD_HERE",
    database="defaultdb",
    ssl_disabled=False,          # Aiven requires SSL
)

cur = conn.cursor()

# Recreate the table cleanly
cur.execute("DROP TABLE IF EXISTS STUDENT")
cur.execute(
    "CREATE TABLE STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)"
)

rows = [
    ("Krish", "Data Science", "A", 90),
    ("John", "Data Science", "B", 100),
    ("Mukesh", "Data Science", "A", 86),
    ("Jacob", "DEVOPS", "A", 50),
    ("Dipesh", "DEVOPS", "A", 35),
]
cur.executemany("INSERT INTO STUDENT VALUES (%s, %s, %s, %s)", rows)
conn.commit()

# Verify
cur.execute("SELECT * FROM STUDENT")
for r in cur.fetchall():
    print(r)

cur.close()
conn.close()
print("Done. Data loaded into Aiven.")
