import time
for i in range(21):
    print(i)
    time.sleep(2)
    if i %5 ==0:
        print("\a")