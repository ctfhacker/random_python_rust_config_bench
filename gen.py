import random
import string
import json

def rand_str(max_length: int):
    length = random.randint(1, max_length)
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_file(entries: int):
    result = {}
    for _ in range(entries):
        result[rand_str(64)] = rand_str(64)

    return result

for len in [64, 1024, 1024 * 4, 1024 * 16, 1024 * 64, 1024 * 1024, 8 * 1024 * 1024]:
    data = generate_file(len)
    with open(f"data_{len}.json", 'w') as f:
        f.write(json.dumps(data))

    with open(f"data_{len}.txt", 'w') as f:
        for (k, v) in data.items():
            f.write(f"{k} {v}\n")
