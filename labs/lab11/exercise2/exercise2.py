score = int(input())
total_a=0
total_b=0
count=1
while score!=-1:
    if count%2==0:
        total_b+=score
    else:
        total_a+=score
    count+=1
    score=int(input())
if total_a>total_b:
    winner="A"
elif total_b>total_a:
    winner="B"
else:
    winner="Tie"
print(total_a)
print(total_b)
print(winner)
