import time

import requests
from concurrent.futures import ThreadPoolExecutor
import threading

thread_local = threading.local()


def main():
    synchronous()
    print("moving onto threaded")
    threaded()


def synchronous():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.perf_counter()
    download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Synchronous: Downloaded {len(sites)} sites in {duration} seconds")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


def download_site(url, session):
    with session.get(url) as response:
        pass


def threaded():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.perf_counter()
    threading_download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Threading: Downloaded {len(sites)} sites in {duration} seconds")


def threading_download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:  # how many threads you want
        # if the question becomes how many threads you need - you need to do some testing to see what works
        # also worry about thread safety and how to join "data"
        executor.map(threading_download_site, sites)


def threading_download_site(url):
    session = get_session_for_thread()
    with session.get(url) as response:
        pass


def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


if __name__ == "__main__":
    main()
