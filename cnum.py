from precision_of_float_number import precision_of_float_number as pre
import math
import cmath

class complex_number():
    """"""
    def __init__(self, z):
        """"""
        self.z=z
    
    def obliczanie(self):
        x=self.z.real
        y=self.z.imag 
        prec1=pre(x).check_precision()
        module=math.sqrt(x**2+y**2)
        print(module)
        module=round(module, prec1)
        t=math.acos(x/module)*(180/math.pi)
        t=round(t, prec1)
        return(module, t)

#if __name__ == "__main__":
    #print(complex_number(1.000+1.000j).obliczanie())


