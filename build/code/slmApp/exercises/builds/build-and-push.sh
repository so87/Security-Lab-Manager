#!/bin/bash
usr="simonowens157/"

for D in */; do
    cd $D
    echo "" > root.txt
    D=${D::-1}
    target="$usr$D:v1.0"
    docker build . -t "$target"
    docker push "$target"
    cd ..
done