import os
import collections
from pprint import pprint

download_path = os.path.join(
    os.path.expanduser("~"),
    "downloads"
)

file_mappings = collections.defaultdict()
for filename in os.listdir(download_path):
    file_type = filename.split(".")[-1]
    file_mappings.setdefault(file_type, []).append(filename)

#pprint(file_mappings)

for folder_name, folder_items in file_mappings.items():
    folder_path = os.path.join(download_path, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    for folder_item in folder_items:
        source = os.path.join(download_path, folder_item)
        destination = os.path.join(folder_path, folder_item)
        print(f'Moving {source} to {destination}')