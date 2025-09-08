def colltaz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1

while True:       
    try:
        numberInput = int(input('Type random number: '))
        if numberInput > 1:
            break
    except ValueError:
        print('Type correct number')

while numberInput != 1:
    numberInput = colltaz(numberInput)
    print(numberInput)