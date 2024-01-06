# # function có return
def welcome(fname, lname):
    return f"hello {fname} {lname}"
print(welcome('Binh',"tran"))


# # function k co return
# def welcome(fname, lname):
#     print( f"hello {fname} {lname}")
# welcome('Binh',"tran")

# def hello(*name):
#     print(f'hello',*name)
# hello('binh')


# bt
# Input: [2, 1, 5, 3, 7, 9]
# Output: [1, 2, 3, 5, 7, 9]
# def sort_array(array):
#     pass
def sort_array(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


print(sort_array([2, 1, 3, 5, 6, 4, 9]))


def sort_array(array):
    for i in range(len(array)):                    
        for j in range(0, len(array) - i - 1):     
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


print(sort_array([2, 1, 3, 5, 6, 4, 9]))


# btvd: viet lai 1 web dky su dung function
def thongtin( firstname 
        ,lastname 
        ,email 
        ,password )
    firstname = input('tên :')
    lastname = input('tên đệm')
    email = input('email:')
    password = input('pass:')
    return {
        firstname : firstname,
        lastname : lastname,
    }
    while True:
        print('1.sign up')
        print('2.sign in')
        choice = int(input('lựa chon:'))
        if choice==1 :





# viết 1 chương trình quản lí hsinh với các chức năng: 
# 1. thêm ttin hs
# 2. in toàn bộ ttin hs
# 3. chỉnh sửa ttin hs
# 4. xoá ttin hs
# sử dụng dict lưu trữ dữ liệu 
# và sử dụng function cho từng chức năng

