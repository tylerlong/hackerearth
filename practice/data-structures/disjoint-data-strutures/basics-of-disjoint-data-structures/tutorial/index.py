import sys

inputs = [line.strip() for line in sys.stdin]
n = int(inputs[0].split(' ')[0])
map = {i: [i] for i in range(1, n + 1)}
for line in inputs[1:]:
  [i, j] = [int(i) for i in line.split(' ')]
  if map[i] == map[j]:
    continue
  [bigger, smaller] = [map[i], map[j]] if len(map[i]) >= len(map[j]) else [map[j], map[i]]
  for k in smaller:
    bigger.append(k)
    map[k] = bigger
  checked = set()
  result = []
  for k in map:
    if(id(map[k]) in checked):
      continue
    result.append(len(map[k]))
    checked.add(id(map[k]))
  print(' '.join([str(i) for i in sorted(result)]))
