#!/bin/bash

prog=$1
if [ -d $prog ]; then
    echo "File not found!"
    exit -1
fi

fores=$2

sudo parallel --xapply $prog ::: `shuf -i 7-541 -n $fores` ::: `seq 0 $fores`
