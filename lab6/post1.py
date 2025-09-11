def genrate_squares():
    for i in range(1,6):
        yield i 
        for number in genrate_squares():
            print(number)