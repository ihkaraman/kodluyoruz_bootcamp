# ihkaraman

from scipy.integrate import quad
import math
import numpy as np

class DataClass():
       
    print("DataClass sınıfına hoş geldiniz.")
    def __init__(self, mean, stdDev, size):
        self.veri = self.dagilimOlustur(mean, stdDev, size)
        self.mean = mean
        self.stdDev = stdDev
        self.size = size           
        
    def specPrint(self):
        print("Nesnenin özellikleri yazdırılıyor.")
        print("Ortalama : {} \nStandart Sapma : {} \nBüyüklük : {}".format(self.mean, self.stdDev, self.size))
    

    # finding cdf manually          
    def cdfBul(self, x):
        I = quad(self.integrand, -math.inf, x)
        return I 
    
    def integrand(self, x):
        return (math.e**(-x**2/2))/(2*math.pi)**0.5    
    
    # finding pdf manually          
    def pdfBul(self, x):     
        return (math.e**((-x-self.mean)**2/(2*self.stdDev*2)))/self.stdDev*(2*(math.pi)**0.5)   
    
    def dagilimOlustur(self, mean, stdDev, size):
        normDist = np.random.normal(mean, stdDev, size)
        return normDist 
            
            

veri = DataClass(3, 5, 200)
veri.specPrint()
print("1----------")
pdf = veri.pdfBul(10)
print("pdf: ", pdf)
print("2----------")
cdf = veri.cdfBul(10)
print("cdf: ", cdf)
print("3----------")
