#!/usr/bin/env bash

for iters in 32 128 256 512; do 
  for f in data_4096 data_16384 data_65536; do 
      echo --- PYTHON $f $iters ITERS --- >> results; 
      python3 bench.py $f $iters >> results; 
      echo --- RUST $f $iters ITERS --- >> results; 
      cargo run -r -- $f $iters  >> results; 
  done
done
