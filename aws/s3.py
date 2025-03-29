import boto3
import os
import time
import tracemalloc
import aioboto3
import asyncio


def read_file_synchrnous():
    t1 = time.perf_counter(), time.process_time()

    tracemalloc.start()
    s3 = boto3.client("s3")
    current_directory = os.getcwd()
    print(f"downloading file to {current_directory}")
    s3.download_file("test-bucket", "5gb-file", f"{current_directory}/5gb-file-froms3")
    print("now writing to source bucket")
    s3.upload_file(
        f"{current_directory}/5gb-file-froms3",
        "new-bucket",
        "5gb-from-test-bucket-sync",
    )
    t2 = time.perf_counter(), time.process_time()
    print("Total time for synchronous request was")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current} bytes")
    print(f"Peak memory usage: {peak} bytes")


async def read_file_async():
    print("downloading file async")
    t1 = time.perf_counter(), time.process_time()

    tracemalloc.start()
    current_directory = os.getcwd()
    session = aioboto3.Session()
    async with session.resource("s3") as s3:
        await s3.meta.client.download_file(
            "test-bucket",
            "5gb-file",
            f"{current_directory}/5gb-from-s3-bucket-async",
        )
    t2 = time.perf_counter(), time.process_time()
    print("Total time for async request was")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current} bytes")
    print(f"Peak memory usage: {peak} bytes")


async def main():
    read_file_synchrnous()
    await read_file_async()


if __name__ == "__main__":
    asyncio.run(main())

"""
now writing to source bucket
Total time for synchronous request was
 Real time: 78.52 seconds
 CPU time: 26.81 seconds
Current memory usage: 16091482 bytes
Peak memory usage: 44553069 bytes
downloading file async
Total time for async request was
 Real time: 28.30 seconds
 CPU time: 14.17 seconds
Current memory usage: 23576490 bytes
Peak memory usage: 110617821 bytes

so async is faster - but def uses more memory
"""
