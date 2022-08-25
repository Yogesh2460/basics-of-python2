c=set([5,6,7,8])
#c
#{8,7,6,8}
A=set('abc')
f=set('123')
>>> f
set(['1', '3', '2'])
>>> 1 in f
False
>>> '1' in f
True
>>> a=set(456)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=set(456)
TypeError: 'int' object is not iterable
>>> a=set('456')
>>> a
set(['5', '4', '6'])
>>> a|f
set(['1', '3', '2', '5', '4', '6'])
s='i\'ll be there for you:)'
>>> print(s.capitalize())
I'll be there for you:)
>>> print(s.find('for you'))
14
>>> print(s.isalnum)
<built-in method isalnum of str object at 0x7f95431042f0>
>>> >>> print(s.isalnum())
SyntaxError: invalid syntax
>>> print(s.isalnum())
False
>>> word_list=s.split()
>>> word_list
["i'll", 'be', 'there', 'for', 'you:)']
>>> print(s.swapcase())
I'LL BE THERE FOR YOU:)
>>> s='''hi
hello
namskara'''
>>> s
'hi\nhello\nnamskara'
>>> sline=s2.splitlines()
sline
['hi', 'hello', 'namskara']
>>> sline[2]
'namskara'
>>> sline[0:2]
['hi', 'hello']

#to join a string ionto empty string this helps to change directory and go to other directory create file there
>>> a1='abc'
>>> a2=''
>>> for ele in a1[::-1]:
	a2+=''.joine(ele)
   print(a2)
