'''moves=34
winningpoint=int(input("Enter the winning point: "))

while moves>0:
    if moves==winningpoint:
        print("Congrats!!!You won the game")
        break
    print(f"{moves} RE left. Tou have chance to win the game")
    moves-=1
else:
    print("Game Over. Try Again")

n=int(input())
s=0
while n>0:
    s+=(n%10)
    n//=10

print(s)'''

n=int(input())
temp=n
rev=0
while n>0:
    rev=rev*10+(n%10)
    n//=10

if rev==temp:
    print("palindrome")
else:
    print("Not palindrome")
