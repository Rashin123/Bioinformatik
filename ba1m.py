Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018, 20:59:26) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> NumberToSymbol = {0: 'A' , 1: 'C' , 2: 'G', 3: 'T'}
>>> def NumberToPattern(n, k):
	if k == 1
	
SyntaxError: invalid syntax
>>> NumberToSymbol = {0: 'A' , 1: 'C' , 2: 'G', 3: 'T'}
>>> def NumberToPattern(n, k):
	kk+
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> NumberToSymbol = {0: 'A' , 1: 'C' , 2: 'G', 3: 'T'}
>>> def NumberToPattern(n, k):
	if k == 1
	
SyntaxError: invalid syntax
>>> def NumberToPattern(n, k):
	if k == 1
	
SyntaxError: invalid syntax
>>> def NumberToPattern(n, k):
	if k == 1:
		return numbertosymbol[n]
	prefixindex = n//4
	r = n % 4
	symbol = numbertosymbol[r]
	prefixpattern = numbertopattern(prefixindex, k-1)
	return prefixpattern + symbol

>>> 
>>> print(numbertopattern(45, 4))

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(numbertopattern(45, 4))
NameError: name 'numbertopattern' is not defined
>>> numbertosymbol = {0: 'A' , 1: 'C' , 2: 'G', 3: 'T'}
>>> def numbertopattern(n, k):
	if k == 1:
		return numbertosymbol[n]
	prefixindex = n//4
	r = n % 4
	symbol = numbertosymbol[r]
	prefixpattern = numbertopattern(prefixindex, k-1)
	return prefixpattern + symbol

>>> 
>>> print(numbertopattern(45, 4))
AGTC
>>> print(numbertopattern(8976, 11))
AAAAGATACAA
>>> 
