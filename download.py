import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

def download_file(url, save_path, log_file, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, stream=True, timeout=10)
            if response.status_code == 200:
                with open(save_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                print(f"Downloaded: {url} -> {save_path}")
                with open(log_file, 'a') as log:
                    log.write(f"SUCCESS: {url}\n")
                return True
            else:
                print(f"Failed to download: {url}, Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    with open(log_file, 'a') as log:
        log.write(f"FAILED: {url}\n")
    return False

def load_failed_logs(log_file):
    if not os.path.exists(log_file):
        return []
    with open(log_file, 'r') as log:
        return [line.split(' ', 1)[1].strip() for line in log if line.startswith("FAILED")] 

def download_website(base_url, output_folder, log_file):
    visited_urls = set()
    failed_downloads = load_failed_logs(log_file)

    def scrape_directory(url, local_path):
        if url in visited_urls:
            return
        visited_urls.add(url)

        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"Failed to access: {url}")
                return

            os.makedirs(local_path, exist_ok=True)
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(url, href)
                parsed_url = urlparse(full_url)

                if parsed_url.path.endswith('/'):
                    scrape_directory(full_url, os.path.join(local_path, os.path.basename(href.rstrip('/'))))
                else:
                    file_name = os.path.basename(parsed_url.path)
                    save_path = os.path.join(local_path, file_name)
                    if full_url not in failed_downloads:
                        download_file(full_url, save_path, log_file)

        except Exception as e:
            print(f"Error accessing {url}: {e}")

    scrape_directory(base_url, output_folder)

if __name__ == "__main__":
    base_url = input("Enter the base URL of the website: ").strip()
    output_folder = input("Enter the output folder path on your local machine: ").strip()
    remote_upload_folder = input("Enter the remote SMB network folder path (or leave blank to skip upload): ").strip()

    log_file = os.path.join(output_folder, "download_log.txt")

    download_website(base_url, output_folder, log_file)

    if remote_upload_folder:
        try:
            import shutil
            shutil.copytree(output_folder, remote_upload_folder, dirs_exist_ok=True)
            print(f"Uploaded to remote folder: {remote_upload_folder}")
        except Exception as e:
            print(f"Error uploading to remote folder: {e}")

    print("Download completed.")
    time.sleep(3)
    exit()
