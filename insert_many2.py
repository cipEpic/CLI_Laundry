import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)

cursor = db.cursor()
sql = "INSERT INTO cucian (id_agen, jenis, berat) VALUES (%s, %s, %s)"
values = [
    (3, 'komplit', 3),
    (1, 'setrika', 1),
    (1, 'cuci', 2),
    (4, 'komplit', 4)
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))
