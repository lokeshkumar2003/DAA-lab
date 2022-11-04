def sort(profit,deadline,n):
    for i in range(n):
        t=profit[i]
        td=deadline[i]
        max = i
        while max-1>=0 and profit[max-1] <t:
            max-=1
            profit[max+1] = profit[max]
            deadline[max+1] = deadline[max]
        profit[max]=t
        deadline[max]=td
    


n = int(input("Enter number of jobs: "))
profit = [int(i) for i in "85 25 16 40 55 19 92 80 15".split()[:n]]
deadline = [int(i) for i in "5 4 3 3 4 5 2 3 7".split()[:n]]
sort(profit,deadline,n)
print(profit)
print(deadline)
print(max(deadline))
timeline=[-1]*max(deadline)
t_profit=0
for i in range(n):
    t = deadline[i] - 1
    
    while t >= 0 and timeline[t]!=-1:
         t-=1
    if t>=0:
        timeline[t]=[profit[i],deadline[i]]
        t_profit+=profit[i]
print(timeline)
print("total profits",t_profit)