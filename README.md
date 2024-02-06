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
JSON:    11.24s (21.96ms/iter)
MANUAL:  13.37s (26.10ms/iter)
MANUAL2: 49.54s (96.76ms/iter)
--- RUST data_65536 512 ITERS ---
JSON:    7.50s (14.47265625ms/iter)
MANUAL:  7.50s (14.654296875ms/iter)
```
