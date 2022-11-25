import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)

cursor = db.cursor()

sql = """CREATE TABLE cucian (
  id_cucian INT AUTO_INCREMENT PRIMARY KEY,
  id_agen INT,
  jenis Varchar(15),
  berat DOUBLE
)
"""

cursor.execute(sql)

print("Tabel cucian berhasil dibuat!")
