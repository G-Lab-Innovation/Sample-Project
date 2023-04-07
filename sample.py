TO CHECK IF TWO STRINGS ARE ANAGRAMS OR NOT

def check(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
s1 = input()
s2 = input()
check(s1, s2)

SAMPLE OUTPUT:
     
Input : s1 = "listen"
        s2 = "silent"
Output : The strings are anagrams.
