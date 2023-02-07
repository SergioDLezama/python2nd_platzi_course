def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Facundo', 'lastname': 'Garcia'}

    superlist = [
        {'firstname': 'Facundo', 'lastname': 'Garcia'},
        {'firstname': 'Sergio', 'lastname': 'Lezama'},
        {'firstname': 'Mathias', 'lastname': 'Arroyave'},
        {'firstname': 'Maxi', 'lastname': 'Blanco'},
        {'firstname': 'Liliana', 'lastname': 'Perez'},
    ]

    superdict = {
        'natural_nums': [1,2,3,4,5],
        'integrer_nums': [-1,-2,0,1,2],
        'floating_nums': [1.1,4.5,6.43],
    }

    for key, value in superdict.items():
        print(key, ' ', value)

    for i in superlist:
        for key, values in i.items():
            print(key, ' ', values)
    
    for item in superlist:
    print(item["firstname"] , "-" , item["lastname"])

if __name__ == '__main__':
    run()