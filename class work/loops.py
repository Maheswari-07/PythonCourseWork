moves=34
winningpoint=int(input("Enter the winning point: "))

while moves>0:
    if moves==winningpoint:
        print("Congrats!!!You won the game")
        break
    print(f"{moves} RE left. Tou have chance to win the game")
    moves-=1
else:
    print("Game Over. Try Again")
