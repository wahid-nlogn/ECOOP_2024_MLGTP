#!/bin/sh
for f in sieve*
do
    `python3 ../../FeatureExtraction/retic.py --transient -nli "$f"`
done
