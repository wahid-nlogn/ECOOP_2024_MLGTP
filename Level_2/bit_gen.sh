#rm log.txt
rm sieve_bits.txt
for f in sieve*
do
	echo "$f"
    echo "$f" >> sieve_bits.txt
    grep '^def ' "$f" > tmp.log
    python3 feature_gen.py >> sieve_bits.txt    
done

