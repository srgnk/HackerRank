class Complex(object):
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.img + no.img)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.img - no.img)
        
    def __mul__(self, no):
        return Complex(self.real*no.real - self.img*no.img,
                      self.real*no.img + self.img*no.real)
        
    def __truediv__(self, no):
        return Complex((self.real*no.real + self.img*no.img)/(no.real**2 + no.img**2),
                      (self.img*no.real - self.real*no.img)/(no.real**2 + no.img**2))

    def mod(self):
        return Complex((self.real**2 + self.img**2)**(1/2),
                       0)

    def __str__(self):
        if self.img == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.img >= 0:
                result = "0.00+%.2fi" % (self.img)
            else:
                result = "0.00-%.2fi" % (abs(self.img))
        elif self.img > 0:
            result = "%.2f+%.2fi" % (self.real, self.img)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.img))
        return result