import os
import json
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Fungsi clear screen sesuai OS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Aktifkan colorama
init(autoreset=True)

# Fungsi tampilkan banner
def tampilkan_banner():
    print("""
╭━━╮╭━━━╮   ╭━━━╮╱╱╭╮╱╱╭╮╱╱╱╱╱╱╱╱
╰┫┣╯┃╭━╮┃   ┃╭━━╯╱╱┃┃╱╭╯╰╮╱╱╱╱╱╱╱
╱┃┃╱┃┃╱╰╯   ┃╰━━╮╭╮┃┃╱╰╮╭╯╭━━╮╭━╮
╱┃┃╱┃┃╭━╮   ┃╭━━╯┣┫┃┃╱╱┃┃╱┃┃━┫┃╭╯
╭┫┣╮┃╰┻━┃   ┃┃╱╱╱┃┃┃╰╮╱┃╰╮┃┃━┫┃┃╱
╰━━╯╰━━━╯   ╰╯╱╱╱╰╯╰━╯╱╰━╯╰━━╯╰╯╱
Author      : Febry Afriansyah
Email       : febryafriansyah@programmer.net
Github      : github.com/hatakecnk
""")

# Fungsi input file dengan validasi
def input_file(jenis):
    while True:
        path = input(f"Masukkan file {jenis}: ").strip('"').strip("'")
        if os.path.exists(path):
            return path
        else:
            print(Fore.RED + f"❌ File tidak ditemukan: {path}\nSilakan coba lagi.\n")

# Fungsi ekstrak username dari HTML/JSON
def ambil_usernames(file_path):
    usernames = set()
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.html':
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
        for div in soup.find_all('div', class_='_a6-p'):
            nested_div = div.find('div')
            if nested_div:
                user_div = nested_div.find('div')
                if user_div:
                    username = user_div.get_text(strip=True)
                    usernames.add(username)

    elif ext == '.json':
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for entry in data:
            try:
                username = entry['string_list_data'][0]['value']
                usernames.add(username)
            except (KeyError, IndexError, TypeError):
                continue

    return usernames

# ==== MULAI PROGRAM ====

clear_screen()
tampilkan_banner()
print(f"{Style.BRIGHT}📁 Program dijalankan dari folder: {os.getcwd()}\n")

print("📂 Masukkan path ke file followers (HTML atau JSON)")
print("👉 Contoh (file di folder ini): followers_1.html")
print("👉 Contoh (full path): C:/Users/Kamu/Documents/following.json\n")
followers_file = input_file("followers")
following_file = input_file("following")

clear_screen()
tampilkan_banner()

# Proses data
followers = ambil_usernames(followers_file)
following = ambil_usernames(following_file)
tidak_follow_back = following - followers
fans_kamu = followers - following

# Simpan ke file
with open('not_following_back.txt', 'w', encoding='utf-8') as f:
    f.write('🔴 Tidak Follow Balik (Kamu follow dia, dia nggak follow kamu)\n')
    f.write('-------------------------------------------------------------\n')
    for idx, user in enumerate(sorted(tidak_follow_back), start=1):
        f.write(f"{idx}. {user}\n")

with open('you_dont_follow_back.txt', 'w', encoding='utf-8') as f:
    f.write('🟢 Kamu Tidak Follow Balik (Dia follow kamu, kamu nggak follow dia)\n')
    f.write('---------------------------------------------------------------\n')
    for idx, user in enumerate(sorted(fans_kamu), start=1):
        f.write(f"{idx}. {user}\n")

# === MENU INTERAKTIF ===
while True:
    print('='*70)
    print(Style.BRIGHT + 'MENU:')
    print('1. Lihat akun yang Tidak Follow Balik')
    print('2. Lihat akun yang Kamu Tidak Follow Balik')
    print('0. Keluar')
    print('='*70)
    pilihan = input('Pilih opsi (1/2/0): ')

    if pilihan == '1':
        print('\n' + '='*70)
        print(Fore.RED + Style.BRIGHT + '🔴 Tidak Follow Balik (Kamu follow dia, dia nggak follow kamu)')
        print('='*70)
        if tidak_follow_back:
            for idx, user in enumerate(sorted(tidak_follow_back), start=1):
                print(f"{Fore.RED}{idx}. {Fore.WHITE}{user}")
            print(Fore.RED + f"\nTotal: {len(tidak_follow_back)} akun\n")
        else:
            print(Fore.GREEN + "✅ Semua orang sudah follow kamu balik! 😎")

    elif pilihan == '2':
        print('\n' + '='*70)
        print(Fore.GREEN + Style.BRIGHT + '🟢 Kamu Tidak Follow Balik (Dia follow kamu, kamu nggak follow dia)')
        print('='*70)
        if fans_kamu:
            for idx, user in enumerate(sorted(tidak_follow_back), start=1):
                print(f"{Fore.BLUE}{idx}. {Fore.WHITE}{user}")
            print(Fore.GREEN + f"\nTotal: {len(fans_kamu)} akun\n")
        else:
            print(Fore.GREEN + "✅ Kamu sudah follow semua followers kamu! 😎")

    elif pilihan == '0':
        print(Style.BRIGHT + "\n👋 Terima kasih sudah menggunakan tools ini!\n")
        break
    else:
        print(Fore.YELLOW + "⚠️ Pilihan tidak valid. Silakan pilih 1, 2, atau 0.\n")
