#!/usr/bin/env bash

./mapper.py < input.txt | sort | ./reducer.py
