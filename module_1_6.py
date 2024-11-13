 # Работа со словарями:
my_dict = {'Sasha':1988,'Ivan':1985,'Olga':1991}
print('Dictionary:', my_dict)
print('Existing value "Sasha":', my_dict['Sasha'])
print('Not existing value "Marina":',my_dict.get('Marina'))
my_dict.update({'Artem':1973,'Nikita':2001})
delete = my_dict.pop('Sasha')
print('Deleted value "Sasha":', delete)
print('Modified dictionary:',my_dict)
 # Работа с множествами:
my_set = {1,1,3,3,4,4,'one','two','one'}
print('Set:',my_set)
my_set.remove(4)
plus_my_set=['zero','study']
my_set.update(plus_my_set)
print('Modified set:',my_set)