for num in range(1, 101):
    output = ''
    if num % 3 == 0:
        output += 'Bucks'
    if num % 5 == 0:  # no more elif
        output += 'Fizz'
    if not output:  # check if msg is an empty string
        output = str(num)
    print(output)
