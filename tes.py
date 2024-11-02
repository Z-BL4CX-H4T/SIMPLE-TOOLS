import requests
from bs4 import BeautifulSoup
import urllib.parse

def google_dork_search(query, num_results=200):
    results = []
    pages = num_results // 10  # Menghitung jumlah halaman yang diperlukan

    for page in range(pages):
        # Encode the query for URL
        encoded_query = urllib.parse.quote(query)
        start = page * 10  # Menghitung offset untuk setiap halaman
        url = f"https://www.google.com/search?q={encoded_query}&num=10&start={start}"

        # Set headers to mimic a browser visit
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Send the request to Google
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all search result links
            results_on_page = soup.find_all('h3')
            links = [result.find_parent('a')['href'] for result in results_on_page if result.find_parent('a')]
            results.extend(links)
        else:
            print(f"\033[1;31mError: {response.status_code}")
            break  # Hentikan jika ada kesalahan

    return results[:num_results]  # Kembalikan hanya jumlah hasil yang diminta

if __name__ == "__main__":
    dork_query = input("\033[1;37mMasukkan Google Dork:\033[1;36m ")
    results = google_dork_search(dork_query)

    print("\033[1;32mHasil Pencarian:")
    for link in results:
        print(link)
