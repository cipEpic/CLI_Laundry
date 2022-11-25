import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)

cursor = db.cursor()

sql = """CREATE TABLE transaksi (
  kode_transaksi INT AUTO_INCREMENT PRIMARY KEY,
  id_cucian INT,
  id_agen INT,
  total_bayar INT
)
"""

cursor.execute(sql)

print("Tabel transaksi berhasil dibuat!")
