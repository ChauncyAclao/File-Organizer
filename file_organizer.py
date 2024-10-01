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

pprint(file_mappings)

