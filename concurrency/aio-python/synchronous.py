"""
Synchronous requests time
"""

import requests
import time


def main() -> None:
    start_time = time.time()
    send_get_requests(
        url="https://httpbin.org/get", request_id="random-http-string-id-1"
    )
    send_get_requests(
        url="https://httpbin.org/get", request_id="random-http-string-id-2"
    )
    send_get_requests(
        url="https://httpbin.org/get", request_id="random-http-string-id-3"
    )
    end_time = time.time()
    print(f"Total time it took was {end_time - start_time}")


def send_get_requests(url: str, request_id: str):
    response = requests.get(url=url, headers={"request_id": request_id})
    return response.json()


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Total time for synchrnous example was {end_time - start_time}")
