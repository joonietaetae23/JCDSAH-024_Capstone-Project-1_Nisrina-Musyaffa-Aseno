# Penggunaan tabulate untuk membuat tabel data
from tabulate import tabulate

from datetime import date


# ===== PROGRAM LOGIN USER =====

# Data jenis user
users = {
    "staff" : {"password" : "staff123"},
    "guest" : {"password" : "guest123"}
}

# Fungsi Login
def login() :
    print("\n=== Sistem Manajemen Proyek ===")
    while True :
        username = input("Username :")
        password = input("Password :")
        if username in users and users[username]["password"] == password :
            print(f"\nLogin Berhasil! Selamat Datang, {username}!")
            return username
        else :
            print("\nUsername atau password salah.")
            ulang = input("Coba lagi? (ya/tidak): ").lower()
            if ulang != "ya":
                return None


# ===== DATA PROYEK =====

# Dictionary data proyek dan klien
data_proyek = [
    {"ID": 10001,
    "Nama Klien": "Adi",
    "Jenis Kelamin": "Laki-laki", 
    "Nomor Telepon": "087812345678",
    "Kavling": "Orchid",
    "Progres Pembangunan" : "50%"},

    {"ID": 10002,
    "Nama Klien": "Rayna",
    "Jenis Kelamin": "Perempuan",
    "Nomor Telepon": "087898765432",
    "Kavling": "Magenta",
    "Progres Pembangunan" : "0%"},

    {"ID": 10003,
    "Nama Klien": "Iceu",
    "Jenis Kelamin": "Perempuan",
    "Nomor Telepon": "087811112222",
    "Kavling": "Violet",
    "Progres Pembangunan" : "75%"},

    {"ID": 10004,
    "Nama Klien": "Hanif",
    "Jenis Kelamin": "Laki-laki",
    "Nomor Telepon": "087899887766",
    "Kavling": "Orchid",
    "Progres Pembangunan" : "100%"}
]

# Perhitungan perkiraan proyek pembangunan selesai sesuai dengan data progres yang ada
def tambah_waktu(sekarang, sisa_bulan) :
    bulan_selesai = sekarang.month + sisa_bulan
    # Antisipasi kelebihan bulan
    tahun_selesai = sekarang.year + ((bulan_selesai - 1) // 12) # Berapa tahun yang berlebih?
    # Penyusunan ulang bulan
    bulan_selesai = ((bulan_selesai - 1) % 12) + 1

    nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][bulan_selesai - 1]

    return (f"{nama_bulan} {tahun_selesai}")

def kapan_selesai(progres) :
    if progres == "25%" :
        return tambah_waktu(date.today(), 6)
    elif progres == "50%" :
        return tambah_waktu(date.today(), 4)
    elif progres == "75%" :
        return tambah_waktu(date.today(), 2)
    elif progres == "100%" :
        return tambah_waktu(date.today(), 0)
    else :
        return "Belum diketahui"

# Membahkan data perkiraan kapan proyek akan selesai pada tabel data
for proyek in data_proyek:
    progres = proyek["Progres Pembangunan"]
    proyek["Perkiraan Selesai"] = kapan_selesai(progres)

# Membuat tabel data menggunakan tabulate
def tabel_data() :
    headers = [
        "No", "ID", "Nama Klien", "Jenis Kelamin", "Nomor Telepon", "Kavling", "Progres Pembangunan", "Perkiraan Selesai"
    ]
    tabel = [
            [i + 1,
            p["ID"], p["Nama Klien"], p["Jenis Kelamin"], p["Nomor Telepon"], p["Kavling"], p["Progres Pembangunan"], p["Perkiraan Selesai"]]
            for i, p in enumerate(data_proyek)
        ]
    return tabulate(tabel, headers=headers, tablefmt="grid")


# ===== PROGRAM MENU UTAMA STAFF DAN GUEST =====

# Menu untuk staff
def menu_utama_adm() :
    while True :
        print("\n=== Selamat Datang di Menu Utama")
        print("List Menu :")
        print("1. Menampilkan Seluruh Data Proyek")
        print("2. Menambah Proyek Baru")    
        print("3. Menghapus Proyek")
        print("4. Mengubah Data Proyek")
        print("5. Exit Program")

        try :
            menu = int(input("Masukkan angka menu yang ingin dijalankan : "))
        except ValueError :
            print("\nInput harus berupa angka!")
            continue
        
        # === 1. Display Data Proyek ===
        if menu == 1 :
            print(tabel_data())

        # === 2. Menambah Proyek Baru ===
        elif menu == 2 :
            print("\n=== Tambah Proyek Baru ===")

            # ID harus angka
            try:
                ID_baru = int(input("Masukkan ID Proyek : "))
            except ValueError:
                print("ID proyek harus berupa angka!")
                continue
            
            # Nama tidak boleh berisi angka
            nama_baru = input("Nama Klien: ").title()
            while not nama_baru.isalpha():
                print("Nama hanya boleh huruf!")
                nama_baru = input("Nama Klien: ").title()

            # Jenis kelamin harus perempuan/laki-laki
            jeniskel_baru = input("Jenis Kelamin (Perempuan/Laki-laki): ").title()
            while jeniskel_baru not in ["Perempuan", "Laki-Laki"]:
                print("Jenis kelamin harus 'Perempuan' atau 'Laki-laki'")
                jeniskel_baru = input("Jenis Kelamin (Perempuan/Laki-laki): ").title()

            # Nomor telepon harus angka
            notelp_baru = input("Nomor Telepon Klien: ")
            while not notelp_baru.isdigit():
                print("Nomor telepon hanya boleh angka!")
                notelp_baru = input("Nomor Telepon Klien: ")

            kavling_baru = str(input("Jenis Kavling: ")).title()

            progres_baru = "0%"

            status_baru = kapan_selesai(progres_baru)
            
            proyek_baru = {
                "ID" : ID_baru,
                "Nama Klien" : nama_baru,
                "Jenis Kelamin" : jeniskel_baru,
                "Nomor Telepon" : notelp_baru,
                "Kavling" : kavling_baru,
                "Progres Pembangunan" : progres_baru,
                "Perkiraan Selesai" : status_baru
            }

            data_proyek.append(proyek_baru)

            print(f"Proyek {ID_baru} berhasil ditambahkan!\n")

        # === 3. Menghapus Proyek ===
        elif menu == 3 :
            print(tabel_data())

            try :
                hapus_ID = int(input("Masukkan ID proyek yang ingin dihapus: "))
                proyek_ditemukan = None
                for proyek in data_proyek:
                    if proyek["ID"] == hapus_ID:
                        proyek_ditemukan = proyek
                        break

                if proyek_ditemukan:
                    validate = input(f"Apakah Anda yakin ingin menghapus proyek dengan ID {hapus_ID}? (ya/tidak): ").lower()
                    if validate == "ya":
                        data_proyek.remove(proyek_ditemukan)
                        print(f"\nProyek dengan ID {hapus_ID} berhasil dihapus!")
                    else:
                        print("Penghapusan dibatalkan.")
                else:
                    print("ID proyek tidak ditemukan!")
            except ValueError:
                print("Input ID harus berupa angka!")
                

        # === 4. Mengubah Data Proyek ===
        elif menu == 4 :
            print("\n=== Ubah Data Proyek ===")
            print(tabel_data())

            try :
                ubah_id = int(input("\nMasukkan ID proyek yang ingin diubah: "))
                proyek_ditemukan = None

                for proyek in data_proyek :
                    if proyek["ID"] == ubah_id :
                        proyek_ditemukan = proyek
                        break

                if proyek_ditemukan is None :
                    print(f"\nProyek dengan ID {ubah_id} tidak ditemukan!")
                
                else :
                    print("\nData proyek ditemukan!")
                    for kolom, data in proyek_ditemukan.items() :
                        print(f"{kolom} : {data}")

                    print("\nPilih data yang ingin diubah:")
                    print("1. Nama Klien")
                    print("2. Jenis Kelamin")
                    print("3. Nomor Telepon")
                    print("4. Kavling")
                    print("5. Progres Pembangunan")
                    print("6. Batalkan Perubahan")

                    ubah_pilihan = input("\nMasukkan pilihan (1-6): ")

                    if ubah_pilihan == "1" :
                        proyek_ditemukan["Nama Klien"] = input("Masukkan nama klien baru: ").title()
                    elif ubah_pilihan == "2":
                        proyek_ditemukan["Jenis Kelamin"] = input("Masukkan jenis kelamin baru (Laki-laki/Perempuan): ").title()
                    elif ubah_pilihan == "3":
                        proyek_ditemukan["Nomor Telepon"] = input("Masukkan nomor telepon baru: ")
                    elif ubah_pilihan == "4":
                        proyek_ditemukan["Kavling"] = input("Masukkan jenis kavling baru: ").title()
                    elif ubah_pilihan == "5":
                        input_progres = input("Masukkan progres baru (%): ").strip()
                        # Agar input selalu dalam bentuk % tanpa spasi
                        if not input_progres.endswith("%"):
                            input_progres += "%"
                        proyek_ditemukan["Progres Pembangunan"] = input_progres
                        proyek_ditemukan["Perkiraan Selesai"] = kapan_selesai(proyek_ditemukan["Progres Pembangunan"])
                    elif ubah_pilihan == "6":
                        print("\nPerubahan dibatalkan.")
                        continue
                    else:
                        print("\nPilihan tidak valid.")
                        continue

                    print(f"\nData proyek {ubah_id} berhasil diperbaharui!")

            except ValueError :
                print("\nID harus berupa angka!")
                
        # === 5. Exit Program ===

        elif menu == 5 :
            print("\nTerima kasih, program selesai.")
            break

        # === 6. Input tidak ada dalam menu ===
        else :
            print("\nMenu tidak tersedia, silakan pilih menu yang ingin dijalankan (1-5)")


# Menu untuk guest
def menu_user() :
    while True :
        print("\n=== Menu Guest ===")
        print("1. Cari proyek berdasarkan nama klien")
        print("2. Hubungi Kami")
        print("3. Keluar")

        try :
            menu = int(input("Pilih menu (1/2/3):"))
        except ValueError :
            print("Input harus berupa angka!")
            continue

        if menu == 1 :
            nama = input("Masukkan nama klien: ").title()
            ditemukan = [p for p in data_proyek if p["Nama Klien"] == nama]

            if ditemukan :
                print("\n=== Hasil Pencarian ===")
                headers = ["Nama Klien", "Kavling", "Progres Pembangunan", "Perkiraan Selesai"]
                tabel = [[
                    p["Nama Klien"], p["Kavling"], p["Progres Pembangunan"], p["Perkiraan Selesai"]
                ] for p in ditemukan ]

                print(tabulate(tabel, headers=headers, tablefmt = "grid"))
            
            else :
                print("\nData tidak ditemukan.")

        elif menu == 2 :
            print("\n=== Hubungi Kami ===")
            print("\n081212312312")
            print("\nadminkami@gmail.com")

        elif menu == 3 :
            print("\nTerima kasih, program telah selesai.")
            break

        else :
            print("\nMenu tidak valid.")


# ===== PROGRAM LOGIN UTAMA ===
role = login()

if role == "staff" :
    menu_utama_adm()
elif role == "guest" :
    menu_user()
else :
    print("Program selesai.")