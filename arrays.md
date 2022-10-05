# Arrays

+ [Squares of sorted array](#squares-of-sorted-array)
+ [Merge two sorted arrays](#merge-two-sorted-arrays)

## Squares of sorted array

Дан отсортированный список в неубывющем порядке. Вернуть элементы этого списка, возведенные в квадрат, в неубывающем порядке
Элементы списка это целые числа. Требуемое время работы $\mathcal{O}(n)$.

```python 
def merge(first, second):
    arr = []
    j = 0
    for i in range(len(first)):
        if first[i] <= second[j]:
            arr.append(first[i])
        else:
            while j < len(second) and second[j] < first[i]:
                arr.append(second[j])
                j += 1
            arr.append(first[i])
    if j < len(second) - 1:
        while j < len(second):
            arr.append(second[j])
            j += 1
    return arr
    
def squares(arr):
    arr_neg = []
    arr_pos = []
    for elem in arr:
        if elem < 0:
            arr_neg.append(elem**2)
        else: arr_pos.append(elem**2)
    arr_neg = arr_neg[::-1]
    return merge(arr_neg, arr_pos)

```

## Merge two sorted arrays


На входе два отсортированных массива (списка), на выходе получить 1 отсортированный массив
Элементы списка это целые числа. Требуемое время работы $\mathcal{O}(n)$.

```python

def merge(first, second):
    arr = []
    j = 0
    for i in range(len(first)):
        if first[i] <= second[j]:
            arr.append(first[i])
        else:
            while j < len(second) and second[j] < first[i]:
                arr.append(second[j])
                j += 1
            arr.append(first[i])
    if j < len(second) - 1:
        while j < len(second):
            arr.append(second[j])
            j += 1
    return arr
