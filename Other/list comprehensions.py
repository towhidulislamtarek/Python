num= [1,2,3,4,5]
[x*x for x in num]

result = list (list(map(lambda x : x*x,num)))
print(result)