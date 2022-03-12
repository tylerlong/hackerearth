## Notes

- Ref: https://www.hackerrank.com/challenges/three-month-preparation-kit-merging-communities/problem
- How to use an unhashable object as map key: 

```python
s = set()
l = []
s.add(id(l))
print(id(l) in s)
```
So `id(s)` is to get the address/pointer/reference ID to an object.
