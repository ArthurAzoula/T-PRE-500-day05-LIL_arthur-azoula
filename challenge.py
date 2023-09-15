import time, random

def challenge():
    startingTime = time.time()
    tab = []
    for i in range(1000000):
        tab.append(random.randint(1,10000))
    tab.sort()
    duration = time.time() - startingTime

    return duration

print(challenge())