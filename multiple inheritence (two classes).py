class rawmaterial:
    mat1="tomato"
    mat2="capsicum"

class makedmaterial:
    mat3="bread"


class sandwitch(rawmaterial,makedmaterial):
    def __init__(self):
        print("materials used in making sandwitch are{},{} and {}".format(self.mat1,self.mat2,self.mat3))


sandd=sandwitch()
          
