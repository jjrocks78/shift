from statistics import *
n=int(input())
# p=[]
# for i in range(n):
#     p.append(input().rstrip().split()[:4])
# print(p)
# m=input()
# c=0
# x=[]
# for j in range(n):
#     if p[j][0]==m:
#         x=map(int,p[j][1:])
#         c=mean(x)
# print(c)
students={}
for i in range(n):
    x=input().rstrip().split()
    name,scores=x[0],map(float,x[1:])
    students[name] = scores
print(mean(students[input()]))