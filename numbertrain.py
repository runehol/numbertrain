#!/usr/bin/env python3


import subprocess
import random
import sys
import time

def main(args=sys.argv):
    voice_name = 'Amelie'
    low_limit = 0
    high_limit = 100
    timeout = 15
    rand = random.SystemRandom()
    
    suspend_list = []
    q_count = 0
    try:
        while True:

            number = 0
            wrong_count = 0
            if suspend_list and suspend_list[0][0] <= q_count:
                number = suspend_list[0][1]
                wrong_count = suspend_list[0][2]

                suspend_list = suspend_list[1:]
            else:
                number = random.randrange(low_limit, high_limit)
                wrong_count = 0

            pr = subprocess.Popen(['say', '-v', voice_name, "%d" % number])

            answer = input("What was said? ")
            if len(answer) > 0 and (answer[0] == "q" or answer[0] == "e"):
                break

            try:
                num_answer = int(answer)
            except:
                num_answer = -1241252135
            if num_answer == number:
                print("Correct\n")
            else:
                wrong_count += 1
                print("Wrong, should have been %d. Wrong %d time(s).\n" % (number, wrong_count))
                time.sleep(1)

                suspend_list.append( (q_count + timeout, number, wrong_count) )
            q_count += 1
    finally:
        pass
    


if __name__ == "__main__":
    main()
