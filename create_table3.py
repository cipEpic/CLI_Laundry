import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)

cursor = db.cursor()

sql = """CREATE TABLE harga (
  id_harga INT AUTO_INCREMENT PRIMARY KEY,
  jenis VARCHAR(30),
  id_agen INT,
  harga INT
)
"""

cursor.execute(sql)

print("Tabel harga berhasil dibuat!")
