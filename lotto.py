# import random

# #로또번호는 1~46, 총6개 당첨번호
# today = []

# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))

# print("오늘의 추첨번호는 " 
# + str(today[0]) + ", "
# + str(today[1]) + ", "
# + str(today[2]) + ", "
# + str(today[3]) + ", "
# + str(today[4]) + ", "
# + str(today[5]) + "입니다")


#


# import random

# # #로또번호는 1~46, 총6개 당첨번호
# today = []

# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))

# print("오늘의 추첨번호는 " 
# + str(today[0]) + ", "
# + str(today[1]) + ", "
# + str(today[2]) + ", "
# + str(today[3]) + ", "
# + str(today[4]) + ", "
# + str(today[5]) + "입니다")
# start=0
# while start<6:
#     today.append(random.randrange(1,46,1))
#     start=start+1

import random

# #로또번호는 1~46, 총6개 당첨번호
# today = []

# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))
# today.append(random.randrange(1,46,1))


today=random.sample(range(1,47),6)

print("오늘의 추첨번호는 " 
+ str(today[0]) + ", "
+ str(today[1]) + ", "
+ str(today[2]) + ", "
+ str(today[3]) + ", "
+ str(today[4]) + ", "
+ str(today[5]) + "입니다")
