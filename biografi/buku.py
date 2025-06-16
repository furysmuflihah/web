buku = []

def pilih():
    print("\n[1] Tambah Data")
    print("[2] Lihat Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Keluar")

    menu = input("Pilih aksi > ")

    if menu == '1':
        tambah()
    elif menu == '2':
        lihat()
    elif menu == '3':
        edit()
    elif menu == '4':
        hapus()
    elif menu == '5':
        print("Program selesai.")
        exit()
    else:
        print("Pilih sesuai menu")
        pilih()

# Menambah data
def tambah():
    x = input('Masukkan Nama Buku = ')
    buku.append(x)
    print("Data berhasil ditambahkan.")

# Menampilkan data
def lihat():
    if len(buku) <= 0:
        print("Data masih kosong.")
    else:
        print("\nDaftar Buku:")
        for i, name in enumerate(buku):
            print(f"[{i}] {name}")

# Mengedit data
def edit():
    lihat()
    if len(buku) > 0:
        try:
            index = int(input("Masukkan indeks buku yang ingin diedit: "))
            if 0 <= index < len(buku):
                new_value = input("Masukkan nama buku baru: ")
                buku[index] = new_value
                print("Data berhasil diubah.")
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Masukkan angka yang benar.")

# Menghapus data
def hapus():
    lihat()
    if len(buku) > 0:
        try:
            index = int(input("Masukkan indeks buku yang ingin dihapus: "))
            if 0 <= index < len(buku):
                del buku[index]
                print("Data berhasil dihapus.")
            else:
                print("Indeks tidak valid.")
        except ValueError:
            print("Masukkan angka yang benar.")

# Program utama
while True:
    pilih()
