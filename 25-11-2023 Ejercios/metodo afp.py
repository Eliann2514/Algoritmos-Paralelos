class Nomina:
 
 def Afp(self,sb):
    return sb * 0.07

 def Ars(self,sb):
   return sb * 0.02

 def SueldoNeto (self,sb,td):
   return sb - td

 def TotalDesc(self,afp, ars):
    return afp + ars

n=Nomina()
sueldo = float(input("Entre el Sueldo Base :"))
afp = n.Afp(sueldo)
ars = n.Ars(sueldo)
descuentos =n.TotalDesc(afp, ars)
sn = n.SueldoNeto(sueldo,descuentos)

print ("Afp         : {:0.2f}".format(afp))
print ("Ars         : {:0.2f}".format(ars))
print ("Descuentos  : {:0.2f}".format(descuentos))
print ("Sueldo Neto : {:0.2f}".format(sn))