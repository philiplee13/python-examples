"""
POC for async requests in python
"""

import aiohttp
import asyncio
import time


async def main() -> None:
    start_time = time.time()
    BASE_URL: str = "https://httpbin.org"
    async with aiohttp.ClientSession(
        headers={"request_id": "random-request-id"}
    ) as session:
        # GET REQUEST
        await get_request(session=session, base_url=BASE_URL)
        await get_request(session=session, base_url=BASE_URL)
        await get_request(session=session, base_url=BASE_URL)
    end_time = time.time()
    print(f"Total time it took was {end_time - start_time}")


async def get_request(session: aiohttp.ClientSession, base_url: str) -> dict:
    async with session.get(f"{base_url}/get") as response:
        return await response.json()


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print(f"Total time async example took was {end_time - start_time}")
