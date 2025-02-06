
with open('regex-sum-42.txt','r') as file:
   digit=[]
  
   for line in file:
       
      
       texts=line.strip()
       words=texts.split()
 
       for word in words:
        if word.isdigit():
         digit.append(int(word))
print(sum(digit))
        
