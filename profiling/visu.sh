#!/bin/bash

function run_python
{
    python -m cProfile -o "temp.cprof" $(1)
}

function calltree
{
    pyprof2calltree -k -i "temp.cprof"
}


run_python
calltree
