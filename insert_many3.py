import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)

cursor = db.cursor()
sql = "INSERT INTO harga (jenis, id_agen, harga) VALUES (%s, %s, %s)"
values = [
    ('cuci', 1, 4000),
    ('setrika', 1, 3000),
    ('komplit', 1, 6500),
    ('cuci', 2, 5500),
    ('setrika', 2, 4000),
    ('komplit', 2, 8000),
    ('cuci', 3, 3500),
    ('setrika', 3, 3500),
    ('komplit', 3, 6500),
    ('cuci', 4, 3000),
    ('setrika', 4, 2500),
    ('komplit', 4, 5000)
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))
