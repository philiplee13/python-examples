import requests
import asyncio
import time
import aiohttp


async def main() -> None:
    url = "https://httpbin.org/get"
    synchronous(url=url, request_id="random-request-id")
    await async_requests(url=url, request_id="random-request-id")


def synchronous(url: str, request_id: str):
    t1 = time.perf_counter(), time.process_time()
    for i in range(10):
        response = requests.get(url=url, headers={"request_id": request_id})
    t2 = time.perf_counter(), time.process_time()
    print("Total time for synchronous request was")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")


async def async_requests(url: str, request_id: str):
    start = time.time()
    t1 = time.perf_counter(), time.process_time()
    tasks = []
    async with aiohttp.ClientSession(headers={"request_id": request_id}) as session:
        for i in range(10):
            tasks.append(get_request(session=session, base_url=url))

        await asyncio.gather(*tasks)
    t2 = time.perf_counter(), time.process_time()
    print("Total time for async took was")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")


async def get_request(session: aiohttp.ClientSession, base_url: str) -> dict:
    async with session.get(base_url) as response:
        return await response.json()


if __name__ == "__main__":
    asyncio.run(main())
