rm log.txt
for f in nbody*
do
	echo "$f"
    echo "$f" >> log.txt
    retic --guarded "$f" >> log.txt    
done

