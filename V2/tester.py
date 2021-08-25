import print_visual
import random

arr_temp = [[0 for i in range(2)] for j in range(18)]
m = 23
def counters():
    for i in range(1,8,1):
        print("tray: " + str(i))
        for b in range(1, 19, 1):
            print("Battery: " + str(b) + "unit: " + str(i))
    v = m%18
    w = (m // 18) +1
    print(v)
    print(w)

def fill():
    for batteries in range(18):
        for n in range(2):
            arr_temp[batteries][0] = str(random.randint(100, 900))
            soc_t = random.randint(0, 100)
            if (soc_t < 100 and soc_t > 9):
                arr_temp[batteries][1] = str(soc_t) + "%"
            elif soc_t < 10:
                arr_temp[batteries][1] = " " + str(soc_t) + "%"
            else:
                arr_temp[batteries][1] = str(soc_t)

# fill()
# print_visual.Output_multiple(2, arr_temp)
counters()
