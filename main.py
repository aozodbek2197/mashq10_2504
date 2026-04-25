import threading
import time
from typing import List

class Downloader:
    def __init__(self, urls: List[str]) -> None:
        self.urls = urls

    def download(self, url: str) -> None:
        print(f"Downloading {url}...")
        time.sleep(1)
        print(f"Finished {url}")

    def run(self) -> None:
        threads = []

        for url in self.urls:
            thread = threading.Thread(target=self.download, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


if __name__ == "__main__":
    urls = ["a.com", "b.com", "c.com"]
    d = Downloader(urls)
    d.run()
