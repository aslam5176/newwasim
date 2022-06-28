a1=input("enter the letters of a1")
a2=input("enter the letters of a2")
##def common_letters(a1):
##  if(a1 in a2):
##      return True
##  else:
##      False
##common_letters=filter(common_letters,a1)
##a2=list(common_letters)
##print(a2)

def subsequence(a1,a2):
    a = list(a1)
    b = list(a2)
    s = ""
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                s += a[i]
                
                
                
    print(s)
                
    
            




subsequence(a1, a2)
