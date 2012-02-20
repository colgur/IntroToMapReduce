#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
   words = re.split(r"\W+", line)
   for word in words:
      if len(word) > 0:
         print word.lower()+"\t"+str(1)
