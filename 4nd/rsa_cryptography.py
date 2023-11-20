#モジュール
import sys

class RSA_Cryptography():
    def __init__(self,p,q,e):
        self.n = p * q
        self.sigma_n = (p-1) * (q-1)
        self.e = e
        print("割られる値" + str(self.e) + "割る値は" + str(self.sigma_n))
    
    def encryption(self):
        # 逆元
        inverse = 1
        list_q = []
        #あまりが1になるまで繰り返す
        r = 0
        #ユーグリッド互除法
        while(r != 1):
            print("割られる値" + str(self.e) + "割る値は" + str(self.sigma_n))
            q,r = divmod(self.e,self.sigma_n)
            print("商は" + str(q) + ",余りは" + str(r))
            list_q.append(q)
            if(r != 1):
                self.e = self.sigma_n
                self.sigma_n = r
            else:
                break
        
        addition = 1
        for i in list_q:
            addition = addition*i

        inverse = inverse + addition
        # print(list_q)

        return inverse

if __name__ == "__main__":
    rsa = RSA_Cryptography(11,13,7)
    answer = rsa.encryption()
    print("生成した暗号カギは" + str(answer))
