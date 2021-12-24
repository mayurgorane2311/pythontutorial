# #compare which loop is fast by using time module
import time
# #Ex1
# initial = time.time()
# k = 0
# while(k<45):
#     print("this is mayur bhai")
#     time.sleep(3)                           # time.sleep is sleep program as per required time here for 3 sec
#     k += 1
# print("while loop run in",time.time()-initial,"seconds")
#
# initial2 = time.time()
# for i in range(45):
#     print("this is harry bhai")
# print("while loop run in", time.time() - initial, "seconds")



#other function of time see
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

