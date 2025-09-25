x = int(input("Entrez un nombre"))
print(x,type(x))

print(x+1) # Addition
print(x-1) # Soustraction
print(x*1) # Multiplication
print(x**1) # Exponentiation

A = (x**3 + 2* x + 5)/5*x
print(A)
#----------------------------
t = True
f = False
print(t and f)
print(t or f)
print(not t)
print(t != f)
#----------------------------
hello = 'hello'
world = "world"
print(hello , len(hello))
hw = hello + ' ' + world
print(hw)
#------------------------
hw12 = '{} {} {}'.format(hello,world,12)
print(hw12)
#------------------------
s = "hello"
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('1','(ell)'))
print('world'.strip())
#------------------------
