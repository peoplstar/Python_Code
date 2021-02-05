from random import *

cnt = 0
check = "O"
for i in range(0,50):
    customer = randrange(5,51)
    if 5 <= customer <= 15:
        check = "O"
        cnt += 1
    else:
        check = " "
    
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, i+1, customer))
print("총 탑승 승객 : {0}분".format(cnt))