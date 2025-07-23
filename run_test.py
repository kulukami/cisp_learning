#!python3
import os
import json
import random

total_case = []
for each_json in os.listdir("exam_set"):
    with open(f"exam_set/{each_json}","r") as f:
        p = json.load(f)
    total_case.append(p)

random_100 = random.sample(total_case, 100)

rpmap = {
    1:"A",
    2:"B",
    3:"C",
    4:"D",
}

c = 0
failed = 0
success = 0
tested = 0
for each_q in random_100:
    c+=1
    print(f"{c}.{each_q["q"]}")
    print(f"->1.{each_q["A"]}")
    print(f"->2.{each_q["B"]}")
    print(f"->3.{each_q["C"]}")
    print(f"->4.{each_q["D"]}")
    f = False
    while True:
        try:
            t = int(input("Answer:1/2/3/4:"))
            if t <= 4 and t>= 1:
                break
        except Exception as e:
            print(f"error with {e}, input must be 1/2/3/4")
            continue
        except KeyboardInterrupt:
            f = True
            break
    if f:
        break

    tested += 1
    if rpmap[t] != each_q["result"]:
        failed += 1
        print(f"failed, answer is {each_q["result"]}")
        if len(each_q["reason"]) >=2:
            print(f"reason: {each_q["reason"]}")
    else:
        success += 1
        print("success")

print(f"\n\nTotal Score:{success/tested} out of {tested}")

if tested == 100:
    print(f"\n\nAll 100 done.")


