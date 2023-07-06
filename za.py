def area_calculator(a:str):
    def r(x,y):
        return x*y
    def c(x):
        x = int(input())
        return x*3,14
    def s(x):
        return x*x
    def t(x,y,z):
        return x*y*z
    if a == "rectangle":
        return r
    if a == "circle":
        return c
    if a == "square":
        return s
    if a == "tritangle":
        return t
print(area_calculator("tritangle")(1,2,3))