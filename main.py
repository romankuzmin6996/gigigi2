from math import *
def funkcija(x) :
  y = 0
  if x<0:
    y = cos(abs(x))
  elif x == 0:
    y = -120
  else:
    y = sin(x**2)
  return y
x = int(input("Ievadiet x: "))
print("y = ", funkcija(x))