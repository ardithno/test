def search_zero(mass):
    if  isinstance(mass, list) or isinstance(mass, tuple):
        mass = ''.join([str(i) for i in mass])
    print(mass.index('0'))


'''Tests:
search_zero('1111110001111010101111000111')
search_zero('10')
search_zero([1, 1, 0, 0])
search_zero(['1', '1', '1', '0', '1'])
search_zero((1,1,1,1,0))'''