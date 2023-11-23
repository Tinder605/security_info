class Ellptic_Curve():
    base_point = (0,0)

    def __init__(self,a,b,p,base_point):
        self.a = a
        self.b = b
        self.p = p
        self.base_point = base_point
    
    # 係数の比較を行い、λを作成する
    def create_lamda(self,former,latter):
        flag = True
        res = 0
        if(former[0] == latter[0] and former[1] == latter[1]):
            lamda_num = 3 * (former[0]**2) + self.a
            lamda_den = 2 * former[1]
        else:
            lamda_num = latter[1] - former[1]
            lamda_den = latter[0] - former[0]
        if(lamda_num < 0):
            exp = 1
            if(abs(lamda_num)/self.p > 1):
                exp = (abs(lamda_num)//self.p) + 1
            lamda_num = exp * self.p + lamda_num
 
        if(lamda_den < 0):
            exp = 1
            if(abs(lamda_den)/self.p > 1):
                exp = (abs(lamda_den)//self.p) + 1
            lamda_den = exp * self.p + lamda_den
        lamda_num = divmod(lamda_num,self.p)[1]
        lamda_den = divmod(lamda_den,self.p)[1]

        if(lamda_num == 0):
            res = 0
            flag = False
        # lamdaを計算して、該当する値
        while(flag):
            q,r = divmod(lamda_num + self.p, lamda_den)
            if(r==0):
                res = q
                flag = False
            else:
                lamda_num = lamda_num + self.p

        return res

    def create_point(self,former,latter):
        lamda = self.create_lamda(former,latter)
        if(lamda == False):
            res = [0,0]
        else:
            point_x = (lamda ** 2) - former[0] - latter[0]

            if(point_x < 0):
                exp = 1
                if(abs(point_x)/self.p > 1):
                    exp = (abs(point_x)//self.p) + 1
                point_x = exp * self.p + point_x

            point_y = lamda*(former[0] - point_x) - former[1]

            if(point_y < 0):
                exp = 1
                if(abs(point_x)/self.p > 1):
                    exp = (abs(point_x)//self.p) + 1
                point_y = self.p + point_y

            x_3 = divmod(point_x,self.p)[1]
            y_3 = divmod(point_y,self.p)[1]
            res = [x_3,y_3]
        
        return res
    
    def mulpitle(self,add_count):
        res = self.base_point
        for i in range(add_count-1):
            res = self.create_point(res,self.base_point)
        return res

if __name__ == "__main__":
    ellptic = Ellptic_Curve(2,1,11,[8,10])
    print("ベースポイントは{0}".format(ellptic.base_point))
    i = 2
    flag = True
    while(flag):
        result = ellptic.mulpitle(i)
        if(ellptic.base_point[0] == result[0] and ellptic.base_point[1] == result[1]):
            flag = False
        print("{0}倍した座標は{1}".format(i,result))
        i = i + 1
    # ellptic.mulpitle(3)

             
