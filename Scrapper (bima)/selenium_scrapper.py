from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import os
import time

def setup_driver():
    """Konfigurasi dan return WebDriver untuk Brave Browser."""
    options = Options()
    options.binary_location = '/usr/bin/brave-browser'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=options)
    return driver

def get_article_links(driver, url):
    """Buka URL, tunggu halaman dimuat, lalu ambil dan filter link artikel."""
    driver.get(url)
    time.sleep(2)

    from urllib.parse import urlparse
    base_domain = urlparse(url).scheme + "://" + urlparse(url).netloc

    keywords = ['/read/', '/artikel/', '/berita/', '/news/']

    elements = driver.find_elements(By.TAG_NAME, 'a')
    article_links = set()

    for el in elements:
        href = el.get_attribute('href')
        if href and href.startswith(base_domain):
            if any(kw in href for kw in keywords):
                article_links.add(href)

    return list(article_links)

print("Memulai browser...")
driver = setup_driver()

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

    print("Membuka situs Detik...")
    driver.get('https://news.detik.com/indeks')
    driver.implicitly_wait(10)

    judul_elemen = driver.find_elements(By.CSS_SELECTOR, 'div.media h3 a')
    waktu = driver.find_elements(By.CSS_SELECTOR, 'div.media div.media__date span')
    link_elemen = driver.find_elements(By.CSS_SELECTOR, 'div.media div.media__image a')
    gambar_elemen = driver.find_elements(By.CSS_SELECTOR, 'div.media div.media__image a span img')

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
    driver.quit()
    print("\nSelesai dan browser ditutup.")