#!/usr/bin/env python

import sys
from random import randint

for arg in sys.argv:
        if "/" in arg:
                pass
        elif arg == "roll.py":
                pass
        else:
                string = arg.split("d")
                number = int(string[0]);
                print("Rolling %s..." % arg)
                arr = []
                for x in range(0,number):
                        num = randint(1,int(string[1]))
                        arr.append(num)
                        print(num)
                if len(arr) > 1:
                        print("Total is %s" % sum(arr))
                print("")
                print("")
