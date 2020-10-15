Problem11


```python
x = 2 
def f(a): 
    x = a * a 
    return x 
y = f(3) 
print(x, y)
```

    2 9
    

Problem12


```python
def count_digits(n):
    return len(str(n))
count_digits(5)
```




    1




```python
def count_digits(n):
    return len(str(n))
count_digits(12345)
```




    5



Problem13


```python
def istrcmp(x,y):
    if x.upper() == y.upper():
        return True
    else:
        return False

print (istrcmp('python', 'Python'))
print (istrcmp('LaTeX', 'Latex'))
print (istrcmp('a', 'b'))

```

    True
    True
    False
    

Problem14


```python
print(2 < 3 and 3 > 1) 
print(2 < 3 or 3 > 1) 
print(2 < 3 or not 3 > 1) 
print(2 < 3 and not 3 > 1)
```

    True
    True
    True
    False
    

Problem15


```python
x = 4 
y = 5 
p = x < y or x < z 
print(p)
```

    True
    

Problem16


```python
True, False == False, True
print(True, False) 
print(2 < 3)
```

    True False
    True
    

Problem17


```python
x = 2 
if x == 2:
    print x 
else: print y
```


      File "<ipython-input-10-f64d328b9447>", line 3
        print x
              ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
    



```python
x = 2 
if x == 2:
    print (x) 
else: print (y)
```

    2
    

Problem18


```python
x = 2 
if x == 2: 
    print(x) 
else:
        print(x +x)
```

    2
    

Problem19


```python

```

Problem20


```python
x = [0, 1, [2]] 
x[2][0] = 3 
print(x) 
x[2].append(4) 
print(x) 
x[2] = 2 
print(x)
```

    [0, 1, [3]]
    [0, 1, [3, 4]]
    [0, 1, 2]
    


```python

```
