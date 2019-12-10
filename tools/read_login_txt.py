def read_login_txt(filename):
    arr = []
    with open('./data/'+filename,'r',encoding='utf-8')as f:
        for data in f.readlines():
            arr.append(tuple(data.strip().split(',')))
        print(arr)
        return arr[1::]
