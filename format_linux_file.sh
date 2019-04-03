#!/bin/bash

for d in $(find $1)
do
  dos2unix $d
done
