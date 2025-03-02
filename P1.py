lenght = int(input())
value = input()
value = value.split(" ")
for i,j in enumerate(value):
    if i == lenght - 1:
        break
    if int(value[i]) >= int(value[i+1]):

        print("No")
        exit()
    
print("Yes")
  #i = index
  #j = value

