import random

class shared_keys():
    def __init__(self,p) -> None:
        self.p = p
        self.g = self.explore_primitive_element(p)
    
    def explore_primitive_element(self,p):
        flag = True
        g = 3
        while(flag and g<p-1):
            formmer = divmod(g**((p-1)/2),p)[1]
            if(formmer == p-1):
                flag = False
            g = g + 1
        return g

class Diffie_Hellman():
    def __init__(self,p,g) -> None:
        self.K = random.randint(1,1000)
        self.param = divmod(g**self.K,p)[1]
        self.reciever = 0
        self.key = 0
        self.p = p
    
    def recieve(self,param):
        self.reciever = param
        self.key = divmod(param**self.K,self.p)[1]

if __name__ == "__main__":
    init_key = shared_keys(7)
    Alice = Diffie_Hellman(init_key.p,init_key.g)
    Bob = Diffie_Hellman(init_key.p,init_key.g)

    Alice.recieve(Bob.param)
    Bob.recieve(Alice.param)

    if(Alice.key == Bob.key):
        print("鍵共有できている")
    else:
        print("鍵共有できていない")
