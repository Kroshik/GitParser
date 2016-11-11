#!bin/bash
for item in $(find | grep -E '*\.c')
do
python3 parse_fun.py $item
done

