# def Sydcn(x):
#     if x % 2==0:
#         print('偶数')
#     else:
#         print('奇数')




# def Sydcn(s):
#     for x in range(2,s):
#         if s % x == 0:
#             print('不是素数')
#             break
#     else:
#         print('是素数')
# Sydcn(13)




# import random
# # 完成简单版本的4位数字的验证码
# # 密码如果错误,只能尝试3次机会.
# # 验证码要有数字和字母滴组合.
# # 验证码只能错5次.
# # 使用wxpy/互亿无线/邮箱来实现类似于短信验证码的功能.

# COUNT = 1
# COUNT1= 1
# def Sydcn():
#     global COUNT
#     global COUNT1
#     username = input('请输入账号')
#     password = input('请输入密码')
#     yanzhengma = random.randrange(1000, 9999)
#     res = int(input('验证码是:%d >>'%yanzhengma))
#     if res == yanzhengma:
#         if username == "Sydcn" and password =="123456":
#             print('Success')
#         else:
#             print('Error')
#             if COUNT !=3:
#                 COUNT += 1
#                 Sydcn()
#             else:
#                 print('尝试次数达到上限,请去客服咨询,客服电话:13838384381')
#     else:
#         print('验证码错误')
#         if COUNT1 !=5:
#             COUNT1 += 1
#             Sydcn()
#         else:
#                 print('尝试次数达到上限,请去客服咨询,客服电话:13838384381')
# Sydcn()  



# 1.
# def getPentagonalNumber(n):
#     count = 0
#     for s in range(1,n + 1):
#         num = s * (3 * s-1)/2
#         print('%d'%num,end = '\t' )
#         count += 1
#         if count % 10 ==0:
#             print('\n  ')
# getPentagonalNumber(100)



# 2.
# def sumDigits(n):
#     ge = n % 10
#     z = 0
#     for i in range(n):
#         bai = n // (10 * (10 ** i)) % 10
#         z += bai
#     sum = z + ge
#     print('整数之和为:%d'%sum)
# sumDigits(12581)




# 3.
# def display(num1,num2,num3):
#     list = [num1,num2,num3]
#     s = sorted(list)
#     print("给三位数字排序得{}".format(s))
# if __name__ == "__main__":
#     a,b,c = map(int,input("请输入三个数字："))
#     display(a,b,c)




# 5.
# def printChars():
#     for i in range(73,91):
#         print(chr(i),end=" ")
#         if i% 10 == 0:
#             print("\n")
# printChars()



# 6.
# def numberOfDaysInAYear(year):
#     for i in range(year,year+11):
#         if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#             print("{}年有366天".format(i))
#         else:
#             print("{}年有365天".format(i))
# numberOfDaysInAYear(2010)




# 7.
# def distance(x1,x2,y1,y2):
#     dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     print("这两个点的距离是：%f"%dis)
# distance(1,4,4,2)




# 9.
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("时间:", localtime)
# main()



# 10.
# import random
# def touzi():
#     a=random.choice([1,2,3,4,5,6])
#     b=random.choice([1,2,3,4,5,6])
#     if a+b==2 or  a+b==3 or a+b==12:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('滚！')
#     elif a+b==7 or a+b==11:
#         print('%d + %d = %d' %(a,b,a+b))
#         print('行吧...')
#     else:
#         print('%d + %d = %d' %(a,b,a+b))
#         c=random.choice([1,2,3,4,5,6])
#         d=random.choice([1,2,3,4,5,6])
#         if c+d==7:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('滚！')
#         elif c+d==a+b:
#             print('%d + %d = %d' %(c,d,c+d))
#             print('行吧...')
# touzi()











































































































































