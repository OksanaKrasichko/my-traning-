

my_dict = {'grisha':1991, 'Oleg':2006, 'Valera':2011}
print(my_dict)
print(my_dict.get('grisha'))
print(my_dict.get('Bogdan'))
my_dict.update({'Jonah':1997,
                'bogdan':1998})
print(my_dict)
my_dict.pop('Valera')
print(my_dict)

my_set = {3, 2, 4, 3, 2, 4, 'Gaver',(324)}
fag_ = [2,2,3,4,4,3 ]
fag_ = set(fag_)
print(fag_)
fag_.discard(2)
fag_.add((9,5))
print(fag_)