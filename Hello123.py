print('PyDev console: using IPython 6.5.0\n')

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['F:\\StudyMaterial\\Efforts\\technical\\Machine Learning\\pyCharmWorkspace\\OpenCV-with-Python', 'F:/StudyMaterial/Efforts/technical/Machine Learning/pyCharmWorkspace/OpenCV-with-Python'])
a = 10
b = 20
a,b = b,c
ll = [1,2,3]
type(ll)
ll = (1,2,3)
type(ll)
print(max(1,2,3,5))

print(max([1,2,8,5]))
max('a','A')
ord('a')
ord('A')
print(1,2,3,4,5)
print(1,2,3,4,5, sep='')
print(1,2,3,4,5, sep='')
print(1,2,3,4,5, sep='')
print(1,2,3,4,5, sep='')
print(1,2,3,4,5, sep='')
print(1,2,3,4,5, sep='')
print(1,2,3,4,5, sep='')
print(1,2,3,4,5, sep='', end='')
print(1,2,3,4,5, sep='', end='')
print(1,2,3,4,5, sep='', end='')
print(1,2,3,4,5, sep='', end='')
print(1,2,3,4,5, sep='', end='')
print(1,2,3,4,5, sep='', end='')
print(1,2,3,4,5, sep='', end='\n')
print(1,2,3,4,5, sep='', end='\n')
print(1,2,3,4,5, sep='', end='\n')
print(1,2,3,4,5, sep='', end='\n')
print(1,2,3,4,5, sep='', end='\n')
print(1,2,3,4,5, sep='', end='\n')
for i in range(5):
    print(i)
for i in range(5):
    print(i, end='')
for i in range(1,5):
    print(i, end='')
for i in range(1,5,2):
    print(i, end='')
range(5)
list(range(5))
sum('1','2','3')
sum(['1','2','3'])
sum([2,2,2.2])
sum(['1','2','3'])
for i in zip([1,2,3,4],['Aman','Sahil','Rajat','Shiv']):
    print(i)
for i in zip([1,2,3,4],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv'],['Aman','Sahil','Rajat','Shiv']):
    print(i)
ord('å')

index = -1

for i in range(200):
    print(str(i),":",chr(i))
    if '¥' in chr(i):
        index = i

print("Found '¥' at index: ", index)

index = -1
character_to_found = '¥'

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found in chr(i):
        index = i

if index!=-1:
    print("Found ",character_to_found," at index: ", index)

index = 0
character_to_found = ''

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found in chr(i):
        index = i

if index!=-1:
    print("Found ",character_to_found," at index: ", index)

index = 0
character_to_found = ' '

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found in chr(i):
        index = i

if index!=-1:
    print("Found ",character_to_found," at index: ", index)

index = 0
character_to_found = ' '

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found in chr(i):
        index = i

if index!=0:
    print("Found ",character_to_found," at index: ", index)

index = 0
character_to_found = ''

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found in chr(i):
        index = i

if index!=0:
    print("Found ",character_to_found," at index: ", index)

is_found = False
index = 0
character_to_found = ''

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found in chr(i):
        is_found = True
        index = i

if is_found:
    print("Found ",character_to_found," at index: ", index)
else:
    print('Given character "',character_to_found,'" not found!!')

is_found = False
index = 0
character_to_found = 'Ç'

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found in chr(i):
        is_found = True
        index = i

if is_found:
    print("Found ",character_to_found," at index: ", index)
else:
    print('Given character "',character_to_found,'" not found!!')

is_found = False
index = 0
character_to_found = ''

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found in chr(i):
        is_found = True
        index = i

if is_found:
    print("Found ",character_to_found," at index: ", index)
else:
    print('Given character "',character_to_found,'" not found!!')
"" in "akfjdkfjdkfjdkfjd"
" " in "akfjdkfjdkfjdkfjd"

is_found = False
index = 0
character_to_found = ''

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found == chr(i):
        is_found = True
        index = i

if is_found:
    print("Found ",character_to_found," at index: ", index)
else:
    print('Given character "',character_to_found,'" not found!!')

is_found = False
index = 0
character_to_found = ''

for i in range(200):
    print(str(i),":",chr(i))
    if character_to_found == chr(i):
        is_found = True
        index = i

if is_found:
    print("Found ",character_to_found," at index: ", index, sep="")
else:
    print('Given character "',character_to_found,'" not found!!', sep="")
"a" in "aman"
"" in "aman"
bin(7)
type(bin(7))
binary_form = bin(7)
binary_form[2:]
a=10
x= 10
def x(input):
    if input> 5:
        return False
    return True

print(callable(x))
print(callable(a))
x
filter(x, [9,3,7,8,2,1])
print(x())
print(x(5))
print(x(55))
print(complex(3, 5))
print(complex(3, 5))
class dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        bark1 = "woof"
        return bark1


fido = dog("Fido", "brown")
print(fido.name)
print(fido.bark())
class dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self, bark1):
        return bark1


fido = dog("Fido", "brown")
print(fido.name)
print(fido.bark("woof"))
class dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

def bark(self, bark1):
    return bark1


fido = dog("Fido", "brown")
print(fido.name)
print(bark("woof"))
class dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color


def bark(bark1):
    return bark1


fido = dog("Fido", "brown")
print(fido.name)
print(bark("woof"))
import boto
help(boto)
import os
%history -f HelloIndia.txt
%history -f Hello123.py
