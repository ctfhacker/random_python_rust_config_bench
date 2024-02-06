# Benchmarking Python and Rust json/config options

## Generate test data

```
python3 gen.py
```

## Run benchmarks

```
./run.sh
```

## Results

```
--- PYTHON data_65536 512 ITERS ---
JSON:    11.08s (2.2e+01ms/iter)
MANUAL:  13.05s (2.5e+01ms/iter)
MANUAL2: 49.04s (9.6e+01ms/iter)
--- RUST data_65536 512 ITERS ---
JSON:    7.42s (14.333984375ms/iter)
MANUAL:  7.42s (14.486328125ms/iter)
```
