#!/bin/bash

bin_dir=$(dirname $0)
. $bin_dir/env.conf.sh
. $INC_DIR/py.inc.sh

sh_index_file="$DATA_DIR/sh-index-axzq.csv"
#sh_index_file="$DATA_DIR/sh-index-axzq-test.csv"
python $bin_dir/astock-ml.py $sh_index_file
