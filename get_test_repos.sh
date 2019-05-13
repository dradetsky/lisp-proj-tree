#!/bin/bash

repos=(
    git@github.com:Shinmera/chirp.git
    git@github.com:fukamachi/woo.git
    git@github.com:eudoxia0/cl-yaml.git
    git@github.com:fukamachi/clack.git
    git@github.com:melisgl/mgl.git
)

if [ -d data ] ; then
    echo data exists
fi

pushd data

for x in ${repos[*]} ; do
    echo $x
    git clone $x
done

popd
