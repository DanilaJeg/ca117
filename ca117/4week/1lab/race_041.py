#!/usr/bin/env python3

import sys

runners = {}

for line in sys.stdin: 
    try:
        runner = line.strip().split()[0] 
        times = line.strip().split()[1:] 
        best_time = int(times[0].split(":")[0]) * 60  + int(times[0].split(":")[1])
        for t in times:
            time = t.split(":") 
            time = int(time[0]) * 60 + int(time[1])
            if time < best_time: 
                best_time = time
        runners[runner] = best_time 
    except ValueError:
        pass

best = min(runners, key=runners.get) #Gets the runner with the minimum(best) time
time = str(runners[best] // 60) + ":" + str(runners[best] % 60) # Converts the seconds into this "00:00" format
print(f'{best} : {time:<04}')
