Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018, 20:59:26) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def patternToNumber(dna):
	crumb = dict(zip('ACGT' , '0123'))
	return int("".join(crumb[i] for i in dna), 4)

>>> print(patternToNumber("TTC"))
61
>>> print(patternToNumber("GGCGGATACTAGGCTTTACCCACTCTTGGT"))
750068321098168299
>>> 
