#!/bin/sh
for f in sieve*
do
    `python3 ../../FeatureExtraction/retic.py --guarded -nli "$f"`
done
