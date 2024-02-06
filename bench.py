import datetime
import sys
import json

name = sys.argv[1]
iters = int(sys.argv[2])

def parse_json(data):
    return json.loads(data)

def parse_config(data):
    result = {}
    for line in data.split("\n"): 
        try:
            k, v = line.strip().split(' ', 1)
            result[k] = v
        except:
            continue


    return result

def parse_config2(data):
    result = {}
    for line in data.split("\n"): 
        i = 0

        try:
            while line[i] != ' ':
                i += 1
        except:
            continue

        result[line[:i]] = line[i + 1:]

    return result

    
json_data = open(f'{name}.json', 'r').read()
raw_data = open(f'{name}.txt', 'r').read()

json_time = datetime.timedelta(seconds=0)
raw_time  = datetime.timedelta(seconds=0)
raw2_time  = datetime.timedelta(seconds=0)

for i in range(iters):
    start = datetime.datetime.now()
    j_data = parse_json(json_data)
    elapsed = datetime.datetime.now() - start
    json_time += elapsed

    start = datetime.datetime.now()
    r_data = parse_config(raw_data)
    elapsed = datetime.datetime.now() - start
    raw_time += elapsed

    start = datetime.datetime.now()
    r2_data = parse_config2(raw_data)
    elapsed = datetime.datetime.now() - start
    raw2_time += elapsed

    assert(j_data == r_data == r2_data)
    assert(len(j_data) > 2)

json_time_us = json_time.seconds * 1000. * 1000. + json_time.microseconds
json_time_iter_ms = json_time_us / iters / 1000.

raw_time_us = raw_time.seconds * 1000. * 1000. + raw_time.microseconds
raw_time_iter_ms = raw_time_us / iters / 1000.

raw2_time_us = raw2_time.seconds * 1000. * 1000. + raw2_time.microseconds
raw2_time_iter_ms = raw2_time_us / iters / 1000.

print(f"JSON:    {json_time_us / 1000. / 1000.:.2f}s ({json_time_iter_ms:.2}ms/iter)")
print(f"MANUAL:  {raw_time_us / 1000. / 1000.:.2f}s ({raw_time_iter_ms:.2}ms/iter)")
print(f"MANUAL2: {raw2_time_us / 1000. / 1000.:.2f}s ({raw2_time_iter_ms:.2}ms/iter)")
