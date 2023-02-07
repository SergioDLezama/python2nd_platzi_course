def run():
    squares = []
#    for i in range(1, 101):
#        i = i**2
#        if i % 3 == 0:
#            pass
#        else:
#            squares.append(i)
#            #squares.append(i**2)
   
#    for i in range(1, 101):
#        if i % 3 != 0:
#            squares.append(i**2)

    #squares = [i**2 for i in range(1,101) if i%3 != 0]
    #print(squares)

    squares = [i for i in range(1,99999) if i % 36 == 0]
    print(squares)

if __name__ == '__main__':
    run()