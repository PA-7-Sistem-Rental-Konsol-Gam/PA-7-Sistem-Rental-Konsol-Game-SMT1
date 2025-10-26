#PA DDP SISTEM RENTAL KONSOL GAME 
#Riaz Ramadhan Al Fattah
#Arizky Saputra
#Otniel Putra


import json
import os
from datetime import datetime
from prettytable import PrettyTable
import pwinput

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "Data_Pengguna.json")
PRODUCTS_FILE = os.path.join(DATA_DIR, "List_Konsol.json")
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "Data_Transaksi.json")

# Utilitas: load/save file ke JSON
def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ID generator, pencari id
def next_id(prefix, existing_ids):
    # Format: PREFIX-XXXX
    num = 1
    while True:
        candidate = f"{prefix}-{num:04d}"
        if candidate not in existing_ids:
            return candidate
        num += 1

def find_user(users, username):
    for u in users:
        if u["username"] == username:
            return u
    return None
1
def find_product(products, pid):
    for p in products:
        if p["id"] == pid:
            return p
    return None

def find_transaction(transactions, tid):
    for t in transactions:
        if t["id"] == tid:
            return t
    return None

# -----------------------------
# register & login
# -----------------------------
def register(users):
    print("=== Registrasi Akun Baru ===")
    username = input("Username baru: ").strip()
    if not username:
        print("Username tidak boleh kosong.")
        return None

    if find_user(users, username):
        print("Username sudah terpakai.")
        return None

    password = pwinput.pwinput("Password: ").strip()
    if not password:
        print("Password tidak boleh kosong.")
        return None

    existing_ids = [u["id"] for u in users]
    uid = next_id("U", existing_ids)
    new_user = {
        "id": uid,
        "username": username,
        "password": password,  # Catatan: untuk produksi, gunakan hashing
        "role": "user",
        "balance": 0
    }
    users.append(new_user)
    save_json(USERS_FILE, users)
    print(f"Akun berhasil dibuat. ID: {uid}, Role: user")
    return new_user

def login(users):
    print("=== Log In ===")
    username = input("Username: ").strip()
    password = pwinput.pwinput("Password: ").strip()

    user = find_user(users, username)
    if user and user["password"] == password:
        print(f"Selamat datang, {user['username']}! Role: {user['role']}")
        return user
    print("Login gagal. Periksa username/password.")
    return None

# Tabel tampilan pretty table
def show_products_table(products):
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Brand", "Tarif/Perjam", "Stok"]
    for p in products:
        table.add_row([p["id"], p["name"], p["brand"], p["perjam"], p["stock"]])
    print(table)

def show_users_table(users):
    table = PrettyTable()
    table.field_names = ["ID", "Username", "Role", "Saldo"]
    for u in users:
        table.add_row([u["id"], u["username"], u["role"], u["balance"]])
    print(table)

def show_transactions_table(transactions):
    table = PrettyTable()
    table.field_names = ["ID", "User", "Produk", "Hari", "Total", "Tgl", "Metode"]
    for t in transactions:
        table.add_row([
            t["id"], t["user_id"], t["product_id"], t["perjam"],
            t["total"], t["created_at"], t["method"]
        ])
    print(table)

# Admin Bagian CRUD 
def admin_create_product(products):
    print("=== Tambah Produk ===")
    name = input("Nama produk: ").strip()
    brand = input("Brand: ").strip()
    try:
        perjam = int(input("Tarif perjam (angka): ").strip())
        stock = int(input("Stok (angka): ").strip())
        if perjam < 1000 or perjam > 100000:
            print("Tarif perjam harus antara 1.000 dan 100.000.")
            return
        if stock < 1 or stock > 100:
            print("Stok harus antara 1 dan 100.")
            return
    except ValueError:
        print("Tarif/Stok harus angka.")
        return

    existing_ids = [p["id"] for p in products]
    pid = next_id("P", existing_ids)
    new_p = {
        "id": pid, "name": name, "brand": brand,
        "perjam": perjam, "stock": stock
    }
    products.append(new_p)
    save_json(PRODUCTS_FILE, products)
    print(f"Produk {pid} berhasil ditambahkan.")

def admin_update_product(products):
    show_products_table(products)
    try:
        print("=== Ubah Produk ===")
        pid = input("Masukkan ID produk: ").strip()
        p = find_product(products, pid)
        if not p:
            print("Produk tidak ditemukan.")
            return
        print("Kosongkan input jika tidak ingin mengubah field tertentu.")
        name = input(f"Nama ({p['name']}): ").strip()
        brand = input(f"Brand ({p['brand']}): ").strip()
        perjam_str = input(f"Tarif/Perjam ({p['perjam']}): ").strip()
        if perjam_str:
            try:
                perjam = int(perjam_str)
                if perjam < 1000 or perjam > 100000:
                    print("Tarif perjam harus antara 1.000 dan 100.000.")
                    return
                p["perjam"] = perjam
            except ValueError:
                print("Tarif harus berupa angka.")
                return
        stock_str = input(f"Stok ({p['stock']}): ").strip()
        if stock_str:
            try:
                stock = int(stock_str)
                if stock < 1 or stock > 100:
                    print("Stok harus antara 1 dan 100.")
                    return
                p["stock"] = stock
            except ValueError:
                print("Stok harus berupa angka.")
                return
        print("Produk berhasil diperbarui!")
    except KeyboardInterrupt:
        return admin_update_product(products)
    
    if name: p["name"] = name
    if brand: p["brand"] = brand
    if perjam_str:
        try: p["perjam"] = int(perjam_str)
        except ValueError: print("Tarif harus angka. Diabaikan.")
    if stock_str:
        try: p["stock"] = int(stock_str)
        except ValueError: print("Stok harus angka. Diabaikan.")

    save_json(PRODUCTS_FILE, products)
    print(f"Produk {pid} berhasil diperbarui.")

def admin_delete_product(products):
    show_products_table(products)
    print("=== Hapus Produk ===")
    pid = input("Masukkan ID produk: ").strip()
    p = find_product(products, pid)
    if not p:
        print("Produk tidak ditemukan.")
        return
    products.remove(p)
    save_json(PRODUCTS_FILE, products)
    print(f"Produk {pid} dihapus.")

def admin_list_products(products):
    print("=== Daftar Produk ===")
    show_products_table(products)


# Admin: CRUD User (opsional, contoh)
def admin_list_users(users):
    print("=== Daftar Pengguna ===")
    show_users_table(users)

def admin_update_user(users):
    show_users_table(users)
    print("=== Ubah Pengguna ===")
    uid = input("Masukkan ID user: ").strip()
    user = next((u for u in users if u["id"] == uid), None)
    if not user:
        print("User tidak ditemukan.")
        return
    print("Kosongkan input jika tidak ingin mengubah field tertentu.")
    username = input(f"Username ({user['username']}): ").strip()
    role = input(f"Role ({user['role']}) [admin/user]: ").strip()
    balance_str = input(f"Saldo ({user['balance']}): ").strip()

    if username: user["username"] = username
    if role in ("admin", "user"): user["role"] = role
    if balance_str:
        try: user["balance"] = int(balance_str)
        except ValueError: print("Saldo harus angka. Diabaikan.")

    save_json(USERS_FILE, users)
    print(f"User {uid} diperbarui.")

def admin_delete_user(users, transactions):
    show_users_table(users)
    print("=== Hapus Pengguna ===")
    uid = input("Masukkan ID user: ").strip()
    user = next((u for u in users if u["id"] == uid), None)
    if not user:
        print("User tidak ditemukan.")
        return
    # Cegah hapus admin terakhir (opsional)
    admins = [u for u in users if u["role"] == "admin"]
    if user["role"] == "admin" and len(admins) == 1:
        print("Tidak bisa menghapus satu-satunya admin.")
        return
    users.remove(user)
    save_json(USERS_FILE, users)
    # Opsional: hapus transaksi terkait user
    transactions[:] = [t for t in transactions if t["user_id"] != uid]
    save_json(TRANSACTIONS_FILE, transactions)
    print(f"User {uid} dihapus.")


# User: fitur saldo dan transaksi
def user_topup_balance(current_user, users):
    print("=== Top Up Saldo E-money ===")
    try:
        amount = int(input("Nominal top up: ").strip())
        if amount <= 0:
            print("Nominal harus lebih dari 0.")
            return
        if amount > 1_000_000_000:
            print("Nominal maksimal 1 miliar.")
            return

    except ValueError:
        print("Nominal harus angka.")
        return
    current_user["balance"] += amount
    save_json(USERS_FILE, users)
    print(f"Top up berhasil. Saldo sekarang: {current_user['balance']}")

def user_rent_product(current_user, users, products, transactions):
    print("=== Sewa Produk ===")
    show_products_table(products)
    pid = input("Masukkan ID produk: ").strip()
    product = find_product(products, pid)
    if not product:
        print("Produk tidak ditemukan.")
        return
    if product["stock"] <= 0:
        print("Stok habis.")
        return

    try:
        perjam = int(input("Jumlah sewa per jam: ").strip())
        if perjam <= 0:
            print("Per jam harus lebih dari 0.")
            return
        if perjam > 168:
            print("Maksimal 168 jam untuk penyewaan.")
            return
    except ValueError:
        print("Sewa per jam harus angka.")
        return

    total = product["perjam"] * perjam
    print(f"Total biaya: {total}")
    if current_user["balance"] < total:
        print("Saldo tidak cukup. Silakan top up terlebih dahulu.")
        return

    # Konfirmasi pertama
    confirm1 = input("Apakah Anda yakin ingin menyewa produk ini? (ya/tidak): ").strip().lower()
    if confirm1 != "ya":
        print("Penyewaan dibatalkan.")
        return

    # Konfirmasi kedua
    confirm2 = input("Konfirmasi sekali lagi untuk menyewa produk ini. Lanjutkan? (ya/tidak): ").strip().lower()
    if confirm2 != "ya":
        print("Penyewaan dibatalkan.")
        return

    # Jika lolos dua kali konfirmasi, proses transaksi
    current_user["balance"] -= total
    product["stock"] -= 1
    transactions.append({
        "user": current_user["username"],
        "product": product["name"],
        "hours": perjam,
        "total": total
    })
    print("Penyewaan berhasil dilakukan!")


    # Potong saldo, kurangi stok, simpan transaksi
    current_user["balance"] -= total
    product["stock"] -= 1
    save_json(USERS_FILE, users)
    save_json(PRODUCTS_FILE, products)

    existing_tids = [t["id"] for t in transactions if isinstance(t, dict) and "id" in t]
    tid = next_id("T", existing_tids)

    trx = {
        "id": tid,
        "user_id": current_user["id"],
        "product_id": product["id"],
        "perjam": perjam,
        "total": total,
        "method": "E-money",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

    transactions.append(trx)
    save_json(TRANSACTIONS_FILE, transactions)

    print("== Invoice ===")
    table = PrettyTable()
    table.field_names = ["Invoice ID", "User", "Produk", "Hari", "Tarif/perjam", "Total", "Metode", "Tanggal"]
    table.add_row([
        trx["id"], current_user["username"], product["name"], perjam,
        product["perjam"], total, trx["method"], trx["created_at"]
    ])
    print(table)
    print("Terima kasih! Sewa berhasil.")

def user_view_transactions(current_user, transactions):
    print("=== Riwayat Transaksi Saya ===")
    my_trx = [t for t in transactions if t["user_id"] == current_user["id"]]
    if not my_trx:
        print("Belum ada transaksi.")
        return
    show_transactions_table(my_trx)


# Menu: Admin dan User
def admin_menu(current_user, users, products, transactions):
    try:
        print("")
        while True:
            print("=== Menu Admin ===")
            print("1. Lihat semua produk")
            print("2. Tambah produk")
            print("3. Ubah produk")
            print("4. Hapus produk")
            print("5. Lihat semua pengguna")
            print("6. Ubah pengguna")
            print("7. Hapus pengguna")
            print("8. Lihat semua transaksi")
            print("9. Log out")
            choice = input("Pilih: ").strip()
            if choice == "1":
                admin_list_products(products)
            elif choice == "2":
                admin_create_product(products)
            elif choice == "3":
                admin_update_product(products)
            elif choice == "4":
                admin_delete_product(products)
            elif choice == "5":
                admin_list_users(users)
            elif choice == "6":
                admin_update_user(users)
            elif choice == "7":
                admin_delete_user(users, transactions)
            elif choice == "8":
                print("=== Semua Transaksi ===")
                show_transactions_table(transactions)
            elif choice == "9":
                print("Log out...")
                break
            else:
                print("Pilihan tidak valid.")
    except KeyboardInterrupt:
        print("Tidak Bisa keluar")
        return admin_menu(current_user, users, products, transactions)
    except EOFError:
        print("\nTidak bisa keluar dengan Ctrl+Z")
        return admin_menu(current_user, users, products, transactions)

def user_menu(current_user, users, products, transactions):
    try: 
        while True:
            print("=== Menu User ===")
            print(f"Saldo: {current_user['balance']}")
            print("1. Lihat produk")
            print("2. Top up saldo")
            print("3. Sewa produk (E-money)")
            print("4. Lihat transaksi saya")
            print("5. Log out")
            choice = input("Pilih: ").strip()
            if choice == "1":
                show_products_table(products)
            elif choice == "2":
                user_topup_balance(current_user, users)
            elif choice == "3":
                user_rent_product(current_user, users, products, transactions)
            elif choice == "4":
                user_view_transactions(current_user, transactions)
            elif choice == "5":
                print("Log out...")
                break
            else:
                print("Pilihan tidak valid.")
    except KeyboardInterrupt:
        print("Gabisa")
        return user_menu(current_user, users, products, transactions)
    except EOFError:
        print("\nTidak bisa keluar dengan Ctrl+Z")
        return user_menu(current_user, users, products, transactions)

# Looping
def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    for path in [USERS_FILE, PRODUCTS_FILE, TRANSACTIONS_FILE]:
        if not os.path.exists(path):
            # Inisialisasi kosong jika belum ada
            save_json(path, [])

def main():
    ensure_data_dir()
    users = load_json(USERS_FILE)
    products = load_json(PRODUCTS_FILE)
    transactions = load_json(TRANSACTIONS_FILE)
    try:
        while True:
            print("=== Sistem Rental Konsol Game ===")
            print("1. Log in")
            print("2. Registrasi")
            print("3. Keluar")
            choice = input("Pilih: ").strip()

            if choice == "1":
                user = login(users)
                if user:
                    if user["role"] == "admin":
                        admin_menu(user, users, products, transactions)
                    else:
                        user_menu(user, users, products, transactions)
            elif choice == "2":
                new_user = register(users)
                if new_user:
                    print("Silakan log in untuk mulai bertransaksi.")
            elif choice == "3":
                print("Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid.")
    except KeyboardInterrupt:
        print("Tidak Bisa keluar")
        return main()
    except EOFError:
        print("\nTidak bisa keluar dengan Ctrl+Z")
        return main()

if __name__ == "__main__":
    main()
