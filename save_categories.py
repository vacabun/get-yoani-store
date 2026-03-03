import requests
import glob

start = 0
end = 400

base_url = "https://storage.googleapis.com/yoani-buppan-prod/compressed/categories/icons/"
# base_url = "https://storage.googleapis.com/yoani-buppan-prod/compressed/products/icons/"

image_extensions = [
    ".jpg", ".JPG", 
    ".jpeg", ".JPEG",
    ".png", ".PNG",
    # ".webp",
    # ".gif",
    # ".svg",
    # ".avif"
]

def get_file(base_url, file_name):
    try:
        print(f"Check {file_name}")
        url = f"{base_url}{file_name}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            with open(f"categories/{file_name}", "wb") as f:
                f.write(r.content)
            print(f"Downloaded {file_name}")
            return True
    except Exception as e:
        print(f"Error at {file_name}: {e}")
    return False

for i in range(start, end + 1):

    if glob.glob(f"categories/{i}.*"):
        continue
    for image_type in image_extensions:
        if get_file(base_url, f"{i}{image_type}"):
            continue
