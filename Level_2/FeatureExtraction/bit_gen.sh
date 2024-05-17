
#rm log.txt
rm sor_bits.txt
for f in SOR*
do
	python3 ../../FeatureExtraction/retic.py -bsg "$f"
    #python3 ../retic.py >> sor_bits.txt    
done
