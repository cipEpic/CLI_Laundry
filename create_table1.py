import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)

cursor = db.cursor()
sql = """CREATE TABLE agen (
  id_agen INT AUTO_INCREMENT PRIMARY KEY,
  nama_laundry VARCHAR(30),
  nama_pemilik Varchar(30),
  telp Varchar(15),
  email VARCHAR(15),
  kota VARCHAR(20),
  alamat VARCHAR(100),
  plat_driver VARCHAR(12)
)
"""

cursor.execute(sql)

print("Tabel agen berhasil dibuat!")
