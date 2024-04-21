import random
import numpy as np
import requests
import socket
import queue
import pandas as pd
import urllib
from gift import __main__
from voucher import __main__
from wallet import __main__

def generate_promo_code(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def apply_promo_code_to_website(website):
    promo_code = generate_promo_code(8)
    # Logika untuk menerapkan promo code ke website
    print(f"Promo code {promo_code} telah diterapkan pada {website}")

def generate_gift_voucher(size):
    voucher = np.random.choice(10000, size=size, replace=False)
    return voucher

def redeem_voucher(voucher):
    # Logika untuk penukaran voucher dengan Google points atau Google gift
    print(f"Voucher {voucher} telah ditukarkan")

def search_google(keyword):
    # Logika untuk mencari di Google menggunakan kata kunci tertentu
    search_query = urllib.parse.quote(keyword)
    url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(url)
    # Logika untuk mengambil dan memproses hasil pencarian dari Google
    print("Hasil pencarian Google untuk", keyword)
    print(response.text)

def main():
    # Contoh penggunaan fitur promo code
    apply_promo_code_to_website("play.google.com")

    # Contoh penggunaan fitur gift voucher
    gift_voucher = generate_gift_voucher(5)
    for voucher in gift_voucher:
        redeem_voucher(voucher)

    # Contoh penggunaan pencarian di Google dengan kata kunci "gift voucher"
    search_google("gift voucher")

if __name__ == "__main__":
    main()
import random
import numpy as np
import requests
import json

def generate_gift_code():
    code_length = 8
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    gift_code = ''.join(random.choice(characters) for _ in range(code_length))
    return gift_code

def generate_promo_code(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    promo_code = ''.join(random.choice(characters) for _ in range(length))
    return promo_code

def apply_promo_code(website, promo_code):
    # Logika untuk menerapkan promo code ke website
    print(f"Promo code {promo_code} telah diterapkan pada {website}")

def generate_coupons_and_titles(num_coupons):
    list_of_coupons_and_title = [
        {"coupon": generate_gift_code(), "title": "Diskon untuk item A"},
        {"coupon": generate_gift_code(), "title": "Gratis ongkir untuk item B"},
        {"coupon": generate_gift_code(), "title": "Potongan 50% untuk item C"},
        {"coupon": generate_gift_code(), "title": "Penawaran spesial untuk item D"},
    ]
    return list_of_coupons_and_title

def apply_coupons_to_items(list_of_coupons_and_title):
    for indx, coupon_and_title in enumerate(list_of_coupons_and_title):
        coupon = coupon_and_title["coupon"]
        title = coupon_and_title["title"]
        # Logika untuk menerapkan kupon pada item tertentu
        print(f"Kupon {coupon} ({title}) telah diterapkan pada item ke-{indx+1}")

def save_coupons_to_file(coupons, filename):
    with open(filename, "w") as f:
        for coupon in coupons:
            f.write(coupon + "\n")

def main():
    # Meminta input dari pengguna untuk website target
    website = input("Masukkan website target: ")

    # Menghasilkan promo code dan menerapkannya pada website
    promo_code = generate_promo_code(8)
    apply_promo_code(website, promo_code)

    # Menghasilkan daftar kupon dan judul
    num_coupons = 10
    list_of_coupons_and_title = generate_coupons_and_titles(num_coupons)

    # Menerapkan kupon pada item-item
    apply_coupons_to_items(list_of_coupons_and_title)

    # Simpan kupon ke dalam file coupons.txt
    coupon_codes = [coupon_and_title["coupon"] for coupon_and_title in list_of_coupons_and_title]
    save_coupons_to_file(coupon_codes, "coupons.txt")

if __name__ == "__main__":
    main()
