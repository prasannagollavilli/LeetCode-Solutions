class Solution(object):
    def squareIsWhite(self, coordinates):
        d={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
        a=int(d.get(coordinates[0]))
        print(a)
        b=int(coordinates[1])
        print(b)
        if (a+b)%2==1:
            return True
        else:
            return False
        