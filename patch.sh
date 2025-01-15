#!/bin/bash

# See https://github.com/cosmicds/radwave-in-motion/pull/19 for a description of why this is needed

filepath=node_modules/@wwtelescope/engine/src/index.js
if ! test -f ${filepath}; then
    filepath="../${filepath}"
fi

line=$(grep -n "renderContext.targetCamera.zoom = this.renderContext.viewCamera.zoom = Math" $filepath | cut -d : -f 1)
if [[ ! -z ${line} ]]
then
    sed -i.bak "${line}d" ${filepath}
    rm ${filepath}.bak
fi
