from tqdm import tqdm
import requests


url="https://download.winzip.com/gl/nkln/winzip24-downwz.exe"

buffer_size=1024
response = requests.get(url, stream=True, verify=False)

file_size = int(response.headers.get("Content-Length",0))

filename = url.split("/")[-1]

progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    for data in progress:
        # write data read to the file
        f.write(data)
        # update the progress bar manually
        progress.update(len(data))
