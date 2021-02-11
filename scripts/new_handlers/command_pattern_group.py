from .command_pattern_constants import TYPE_SPEC_TYPES as TYPES
from .command_pattern_constants import DEFAULT_TYPE

'''
simple group class

needs functionality:

group = Group('var_name', static=True, type=int)
'''
class Group:
    def __init__(self, name, static = False, type_name = ''):
        self.name = name
        self.static = static
        self.type = TYPES[type_name] if type_name in TYPES else DEFAULT_TYPE
