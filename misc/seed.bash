#!/usr/bin/env bash

if [ -f report.db ]
then
    rm -f report.db
fi

for i in {1..10}
do
   labzoo-run misc/example.yaml report.db localhost
done
