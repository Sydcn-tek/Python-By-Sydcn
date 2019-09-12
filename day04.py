# 1.
# def main(a,b,c,d):
#     s=[a,b,c,d]
#     y=sorted(s)
#     best=y[-1]
#     print(best)
# for i in range(s):
#     if   i >= best - 10:
#         print('A级')
#     elif i >= best - 20:
#         print('B级')
#     elif i >= best - 30:
#         print('C级')
#     elif i >= best - 40:
#         print('D级')
#     else:
#         print('F级')
# main(40,55,70,58)


#2：
#a = [1,2,3,4,0,9,8,7]
#b = a[::-1]
#print(b)






#3:
#def occurso(str1):
#    str3 = str1
#    str2 = []
#    for i in str1:
#        if i not in str2 :
#            str2.append(i)
#
#    for i in range(len(str2)):
#        num1 = 0
#        for j in range(len(str3)):
#            if str3[j] == str2[i]:
#                num1 += 1
#            else:
#                num1 = num1
#        print('有这么多个数数%d'%num1)
#occurso([1,2,3,4,5,4,3,5,3,2,4,2])




#4:
#def average(list):
#    pinjun = sum(list)/(len(list)*1.0)
#    return pinjun
#num1 = 0
#num2 = 0
#def fenshu(list_):
#    pinjun = average(list_)
#    for i in range(len(list_)):
#        
#        global num1
#        global num2
#        if list_[i] > pinjun: 
#            num1 += 1
#        elif list_[i] < pinjun:
#            num2 += 1
#        else:
#            pass
#    print(num1)
#    print(num2)
#    print(pinjun)
#fenshu([2,4,2,4,8])




#5：

#import numpy
#def suiji():
#    a = numpy.random.choice(range(1000))
#    return a
#for i in range(1000):
#    str1 = [suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji(),suiji()]
#    print(str1)




#6：
#def indexOFSmallestElement(lst):
#    lst1 = lst
#    lst2 = sorted(lst)
#    zuixiao = lst2[0]
#
#    for i in range(len(lst1)):
#        if lst1[i] == zuixiao:
#            print('最小元素的下标再第几个呢，就是这里>>%d'%(i+1))
#            
#indexOFSmallestElement([3,4,2,7,5,4,1,4,3,4])




















































































