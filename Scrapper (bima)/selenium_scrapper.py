from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import os 

# 1. Konfigurasi Khusus untuk Brave Browser
options = Options()
options.binary_location = '/usr/bin/brave-browser'

print("Memulai browser...")
driver = webdriver.Chrome(options=options)

try:
    data_json = {}
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            try:
                data_json = json.load(file)
            except json.JSONDecodeError:
                pass

    if "list" not in data_json or not isinstance(data_json["list"], list):
        data_json["list"] = []

    # 3. Buka halaman
    print("Membuka situs Detik...")
    driver.get('https://news.detik.com/indeks')
    driver.implicitly_wait(10)

    # 4. Mencari Elemen
    judul_elemen = driver.find_elements(By.CSS_SELECTOR, 'div.media h3 a')
    waktu = driver.find_elements(By.CSS_SELECTOR, 'div.media div.media__date span')
    link_elemen = driver.find_elements(By.CSS_SELECTOR, 'div.media div.media__image a')
    gambar_elemen = driver.find_elements(By.CSS_SELECTOR, 'div.media div.media__image a span img')

    # 5. Ekstrak dan Print Data
    print("\n=== 5 Berita Terbaru di Detik Saat Ini ===")
    batas = min(5, len(judul_elemen))

    for i in range(batas):
        teks_judul = judul_elemen[i].text
        waktu_berita = waktu[i].text
        link = link_elemen[i].get_attribute('href')
        gambar = gambar_elemen[i].get_attribute('src')
        print(f"{i+1}. {teks_judul}")

        data_json["list"].append({
            "Nomor": i+1,
            "Judul": teks_judul,
            "Waktu": waktu_berita,
            "Link": link,
            "Gambar": gambar,
        })

    with open("data.json", "w") as file:
        json.dump(data_json, file, indent=4)
    print("\nData berhasil disimpan ke data.json")

except Exception as e:
    print(f"\nTerjadi kesalahan: {e}")

finally:
    # 6. Tutup browser
    driver.quit()
    print("\nSelesai dan browser ditutup.")