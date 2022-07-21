# file uploader

import requests

url = f"http://{sys.argv[1]}"  # Change for url or use f-string
r = requests.get(url, allow_redirects=True)
open("file.ext", "wb").write(r.content)
