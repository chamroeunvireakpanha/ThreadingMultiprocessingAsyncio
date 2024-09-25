import multiprocessing

#Function to check wether a number is prime or not
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

#Function to return a list of prime numbers from a list of numbers
def check_prime_chunk(numbers):
  return [n for n in numbers if is_prime(n)]

#Function using multiprocessing to find primes in a lists of numbers
def find_primes_in_range(numbers, chunk_size):
  with multiprocessing.Pool() as pool:
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    prime_chunks = pool.map(check_prime_chunk, chunks)
  return [prime for chunk in prime_chunks for prime in chunk]

