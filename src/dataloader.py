# install kagglehub if not installed
# pip install kagglehub

import kagglehub
import os
import shutil

def download_and_copy_file(dataset, filename):
    path = kagglehub.dataset_download(dataset)
    print(f"Path to dataset files: {path}")
    data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_folder, exist_ok=True)
    src_file = os.path.join(path, filename)
    dst_file = os.path.join(data_folder, filename)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)
        print(f"{filename} copied to: {os.path.abspath(dst_file)}")
    else:
        print(f"{filename} not found in the downloaded dataset.")

# Download stocks.csv
download_and_copy_file("bestagi/indonesia-stock-marketidx-price-data", "stocks.csv")

# Download indonesian-news-dataset.csv
download_and_copy_file("ibamibrahim/indonesian-news-title", "indonesian-news-title.csv")


# too big file
# Download DaftarSaham.csv
# download_and_copy_file("muamkh/ihsgstockdata", "DaftarSaham.csv")
# Download data.csv (news dataset)
# download_and_copy_file("iqbalmaulana/indonesian-news-dataset", "data.csv")