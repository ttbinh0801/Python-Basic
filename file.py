with open('example.txt', 'a') as file:
    # # 1.read(): đọc toàn bộ file
    # print(file.read())
    # # 2.readline() : đọc từng dòng file
    # print(file.readline())
    # # 3.read(n) : đọc n (n:ký tự đầu)
    # print(file.read(6))
    file.write('hello,world' + '\n')
