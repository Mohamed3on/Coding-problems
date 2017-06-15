times = int(input())
inputs = [0 for x in range(times)]
outputs = ["INSOMNIA" for x in range(times)]
for i in range(times):
    inputs[i] = input()

for j in range(times):
    reached = False
    seen = set()
    i = 1
    original = inputs[j]
    if original == '0': continue
    number = inputs[j]
    while not reached:
        for ch in number:
            digit = int(ch)
            if digit not in seen:
                seen.add(digit)
        if len(seen) == 10:
            outputs[j] = int(number)
            reached = True
        else:
            i += 1
            number = str(int(original) * i)
for i in range(len(outputs)):
    print('Case #' + str(i + 1) + ': ' + str(outputs[i]))
