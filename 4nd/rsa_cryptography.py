#モジュール
import sys

class RSA_Cryptography():
    def __init__(self,p,q,e):
        self.n = p * q
        self.sigma_n = (p-1) * (q-1)
        self.p = p
        self.q = q
        self.e = e
        print("公開鍵 n=" + str(self.n) + ", e=" + str(self.e))
        
    
    def create_encryption_key(self):
        # 逆元
        inverse = 1
        list_q = []
        #あまりが1になるまで繰り返す
        r = 0

        sigma = self.sigma_n
        e = self.e
        #ユーグリッド互除法
        while(r != 1):
            #print("割られる値" + str(sigma) + "割る値は" + str(e))
            q,r = divmod(sigma,e)
            #print("商は" + str(q) + ",余りは" + str(r))
            list_q.append(q)
            if(r != 1):
                sigma = e
                e = r
            else:
                break
        if(len(list_q) == 1):
            inverse = sigma - list_q[0]
        elif(len(list_q) == 2):
            inverse = 1 - list_q[1]*((-1)*list_q[0])
        else:
            inverse = (-1)*list_q[0] - (list_q[2] * (1 - list_q[1]*((-1)*list_q[0])))
        if(inverse<0):
            inverse = self.sigma_n + inverse
        print("秘密鍵: d=" + str(inverse) + ", p=" + str(self.p) + ", q=" + str(self.q))
        return inverse
    
    def encode_message(self,m):
        print("メッセージ: m=" + str(m) )
        c = divmod(m ** (self.e),self.n)[1]
        return c
    
    def decode_message(self,c,d):
        m = divmod(c ** d,self.n)[1]
        return m

if __name__ == "__main__":
    rsa = RSA_Cryptography(29,103,13)
    answer = rsa.create_encryption_key()
    c_message = rsa.encode_message(94)
    print("メッセージの暗号化" + str(c_message))
    message = rsa.decode_message(c_message,answer)
    print("暗号化メッセージの復号" + str(message))

    rsa = RSA_Cryptography(11,13,7)
    answer = rsa.create_encryption_key()
    c_message = rsa.encode_message(94)
    print("メッセージの暗号化" + str(c_message))
    message = rsa.decode_message(c_message,answer)
    print("暗号化メッセージの復号" + str(message))
