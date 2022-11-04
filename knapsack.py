def sort(profit,deadline,pp,n):
    for i in range(n):
        t=profit[i]
        td=deadline[i]
        tp=pp[i]
        max = i
        while max-1>=0 and profit[max-1] <t:
            max-=1
            profit[max+1] = profit[max]
            deadline[max+1] = deadline[max]
            pp[max+1]=pp[max]
        profit[max]=t
        deadline[max]=td
        pp[max]=tp

n = int(input("Enter number of Objects: "))
m = int(input("Size of bag: "))

profit = [int(i) for i in "10 5 15 7 6 18 3".split()[:n]]
weights = [int(i) for i in "2 3 5 7 1 4 1".split()[:n]]

p_w = [profit[i]/weights[i] for i in range(n)]

sort(p_w,weights,profit,n)
t=[]
t_profit=0
for i in range(n):
    if(m<=0):
        break
    if weights[i]<=m:
        m-=weights[i]
        t.append([profit[i],weights[i],1])
        t_profit+=profit[i]
    else:
        t.append([profit[i],weights[i],m/weights[i]])
        t_profit+=profit[i]*m/weights[i]
        m=0
    print(m)
print(t)
print("total profits",t_profit)