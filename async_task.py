import asyncio

#Function to write data to a file applying async function
async def async_write_to_file(filename, data, duration):
    await asyncio.sleep(duration)
    try:
        with open(filename, 'w') as file:
            file.write("\n".join(map(str, data)))
        print(f"Finished writing to {filename}")
    except Exception as e:
        print(f"Error writing to {filename}: {e}")

#Function to run multiple async tasks concurrently
async def run_async_tasks(prime_data):
    chunk_size = len(prime_data) // 2
    await asyncio.gather(
        async_write_to_file("primes.txt", prime_data[:chunk_size], 2),
        async_write_to_file("primes2.txt", prime_data[chunk_size:], 4)
    )

