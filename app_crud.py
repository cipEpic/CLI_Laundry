import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="laundryku"
)


def insert_agen(db):
    nama_laundry = input("Masukan nama laundry: ")
    nama_pemilik = input("Masukan nama pemilik: ")
    telp = input("Masukan nomer telepon: ")
    email = input("Masukan email: ")
    kota = input("Masukan kota: ")
    alamat = input("Masukan alamat: ")
    plat_driver = input("Masukan nomer plat driver: ")

    val = (nama_laundry, nama_pemilik, telp, email, kota, alamat, plat_driver)
    cursor = db.cursor()
    sql = "INSERT INTO agen (nama_laundry, nama_pemilik, telp, email, kota, alamat, plat_driver) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

    # 1cuci
    jenis = input("Masukan jenis: ")
    id_agen = input("Masukan id agen: ")
    harga = input("harga: ")

    val = (jenis, id_agen, harga)
    cursor = db.cursor()
    sql = "INSERT INTO harga (jenis, id_agen, harga) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

    # setrika
    jenis = input("Masukan jenis: ")
    id_agen = input("Masukan id agen: ")
    harga = input("harga: ")

    val = (jenis, id_agen, harga)
    cursor = db.cursor()
    sql = "INSERT INTO harga (jenis, id_agen, harga) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

    # komplit
    jenis = input("Masukan jenis: ")
    id_agen = input("Masukan id agen: ")
    harga = input("harga: ")

    val = (jenis, id_agen, harga)
    cursor = db.cursor()
    sql = "INSERT INTO harga (jenis, id_agen, harga) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_dataagen(db):
    cursor = db.cursor()
    sql = "SELECT * FROM agen"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print("Nama Laundry : ", data[0])
            print("Nama Pemilik : ", data[1])
            print("No Telp.     : ", data[2])
            print("Email        : ", data[3])
            print("Kota         : ", data[4])
            print("Alamat       : ", data[5])
            print("Plat Driver  : ", data[6])


def update_dataagen(db):
    cursor = db.cursor()
    show_dataagen(db)
    id_agen = input("pilih id agen> ")
    nama_laundry = input("Masukan nama baru laundry: ")
    nama_pemilik = input("Masukan nama baru pemilik: ")
    telp = input("Masukan nomer telepon baru: ")
    email = input("Masukan email baru: ")
    kota = input("Masukan kota baru: ")
    alamat = input("Masukan alamat baru: ")
    plat_driver = input("Masukan nomer plat driver baru: ")

    sql = "UPDATE agen SET nama_laundry=%s, nama_pemilik=%s, telp=%s, email=%s, kota=%s, alamat=%s, plat_driver=%s WHERE id_agen=%s"
    val = (nama_laundry, nama_pemilik, telp, email,
           kota, alamat, plat_driver, id_agen)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


def delete_dataagen(db):
    cursor = db.cursor()
    show_dataagen(db)
    id_agen = input("pilih id agen> ")
    sql = "DELETE FROM agen WHERE id_agen=%s"
    val = (id_agen,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def search_dataagen(db):
    cursor = db.cursor()
    keyword = input("Masukkan nama atau kota agen laundry: ")
    sql = "SELECT * FROM agen JOIN harga ON agen.id_agen = harga.id_agen WHERE nama_laundry LIKE %s OR kota LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def insert_datapesanan(db):
    cursor = db.cursor()
    id_agen = input("pilih id agen> ")
    jenis = input("pilih Jenis paket> ")
    berat = input("Masukan berat laundry> ")

    val = (id_agen, jenis, berat)
    cursor = db.cursor()
    sql = "INSERT INTO cucian (id_agen, jenis, berat) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_datapesanan(db):
    cursor = db.cursor()
    keyword = input("Masukkan id cucian: ")
    sql = "SELECT cucian.id_cucian, cucian.id_agen, agen.nama_laundry, cucian.jenis, cucian.berat, (cucian.berat * harga.harga) AS total_bayar FROM cucian JOIN harga ON cucian.id_agen = harga.id_agen JOIN agen ON harga.id_agen=agen.id_agen WHERE id_cucian LIKE %s AND cucian.jenis = harga.jenis"
    val = ("%{}%".format(keyword),)
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print("Id Cucian    : ", data[0])
            print("Id Agen      : ", data[1])
            print("Nama Laundry : ", data[2])
            print("Jenis        : ", data[3])
            print("Berat        : ", data[4])
            print("Total Bayar  : ", data[5])


def show_datacucian(db):
    cursor = db.cursor()
    sql = "SELECT * FROM cucian"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print("id Agen      : ", data[0])
            print("Jenis        : ", data[1])
            print("Berat        : ", data[2])


def update_datacucian(db):
    cursor = db.cursor()
    show_datacucian(db)
    id_cucian = input("pilih id cucian> ")
    id_agen = input("Masukan id agen yang baru: ")
    jenis = input("Masukan jenis laundry yang baru: ")
    berat = input("Masukan berat yang baru: ")

    sql = "UPDATE cucian SET id_agen=%s, jenis=%s, berat=%s WHERE id_cucian=%s"
    val = (id_agen, jenis, berat, id_cucian)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


def delete_datacucian(db):
    cursor = db.cursor()
    show_datacucian(db)
    id_cucian = input("pilih id cucian> ")
    sql = "DELETE FROM cucian WHERE id_cucian=%s"
    val = (id_cucian,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def search_datacucian(db):
    cursor = db.cursor()
    keyword = input("Masukkan id cucian: ")
    sql = "SELECT * FROM cucian WHERE id_cucian LIKE %s"
    val = ("%{}%".format(keyword),)
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print("Id Cucian    : ", data[0])
            print("Id Agen      : ", data[1])
            print("Jenis        : ", data[2])
            print("Berat        : ", data[3])


def transaksi(db):
    cursor = db.cursor()
    keyword = input("Masukkan id cucian: ")
    sql = "SELECT cucian.id_cucian, cucian.id_agen, (cucian.berat * harga.harga) AS total_bayar FROM cucian JOIN harga ON cucian.id_agen = harga.id_agen WHERE id_cucian LIKE %s AND cucian.jenis = harga.jenis"
    val = ("%{}%".format(keyword),)
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            id_cucian = data[0]
            id_agen = data[1]
            total_bayar = data[2]
            val = (id_cucian, id_agen, total_bayar)
            cursor = db.cursor()
            sql = "INSERT INTO transaksi (id_cucian, id_agen, total_bayar) VALUES (%s, %s, %s)"
            cursor.execute(sql, val)
            db.commit()
            print("{} data berhasil disimpan".format(cursor.rowcount))

    sql = "DELETE FROM cucian WHERE id_cucian LIKE %s"
    val = ("%{}%".format(keyword),)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def show_menu(db):
    print("=== APLIKASI DATABASE PYTHON LAUNDRYKU ===")
    print("1.  Insert Data Agen")
    print("2.  Tampilkan Data Agen")
    print("3.  Update Data Agen")
    print("4.  Hapus Data Agen")
    print("5.  Cari Data Agen")
    print("6.  Insert Data Pesanan")
    print("7.  Tampilkan Data Pesanan")
    print("8.  Update Data Cucian")
    print("9.  Hapus Data Cucian")
    print("10. Cari Data Cucian")
    print("11. Transaksi")
    print("0.  Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    # clear screen
    # os.system("clear")

    if menu == "1":
        insert_agen(db)
    elif menu == "2":
        show_dataagen(db)
    elif menu == "3":
        update_dataagen(db)
    elif menu == "4":
        delete_dataagen(db)
    elif menu == "5":
        search_dataagen(db)
    elif menu == "6":
        insert_datapesanan(db)
    elif menu == "7":
        show_datapesanan(db)
    elif menu == "8":
        update_datacucian(db)
    elif menu == "9":
        delete_datacucian(db)
    elif menu == "10":
        search_datacucian(db)
    elif menu == "11":
        transaksi(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu(db)
