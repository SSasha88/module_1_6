 # Работа со словарями:
my_dict = {'Sasha':1988,'Ivan':1985,'Olga':1991}
print(type(my_dict))
print('Dictionary:', my_dict)
print('Existing value "Sasha":', my_dict['Sasha'])
print('Not existing value "Marina":',my_dict.get('Marina'))
my_dict.update({'Artem':1973,'Nikita':2001})
delete = my_dict.pop('Sasha')
print('Deleted value "Sasha":', delete)
print('Modified dictionary:',my_dict)
 # Работа с множествами:
my_set = {1,1,3,3,4,4,'one','two','one'}
print(type(my_set))
print('Set',my_set)
my_set.remove(4)
my_set.add('zero')
print('Modified set:',my_set)
