num=int(input("Enter a number\n"))
sum = 0
temp = num
while temp > 0:
    n=temp%10
    sum+=n**3
    temp//=10
if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")