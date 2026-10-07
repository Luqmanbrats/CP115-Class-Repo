number = int(input())
count=0
biggest_jump=0
previous=number
while number!=0:
    count+=1
    jump=number-previous
    if jump>biggest_jump:
        biggest_jump=jump
    previous=number
    number=int(input())
print(count)
print(biggest_jump)
