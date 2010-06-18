#!/bin/sh
echo "setting python path."
export PYTHONPATH=$PWD/lib:$PYTHONPATH
echo "adding bin to \$PATH"
export PATH=$PATH:$PWD/bin
