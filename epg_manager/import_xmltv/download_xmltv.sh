echo $1 + $2
gzfile=$2
wget "$1" -O "$gzfile"
#gunzip $gzfile
