"""
#to join a string ionto empty string this helps to change directory and go to other directory create file there

a1='abc'
a2=''
for ele in a1[::-1]:
    a2+=' '.join(ele)
print(a2)
"""
#to check if they r anagrams or not

def anagrams(a,b):
   if sorted(a)==sorted(b):
      print("anagrams")
   else:
      print("not an anagram")
a=input("enter first ")#'mary' a=listen
b=input("enter second ")#'army'#or b=silent
anagrams(a,b)
