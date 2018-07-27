# class Cal():
#     def __init__(self, value):
#         self.value = value
    
#     def result(self):
#         print(self.value)

#     def add(self, input_value):
#         self.value += input_value
#         #self.value = self.value + input_value

#     def sub(self, input_value):
#         self.value -= input_value

#     def mul(self, input_value):
#         self.value *= input_value

#     def div(self, input_value):
#         self.value /= input_value
# #예외처리



# #상속
# class SafeCal(Cal):
#     def __init__(self, value):
#         self.value = value
#     def div(self, input_value):
#         if (input_value == 0):
#             self.value = 0
#         else:
#             self.value /=input_value


# cal1 = Cal(0)
# cal1.add(10)
# cal1.result()
# cal1.div(0)
# cal1.result()

#0으로 나누면 무한대이므로 에러일때, 0의초기화할 경우,
# cal2 = SafeCal(0)
# cal2.add(10)
# cal2.result()
# cal2.div(0)
# cal2.result()

# #예외처리
# class Cal():
#     def __init__(self, value):
#         self.value = value
    
#     def result(self):
#         print(self.value)

#     def add(self, input_value):
#         self.value += input_value
#         #self.value = self.value + input_value

#     def sub(self, input_value):
#         self.value -= input_value

#     def mul(self, input_value):
#         self.value *= input_value

#     def div(self, input_value):
#         try:
#             self.value /= input_value
#         #except expression as identifier:
#         except ZeroDivisionError: 
#             print("0으로 나눌수 없음")
#         else: 
#             print("알수없는 오류임")  


# cal1 = Cal(0)
# cal1.add(10)
# cal1.result()
# cal1.div(0)
# cal1.result()

class Cal():
    def __init__(self, value):
        self.value = value
    
    def result(self):
        print(self.value)

    def add(self, input_value):
        self.value += input_value
        #self.value = self.value + input_value

    def sub(self, input_value):
        self.value -= input_value

    def mul(self, input_value):
        self.value *= input_value

    def div(self, input_value):
        try:
            # self.value /= input_value
            self.value /= "DIV"
        #except expression as identifier:
        except:
        #except ZEROerror:
            print("0으로 나눌수 없음")
        finally: 
            print("나누기 실행완료")
        

cal1 = Cal(0)
cal1.add(10)
cal1.result()
cal1.div(0)
cal1.result()        