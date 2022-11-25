import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)

cursor = db.cursor()
sql = "INSERT INTO transaksi (id_cucian, id_agen, total_bayar) VALUES (%s, %s, %s)"
values = [
    (12, 1, 8000),
    (13, 4, 20000)
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))
