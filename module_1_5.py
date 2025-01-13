immutable_var = (1, 2.4, 'Oleg', 5/6,)
print(immutable_var)

#mmutable_var[0] = 'kabanchiki'  даннай переменной нельзя изменять элементы так как она евляется картежом,не изменяемой переменной
#rint(immutable_var)

mutable_list = ([1, 2,], 3, 'warface')
print(mutable_list)
mutable_list[0][0] = 2
print(mutable_list)