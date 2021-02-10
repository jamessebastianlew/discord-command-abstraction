'''
simple group class

needs functionality:

group = Group('var_name', static=True, type='int')
'''
class Group:
    def __init__(self, name, static = False, type_name = ''):
        self.name = name
        self.static = static
        self.type_name = type_name
