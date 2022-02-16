import sys

lines = [line.strip() for line in sys.stdin]

q = []
for line in lines[1:]:
    if line == 'D':
      i = q.pop(0) if len(q) > 0 else -1
      print('{} {}'.format(i, len(q)))
    elif line.startswith('E '):
      i = line[2:]
      q.append(i)
      print(len(q))
