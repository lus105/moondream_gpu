import os
import urllib.request
import gzip
import shutil

# Define URLs and file paths
files = [
    {
        "url": "https://huggingface.co/vikhyatk/moondream2/resolve/main/model.safetensors",
        "path": "models/model.safetensors"
    },
    {
        "url": "https://huggingface.co/vikhyatk/moondream2/resolve/onnx/moondream-2b-int8.mf.gz",
        "path": "models/moondream-2b-int8.mf.gz",
        "unzip_to": "models/moondream-2b-int8.mf"
    }
]

# Download function
def download(url, path):
    if os.path.exists(path):
        print(f"Skipping {os.path.basename(path)} — already exists.")
        return
    print(f"Downloading {os.path.basename(path)}...")
    urllib.request.urlretrieve(url, path)
    print(f"Downloaded to {path}")

# Extract gzip file
def extract_gz(gz_path, out_path):
    if os.path.exists(out_path):
        print(f"Skipping extraction — {os.path.basename(out_path)} already exists.")
        return
    print(f"Extracting {os.path.basename(gz_path)}...")
    with gzip.open(gz_path, 'rb') as f_in, open(out_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    os.remove(gz_path)
    print(f"Extracted to {out_path} and deleted {os.path.basename(gz_path)}")

# Run download and extract
for f in files:
    download(f["url"], f["path"])
    if "unzip_to" in f:
        extract_gz(f["path"], f["unzip_to"])

print("\nAll done. Files saved in models/")