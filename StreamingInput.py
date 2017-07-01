# Take input separated by newline without knowing the number of lines
lines = []
while True:
    line = input()
    if line:
        lines.append(int(line))
    else:
        break
print(lines)
