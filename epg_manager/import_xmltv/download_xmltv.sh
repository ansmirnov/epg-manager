gzfile=$2.gz
wget "$1" -O "$gzfile"
gunzip $gzfile
