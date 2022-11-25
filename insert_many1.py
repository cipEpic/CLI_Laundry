import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)

cursor = db.cursor()
sql = "INSERT INTO agen (nama_laundry, nama_pemilik, telp, email, kota, alamat, plat_driver) VALUES (%s, %s, %s, %s, %s, %s, %s)"
values = [
    ('laundry satu', 'pemilik1', '081231231231', 'laundry1@gmail.com',
     'Klungkung', 'Jalan Krisna No. 3 Depan Banjar Papaan', 'DK 1215 NA'),
    ('laundry dua', 'pemilik2', '081223334444', 'laundry2@gmail.com',
     'Denpasar', 'Jalan Danau Meninjau nomor 3', 'DK 1234 NA'),
    ('laundry tiga ', 'pemilik3', '081231098239', 'laundry3@gmail.com',
     'Singaraja', 'Jalan Sudirman nomor 4', 'DK 1111 NA'),
    ('laundry empat', 'pemilik4', '081231098239', 'laundry4@gmail.com',
     'Karangasem', 'Jalan gunung agung nomor 3', 'DK 1246 NA')
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))
