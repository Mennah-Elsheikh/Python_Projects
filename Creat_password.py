import string
import random
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_lowercase)
s3 = list(string.ascii_letters)
s4 = list(string.punctuation)

num_of_characters = input("Please, Enter the number of characters you need: ")

while (True):
    try:
       num_of_characters = int(num_of_characters)  
       if num_of_characters < 6 :
        print("the numer should be at least 6 ")
        num_of_characters = input("Please, Enter the number again : ")
       else :
           break
    except:
      print ("please , Enter nubers only : ")
      num_of_characters = input("Enter the number of characters you need: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(num_of_characters*(30/100))
part2= round(num_of_characters*(20/100))

password= []

for i in range(part1):
  password.append(s1[i])
  password.append(s2[i])
for i in range(part2):
   password.append(s3[i])
   password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])
print(password)