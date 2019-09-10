# username=input('请输入用户名：')
# password=input('请输入密码：')
# if username =='admin' and password =='123456789':
#     print('身份验证成功！')
# else:
#     print('身份验证失败！')


# s=input('请输入成绩：')
# if '60'<=s<'70' :
#     print('成绩为C！')
# elif '70'<=s<'80' :
#     print('成绩为B！')
# else :
#     print('成绩为A！')


# username=input('请输入用户名：')
# u=username[0]
# if u in '!@#$%^&*()':
#     print('用户名不能以特使字符开头！')
# else :
#     pass


# x=float(input('x='))
# if x>1:
#     print(3*x-5)
# elif -1<=x<=1:
#     print(x+2)
# else :
#     print(x+3)


# a=float(input('请输入一个数字：'))
# b=input('输入一个运算符(+、-、*、/)：')
# c=float(input('请输入另一个数字：'))
# if  b=='+'   : 
#     print('%a+c')
# elif    b=='-':
#     print('%a-c')
# elif    b=='*':
#     print('%a*c')
# else:
#     print('%a/c')


# import numpy as nu
# res = np.random.choice(['剪刀','石头','布'])
# print(res)


# number=int(input('请输入一个五位数：'))
# a = int(number[0])
# b = int(number[1])
# c = int(number[2])
# d = int(number[3])
# e = int(number[4])
# if a==e and b==d :
#     print('该数字为回文数！')
# else:
#     print('该数字不是回文数！')

# import time
# import pygame
# file=r'D:\CloudMusic\薛之谦-慢半拍.mp3'
# pygame.mixer.init()
# print('播放音乐1')
# track = pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer,music.stop()


# sum1 = 0
# sum2 = 0
# for x in range(1,101):
#     if x%2==0:
#         sum2 += x
#     else:
#         sum1 += x
# print(sum1,sum2 )


# import time
# start = time.time()
# sum_= 0
# for i in range(1000000):
#     sum_ += i
# end = time.time()
# print(end - start)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(j,i,j*i),end='\t')
#     print(end='\n')


# from math import sqrt

# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)


# a = 'abcdefg'
# i = 0
# while i <len(a):
#     print(a[i])
#     i += 1

# 1.
# import math
# a=float(input('请输入第一个数字：'))
# b=float(input('请输入第二个数字：'))
# c=float(input('请输入第三个数字：'))
# if (b**2-4*a*c)>0:
#     r1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
#     r2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
#     print('r1=%.6f,r2=%.6f'%(r1,r2))
# elif (b**2-4*a*c)==0:
#     r1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
#     r2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
#     print('r1=%.6f'%r1)
# else:
#     print('The equation has no real roots')



# 2.
# import numpy
# num1 =numpy.random.choice(range(0,100))
# num2 =numpy.random.choice(range(0,100))
# num3 =float(input('请输入一个数字'))
# if num3 == num1+num2:
#     print('行吧...')
# else:
#     print('滚！！！')



3.
num1=int(input('输入一个数字看看今天周几：'))
num2=int(input('你还想看哪天：'))

if num1==0:
    today='Sunday'
elif num1==1:
    today='Monday'
elif num1==2:
    today='Tuesday'
elif num1==3:
    today='Wednesday'
elif num1==4:
    today='Thursday'
elif num1==5:
    today='Friday'
elif num1==6:
    today='Saterday'
if num2>7:
    print((num1+num2)%7)






# 4.
# def count(a,b,c):
#   num = [a,b,c]
#   num.sort()
#   print(num)
# def start():
#   a = int(input('输入第一个整数：'))
#   b = int(input('输入第二个整数：'))
#   c = int(input('输入第三个整数：'))
#   count(a,b,c)
# start()



# 5.
# def shop(weight1,weight2,price1,price2):
#   package1 = weight1 / price1
#   package2 = weight2 / price2
#   if package1 > package2:
#       print('package1 has the better price')
#   else:
#       print('package2 has the better price')
# def start():
#   weight1 = float(input('第一种重量是:')) 
#   price1 = float(input('第一种价格是:'))
#   weight2 = float(input('第二种重量是:'))
#   price2 = float(input('第二种价格是:'))
#   shop(weight1,weight2,price1,price2) 
# start()  



# 6.

# import calendar 
# def num(year,month):
#   print(calendar.monthrange(year, month)[1])
# def start():
#   year = int(input('Enter year: ')) 
#   month = int(input('Enter month number: '))
#   num(year,month)
# start()




# 7.

# import random
# x = int(input('请输入你的猜测（1为正，2为反）：'))
# a = random.randint(1,2)
# if x == a:
#     print('你猜对了')
# else:
#     print('你猜错了')




# 8.
# import random
# U_res = int(input('0:石头,1:剪刀,2:布>>>'))
# C_res = random.randint(0,2)
# if C_res == U_res:
#     print('平局')
# else:
#     if C_res == 0 and U_res == 1:
#         print('电脑赢了 ')
#     elif C_res == 1 and U_res == 2:
#         print('电脑赢了 ')
#     elif C_res == 2 and U_res == 0:
#         print('电脑赢了 ')
#     else:
#         print('你赢了 ')





# 9.
# def main(year,m,d):
#     a = ['周六','周日','周一','周二','周三','周四','周五']
#     if m == 1:
#         m = 13
#         year = year - 1
#     if m ==2:
#         m = 14
#         year = year - 1
#     h = int(d+((26*(m+1))//10)+(year%100)+((year%100)/4)+((year//100)/4)+5*year//100)%7
#     day = a[h]
#     print('那一天是一周中的:%s' %day)
# def Start():
#     year = int(input('输入哪一年:'))
#     m = int(input('输入月份1-12:'))
#     d = int(input('输入月份第几天1-31:'))
#     main(year,m,d)
# Start()




# 10.
# def chou():
#     import numpy as np
#     daxiao=np.random.choice(['A','2','3','4','5','6','7','8','9','10','J','Q','K'])
#     huase=np.random.choice(['梅花','红桃','方块','黑桃'])
#     print('你选择的牌是  %s , %s'%(huase,daxiao))
# def Start():
#     a = input("是否决定抽牌y/n:")
#     if a == 'y':
#         chou()
#     else:
#         pass
# Start()





# 11.
# num = input('输入一个三位数：')
# if int(num[0])==int(num[2]):
#     print('是回文数')
# else:
#     print("不是回文数")




# 12.
# a,b,c = map(float,input('enter three edge:').split(','))
# if a+b>c and a+c>b and b+c>a:
#     L = a+b+c
#     print("其周长为",L)
# else:
#     print("不是三角形三条边") 








#  2.
# money = 10000
# sum1 = 0
# for i in range(1,14):
#     money = money * 0.05 + money
#     if i ==10:
#          print('十年之后的学费：%.2f'%money)
#     if i >= 10: 
#         sum1 += money
# print('十年后大学四年的总学费为：%.2f'%sum1)




# 4.
# geshu = 0
# for i in range(100,1001):
#     if i%5 == 0 and i%6 == 0:
#         print(i,end=' ')
#         geshu += 1
#         if geshu % 10 == 0:
#             print('\n')




# 5.
# n = 0
# m = 0
# while n**2 <= 12000:
#     n += 1
# print('n的平方大于12000的最小整数n为：%d'%n)

# while m**3 < 12000:
#     m += 1
# print('n的立方大于12000的最大整数n为：%d'%(m-1))




# 6.
# sum1 = 0
# sum2 = 0
# for i in range(1,50001):
#     sum1 += 1/i
#     i += 1
# print('从左向右计算为：',sum1)
# for i in range(50000,0,-1):
#     sum2 += 1/i
#     i -= 1
# print('从右向左计算为：',sum2)




#8.
# sum1 = 0
# for i in range(3,100,2):
#     sum1 += (i-2)/i
# print('数列的和为：',sum1) 




#9.
# pi = 0
# i = int(input('输入i的值：'))
# for j in range(1,i+1):
#     pi += 4 * ((-1)**(1+j)/(2*j-1))
# print('π的值为：%f'%pi)





#11.
# list1 = []
# for i in range(1,8):
#     for j in range(1,8):
#             if i != j and sorted([i,j]) not in list1:
#                 list1.append([i,j])
# print('所有可能的组合为：',list1)
# print('组合总个数为：',len(list1))





























