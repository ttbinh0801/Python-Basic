# viết 1 chương trình quản lí hsinh với các chức năng:
# 1. thêm ttin hs
# 2. in toàn bộ ttin hs
# 3. chỉnh sửa ttin hs
# 4. xoá ttin hs
# sử dụng dict lưu trữ dữ liệu
# và sử dụng function cho từng chức năng

khodulieu={}
def addstudent (studentid,name,age,score):
    if studentid in khodulieu :
        print('already used')
    else:
        khodulieu[studentid]={
            'name': name,
            'age': age,
            'score': score
        }
        print(f'the student id which is {studentid} had successfully added into the list')
        print(khodulieu)
addstudent(1,'Bình',17,9)
addstudent(112, 'Bình2', 17, 9)
def Allstudentdisplay():
    for student,studentinfo in khodulieu.items():
       print(f"ID :{student} , Name :{studentinfo['name']} , age :{studentinfo['age']}, score :{studentinfo['score']}")
Allstudentdisplay()
def findstudent(studentid):
    if studentid in khodulieu :
        print(
            f"ID :{studentid} , Name :{khodulieu[studentid]['name']} , age :{khodulieu[studentid]['age']}, score :{khodulieu[studentid]['score']}")
    else :
        print('student is not on the list')
findstudent(112)
def updateinfo(studentid,name=None,age=None,score=None):
    if studentid in khodulieu:
        if name :
            khodulieu[studentid]['name']= name
        if age:
            khodulieu[studentid]['age'] = age 
        if score:
            khodulieu[studentid]['score'] = score
    else :
        print('the student does not exist')
def delstudent(studentid):
    if studentid in khodulieu:
        choice=input(f'bạn có muốn xoá hs có id là {studentid} ko:')
        if choice == 'y' :
            del khodulieu[studentid]
            print('the student had been deleted')
delstudent(112)
print(khodulieu)

    

    