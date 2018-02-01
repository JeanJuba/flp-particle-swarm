import copy

class Teste:

    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return 'Valor %d' % self.value


t = Teste(10)
list = []
list.append(t)

print(list[0].value)


'''
t = Teste(5)
print('t ', t)
t.value = 6
print('t ', t)

t1 = copy.copy(t)
print('t1 ',  t1)
t1.value = 7
print('t1 ', t1)
print('t ', t)
'''
