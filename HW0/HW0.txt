mkdir pronto
cd pronto
touch README.txt
Echo "these are the pronto data from 2015">README.txt
mkdir data
cd data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head *.csv
