x = int(input('please input your number: '))
if x > 1 and x != 4:
    for i in range(2 , x//2):
        if x % i == 0:
            print('add aval nemibashad')
            break
    else:
        print('add aval mibashad')  
else:
    print("adda aval nemibashad")
