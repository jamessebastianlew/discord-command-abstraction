import re
import sys
from . import command_pattern_helpers as CPHelpers
"""

patterns:
       unit1                  unit2
    r'literal <var_type:var_name>({regex_pattern})'
    -> r'literal {regex_pattern}'

    processes into

    pattern_groups = [
        Group
            static: True,
            type: var_type,
            name: var_name
    ]

    which captured groups can refer to for
    translation of types

    <var_type:var_name> is the type specifier (TYPE_SPEC)
    ({regex_pattern}) is the pattern specifier (PATT_SPEC)

functionality:
    command_pattern = CommandPattern(pattern)
    command_pattern.get_match(text)

"""

class CommandPattern:
    @staticmethod
    def process_groups(pattern):
        '''
        outputs a list of Group objects for each
        variable input in the pattern

        e.g.

        pattern = r'say <string:something>(\w+)'
        returns [ Group('something', static=True, type_name = 'string') ]
        '''
        pattern_units = CPHelpers.split_units(pattern)
        
        pattern_groups = []
        for unit in pattern_units:
            group = CPHelpers.get_unit_group(unit)
            if group is not None:
                pattern_groups.append(group)
        
        return pattern_groups


    @staticmethod
    def process_regex(pattern):
        '''
        changes a given command pattern into its regex
        counterpart

        returns a string representing the output regex pattern
        '''
        pattern_units = CPHelpers.split_units(pattern)
        list_unit_expressions = map(CPHelpers.get_unit_regex, pattern_units)
        return ''.join(list_unit_expressions)


    def get_match(self, text):
        '''
        considers a string `text` and compares it to the
        regular expression `self.regex_obj`

        returns an object with all the groups mapped to their
        appropriate values (if convertible)

        otherwise returns None 

        in the case of a conversion error raises an error

        e.g.

        pattern = r'multiply <int:a>(\d+) <int:b>(\d+)'
        text = 'multiply 10 11'

        returns 
        {
            'a': 10,
            'b': 11
        }

        
        '''
        match_obj = self.regex_obj.fullmatch(text)
        if match_obj is None:
            return None

        match_args = {}
        for group in self.pattern_groups:
            try:
                match_args[group.name] = group.type(match_obj.group(group.name))
            except:
                raise Exception('Unexpected error: Likely converting group type')

        return match_args


    def __init__(self, pattern):
        self.pattern_groups = CommandPattern.process_groups(pattern)
        self.regex_obj = re.compile(CommandPattern.process_regex(pattern))


if __name__ == '__main__':
    compat = CommandPattern(r'say <string:something>(\w+)')
    print(compat.pattern_groups)
    print(compat.get_match('say poop'))



