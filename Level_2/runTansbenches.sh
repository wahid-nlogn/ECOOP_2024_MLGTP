rm log_transient_sieve.txt
for f in sieve*
do
	echo "$f"
    echo "$f" >> log_transient_sieve.txt
    retic --transient "$f" >> log_transient_sieve.txt    
done

