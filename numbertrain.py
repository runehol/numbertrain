#!/usr/bin/env python3


import subprocess
import random
import sys
import time
import argparse

def run(voice_name, low_limit, high_limit, timeout):
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

            retry = True
            while retry:
                pr = subprocess.Popen(['say', '-v', voice_name, "'%d'" % number])
                answer = input("What was said? ")

                retry = False
                if len(answer) > 0 and (answer[0] == "q" or answer[0] == "e"):
                    sys.exit()
                if len(answer) > 0 and (answer[0] == "r"):
                    retry = True
            

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
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--voice", default="Amelie", help='Select the voice for the OS X speech synth. To see the alternatives on your system, run "say -v ?" (default: Amelie)')
    parser.add_argument("--low-limit", type=int, default=0, help="Lowest number that can be generated (default: 0)")
    parser.add_argument("--high-limit", type=int, default=100, help="Highest number that can be generated (default: 100)")

    args = parser.parse_args()
    

    
    
    run(args.voice, args.low_limit, args.high_limit, 15)

if __name__ == "__main__":
    main()
