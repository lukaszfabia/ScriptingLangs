# Data Structures in Python

## List of contents

1. [List](#list)
2. [Set](#set)
3. [Tuple](#tuple)
4. [Dictonary](#dict)

## List <a id="list"></a>

| Operation           | Average Case | Amortized Worst Case |
| ------------------- | ------------ | -------------------- |
| Copy                | O(n)         | O(n)                 |
| Append[1]           | O(1)         | O(1)                 |
| Pop last            | O(1)         | O(1)                 |
| Pop intermediate[2] | O(n)         | O(n)                 |
| Insert              | O(n)         | O(n)                 |
| Get Item            | O(1)         | O(1)                 |
| Set Item            | O(1)         | O(1)                 |
| Delete Item         | O(n)         | O(n)                 |
| Iteration           | O(n)         | O(n)                 |
| Get Slice           | O(k)         | O(k)                 |
| Del Slice           | O(n)         | O(n)                 |
| Set Slice           | O(k+n)       | O(k+n)               |
| Extend[1]           | O(k)         | O(k)                 |
| Sort                | O(n log n)   | O(n log n)           |
| Multiply            | O(nk)        |                      |
| x in s              | O(n)         |                      |
| Get Length          | O(1)         | O(1)                 |

## Set <a id="set"></a>

| Operation                          | Average Case                        | Worst Case                          | Notes                                       | 
|------------------------------------|-------------------------------------|-------------------------------------|---------------------------------------------| 
| x in s                             | O(1)                                | O(n)                                |                                             | 
| Union s|t                         | O(len(s)+len(t))                    |                                     |                                             | 
| Intersection s&t                  | O(min(len(s), len(t)))              | O(len(s) * len(t))                  | replace "min" with "max" if t is not a set | 
| Multiple intersection s1&s2&..&sn | (n-1)*O(l) where l is max(len(s1),..,len(sn))|                               |                                             | 
| Difference s-t                    | O(len(s))                           |                                     |                                             | 
| s.difference_update(t)            |                                     | O(len(t))                           |                                             | 
| Symmetric Difference s^t          | O(len(s))                           | O(len(s) * len(t))                  |                                             | 
| s.symmetric_difference_update(t)  |                                     | O(len(t) * len(s))                  |                                             | 





## Tuple <a id="tuple"></a>

Short function to test tuples.

```python
def tuples() -> None:
    my_tuple = (1, True, "string", 3.4)
    print(my_tuple)

    # unpacking
    a, b, c, d = my_tuple
    print(f'a={a} b={b} c={c} d={d}')

    # len of tuple
    print(f'len={len(my_tuple)}')

    # indexing
    print(f'indexing={my_tuple[1]}')

    # slicing
    print(f'slicing, range of indexes->[1,3): {my_tuple[1:3]}')

    # concatenation
    my_tuple += (5, 6)
    print(f'concatenation={my_tuple}')

    # repetition
    my_tuple *= 2
    print(f'repetition={my_tuple}')

    # membership
    print(f'membership={True in my_tuple}')

    # iteration
    for i in my_tuple:
        print(i)

    # type
    print(f'type={type(my_tuple)}')
```

## Dictonary <a id="dict"></a>

| Operation    | Average Case | Amortized Worst Case |
| ------------ | ------------ | -------------------- |
| k in d       | O(1)         | O(n)                 |
| Copy[3]      | O(n)         | O(n)                 |
| Get Item     | O(1)         | O(n)                 |
| Set Item[1]  | O(1)         | O(n)                 |
| Delete Item  | O(1)         | O(n)                 |
| Iteration[3] | O(n)         | O(n)                 |
