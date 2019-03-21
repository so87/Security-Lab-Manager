#!/bin/bash
usr="simonowens157/"

for D in */; do
    cd $D
    D=${D::-1}
    target="$usr$D"
    docker build . -t "$target"
    docker push "$target"
    cd ..
done