cases = input()
cases = int(cases)
answers = ["NO"] * cases
for i in range(0, cases):
    n = int(input())
    array = list(map(int, input().split()))
    if len(array) < 2:
        answers[i] = "YES"
        continue
    total = sum(array)
    leftsum = array[0]
    rightsum = total - leftsum
    for j in range(1, n):
        if leftsum == rightsum - array[j]:
            answers[i] = "YES"
            break
        rightsum -= array[j]
        leftsum += array[j]

print("\n".join(answers))
