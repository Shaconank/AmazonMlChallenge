import os
import requests
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_image(url, folder, status_dict):
    try:
        image_name = os.path.basename(url)
        image_path = os.path.join(folder, image_name)

        if os.path.exists(image_path):
            status_dict[url] = True
            return
        
        response = requests.get(url)
        response.raise_for_status()
        with open(image_path, 'wb') as file:
            file.write(response.content)

        status_dict[url] = True

    except requests.RequestException as e:
        # print(f"Failed to download {url}. Reason: {e}")
        status_dict[url] = False

def download_images_from_csv(csv_file, folder, limit=None):
    if not os.path.exists(folder):
        os.makedirs(folder)

    df = pd.read_csv(csv_file)

    if 'image_link' not in df.columns:
        print("CSV file does not contain 'image_link' column.")
        return

    if limit is not None:
        df = df.head(limit)

    urls = df['image_link'].dropna().tolist()
    status_dict = {url: False for url in urls}

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = [executor.submit(download_image, url, folder, status_dict) for url in urls]

        for future in tqdm(as_completed(futures), total=len(futures), desc="Downloading images"):
            future.result()

    df['downloaded'] = df['image_link'].apply(lambda url: status_dict.get(url, False))
    df.to_csv('data/downloaded_train.csv', index=False)

if __name__ == "__main__":
    stage = "train"

    csv_file = f'data/{stage}.csv'
    folder = f'data/{stage}_images'
        
    limit = 10_000
    download_images_from_csv(csv_file, folder, limit)
