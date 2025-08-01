
s=input("Enter a sentence ")
n=1

for i in range(len(s)):
    if(s[i]==" "):
        n+=1

print("Number of words in the sentence is", n)