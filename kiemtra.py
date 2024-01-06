# def hamchan(sochan):
#     if sochan %2 == 0:
#         print(f'{sochan} is an even number')
#     else :
#         print(f'{sochan}is not an even number')
# hamchan(7)

# def cal_area(r):
#     if type(r) == int :
#         import math
#         pi = math.pi
#         S= r**2*pi
#         print(S)
# cal_area(8)

# def reverse_str(str):
#     print(''.join(str[-1::-1]))
# reverse_str('BINH')

# def reverse_str(str):
#     a_list =[]
#     for i in str :
#         a_list.append(i)
#     a_list.reverse()
#     print(''.join(a_list))
# reverse_str('BINH')

# def is_palindrome(so):
#     if ''.join(so[-1::-1]) == so :
#         print('this is a palindrome')
#     else :
#         print('it is not a palindrome')
# is_palindrome('anna')


# phan 2
# def giaithua(so):
#     sogt = 1
#     for i in range (1,so+1): 
#         sogt = sogt* i
#     print(sogt)
# giaithua(5)

# def hamso(so):
#     for i in range(len(so)):
#         for j in range (1,len(so)-i-1):
#             if so[j] >so [j+1]:
#                 temp = so[j]
#                 so[j]= so[j+1]
#                 so[j+1]= temp
#     print(so)
#     print(so[::-1])
# hamso([1, 3, 5, 3, 7, 5, 9])

# Nolist = int(input('so luong phan tu :'))
# target = int(input('so muon tim:'))
# list = []
# for i in range(0,Nolist) :
#     a = int(input('so:'))
#     list.append(a)
# for i in list

def findvalue(numbers,target):
    list_i=[]
    for i in range(0,len(numbers)) :
        if numbers[i] == target :
            list_i.append(i)
    return list_i
print(findvalue([7,7,2,3,4,5,6,1],7))

        

    

