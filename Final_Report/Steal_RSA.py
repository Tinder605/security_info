#モジュール
import sys

p = 2161
q = 1949
d = 3606583

def Euler_funtion(p,q,d,c):
    flag = True
    count = 2
    current_param = c
    phy_n = (p-1)*(q-1)
    modify_list = []

    while flag:
        if(count < d):
            current_param = divmod(current_param**2,p*q)[1]
            modify_list.append(current_param)
            count *= 2
        else:
            # print(count)
            flag = False
    check_d = d - 2**len(modify_list)
    res = modify_list[len(modify_list)-1]
    while(check_d>=1):
        for i in reversed(range(len(modify_list))):
            if(check_d - 2**(i+1)>=0):
                check_d = check_d - 2**(i+1)
                res = divmod(res*modify_list[i],p*q)[1]
                break
        if(check_d<=1):
            if(check_d == 1):
                res = divmod(res*c,p*q)[1]
            break
    return res

if __name__ == "__main__":
    ciphertext = [4089096,4088091,3399469,2400142,1291127,289694,891601]
    for C in ciphertext:
        print(Euler_funtion(p,q,d,C))