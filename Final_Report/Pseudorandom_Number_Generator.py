import numpy as np
import matplotlib.pyplot as plt

# 平方採中法
def middle_square_method(x):
    x_2 = str(x**2)
    if(divmod(len(x_2),2) == 1):
        x_2 = "0" + x_2
    middle_idx = int(len(x_2)/2)
    res = x_2[middle_idx-2:middle_idx+2]
    return res

# 線形合同法
def linear_congruential_method(a,c,M,x):
    linear_val = a*x+c
    res = divmod(linear_val,M)[1]
    return res

# LFSR
def LFSR_function(x,layer,return_pattern):
    register = str(x)
    cycle_flag = True
    register_list = []
    if(layer - len(str(x)) > 0):
        for i in range(layer-len(str(x))):
            register = register + "0"
    register_list.append(register)
    after_register = len(register)*[0]
    while cycle_flag:
        after_register[0] = str(divmod(int(register[return_pattern[0]-1]) + int(register[return_pattern[1]-1]),2)[1])
        for i in range(len(register)):
            if(0 != i):
                after_register[i] = register[i-1]
        register = ''.join(after_register)
        if(register in register_list):
            cycle_flag = False
        else:
            register_list.append(register)
    return register_list

def plot_xypoint(x_range,y_range):
    # figureオブジェクトの生成
    fig = plt.figure(figsize=(7,5))

    # subplotの書式設定
    ax = fig.add_subplot(111, aspect='equal')
    ax.set_xlim(0, 256)
    ax.set_ylim(0, 256)
    # set axis labels
    ax.set_xlabel('input')
    ax.set_ylabel('output')
    # 各座標を入れる
    ax.scatter(x_range,y_range, s=10, c='blue',  marker='o', alpha=0.5, linewidths=0.2)
    # グリッドの表示
    ax.grid()
    # グラフの表示
    plt.show()

if __name__ == "__main__":
    # 平方採中法
    sample = [3145,8910,3881]
    for val in sample:
        print("入力データ：{0}->出力データ：{1}".format(val,middle_square_method(val)))
    
    # 線形合同法
    x_val = range(0,256)
    y_val = []
    for input in x_val:
        y_val.append(linear_congruential_method(a=129,c=5,M=256,x=input))
    plot_xypoint(x_range=x_val,y_range=y_val)

    # LFSR
    register_data = LFSR_function(x=1,layer=7,return_pattern=(7,1))
    for idx,val in enumerate(register_data):
        if(idx<20 or idx>len(register_data)-3):
            print("{0}：{1}".format(idx+1,val))
