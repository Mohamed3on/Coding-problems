current = int(input())
needed = 0
maxcalls = 0
n = int(input())
start = [0] * n
end = [0 for j in range(n)]
for i in range(0, n):
    a, b = map(int, input().split())
    start[i] = a
    end[i] = b
start.sort()
end.sort()
while start and end:
    if start[0] < end[0]:
        needed += 1
        maxcalls = max(maxcalls, needed)
        del start[0]
    else:
        needed -= 1
        del end[0]
while start:
    needed += 1
    maxcalls = max(maxcalls, needed)

print(maxcalls - current)
