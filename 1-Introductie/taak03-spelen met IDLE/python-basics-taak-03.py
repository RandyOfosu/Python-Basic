Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3*'Py'+2*'thon'
'PyPyPythonthon'
>>> len('even kijken wat deze functie doet')
33
>>> a = 'is dit aantal tekens.'
>>> len(a)
21
>>> int('even kijken of dit kan.')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('even kijken of dit kan.')
ValueError: invalid literal for int() with base 10: 'even kijken of dit kan.'
>>> int('56.87')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('56.87')
ValueError: invalid literal for int() with base 10: '56.87'
>>> int(['oh ik zie nu pas dat het op deze manier moet'])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(['oh ik zie nu pas dat het op deze manier moet'])
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> int('hmm', 12)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int('hmm', 12)
ValueError: invalid literal for int() with base 12: 'hmm'
>>> int('uhh', base=12)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int('uhh', base=12)
ValueError: invalid literal for int() with base 12: 'uhh'
>>> print(int("dit zou moeten werken"))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(int("dit zou moeten werken"))
ValueError: invalid literal for int() with base 10: 'dit zou moeten werken'
>>> print(int("12"))
12
>>> int("12")
12
>>> int("56.87")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int("56.87")
ValueError: invalid literal for int() with base 10: '56.87'
>>> test = 56.87
>>> test = int(test)
>>> print(test)
56
>>> type(test)
<class 'int'>
>>> type(str(test))
<class 'str'>
>>> num1 = 162.48
>>> num2 = 13.45
>>> num1 / num2
12.080297397769517
>>> int(num1 / num2)
12
>>> type(int(num1 / num2))
<class 'int'>
>>> type(str(num1 / num2))
<class 'str'>
>>> 