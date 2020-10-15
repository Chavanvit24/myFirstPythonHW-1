Problem21



```python
 listA=[1,2,3]
```


```python
sum(listA)
```




    6




```python
sumlist=0
for i in listA:
          sumlist+= i
print(sumlist)
```

    6
    


```python
def sumlist(listA):
    sumlist=0
    for i in listA:
        sumlist +=i
    return(sumlist)
sumlist1 = sumlist(listA)
print(sumlist1)
```

    6
    

Problem22


```python
def sumlist (list):
    sumlist=' '
    for i in list :
        sumlist +=i
    return sumlist
a=['hello','world']
b=['aaa','bbb','ccc']
print(sumlist(a))
print(sumlist(b))
```

     helloworld
     aaabbbccc
    

Problem23


```python
a=[8,9,10]
def product(a):
    product = 1
    for i in a :
        product *=i
    return(product)
producta = product(a)
print(producta)        
```

    720
    

Problem24


```python
def factorialN(n):
    if n < 0:
        print('Error: factorila cannot less than o ')
        return(-1)
    elif n == 0:
        return(1)
    else:
        j = 1
        for i in range(1,n+1):
            print(i)
            j *= i
    return j

```


```python
factorialN(5)
```

    1
    2
    3
    4
    5
    




    120



Problem25


```python
listA=[1,2,3,4]
print(listA)
```

    [1, 2, 3, 4]
    


```python
def reverse(listA):
    listALen = len(listA) - 1
    reverseListA = []
    for i in range(len(listA)) :
        reverseListA.append(listA[listALen-i])
    return(reverseListA)
reverse(listA)
```




    [4, 3, 2, 1]



Problem26


```python
listA = [1,2,3,4,5,6]
listB = ['a','b','c','d','e','f']
print(max(listA))
print(min(listA))
print(max(listB))
print(min(listB))
```

    6
    1
    f
    a
    


```python
def mymax(listin):
    maxvalue = listin[0]
    for i in listin:
          if maxvlue< i :
                maxvlue=i
    return maxvalue
def mymin(listin):
    maxvalue = listin[0]
    for i in listin:
          if maxvlue> i :
                maxvlue=i
    return maxvalue
print(max(listA))
print(min(listA))
print(max(listB))
print(min(listB))
```

    6
    1
    f
    a
    

Problem27


```python
def cumulativesum(listIn):
    cumuValue = listIn[0]
    cumulist = [ ]
    cumulist.append(cumuValue)
    for i in range(1,len(listIn)):
        cumuValue = cumuValue+listIn[i]
        cumulist.append(cumuValue)
    return cumulist
```


```python
cumulativesum(listA)
```




    [1, 3, 6, 10, 15, 21]




```python
cumulativesum(listB)
```




    ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']



Problem28


```python
def cumulativesum(listIn):
    cumuValue = listIn[0]
    cumulist = [ ]
    cumulist.append(cumuValue)
    for i in range(1,len(listIn)):
        cumuValue = cumuValue*listIn[i]
        cumulist.append(cumuValue)
    return cumulist
```


```python
cumulativesum(listA)
```




    [1, 2, 6, 24, 120, 720]




```python
def findUnique(listIn):
    UniqueValue = listIn[0]
    Uniquelist = [ ]
    Uniquelist.append(UniqueValue)
    for i in range(1,len(listIn)):
        Uniquecheck = 0
        UniqueValue = listIn[i]
    for j in  Uniquelist:
        if j ==  UniqueValue:
            Uniquecheck = 1
        if Uniquecheck == 0:
            Uniquelist.append( UniqueValue)   
    return  Uniquelist
```


```python
findUnique([1,2,1,3,2,5])
```




    [1, 5]



Problem29


```python
def unique(lists):
    unique=[]
    for i in lists:
        if i not in unique :
            unique.append(i)
    return unique
unique([1,2,1,3,2,5])
```




    [1, 2, 3, 5]



Problem30


```python
def dups(x):
    indups = []
    for i in range(len(x)):
        for k in range (i + 1, len(x)):
            if x[k]==x[i]:
                indups.append(x[k])
    return indups
dups([1 ,2 ,1 ,3 ,2 ,5])
            
    
```




    [1, 2]




```python

```
