import re
from command_pattern_helpers import split_unit, get_unit_type_spec

"""

patterns:
       unit1                  unit2
    r'literal <var_type:var_name>({regex_pattern})'
    -> r'literal {regex_pattern}'

    processes into

    pattern_groups = [
        {
            'static': True,
            'type': var_type,
            'name': var_name
        }
    ]

    which captured groups can refer to for
    translation of types

    <var_type:var_name> is the type specifier (TYPE_SPEC)
    ({regex_pattern}) is the pattern specifier (PATT_SPEC)

functionality:
    command_pattern = CommandPattern(pattern)
    command_pattern.matches(expr)
    command_pattern.get_args(expr)

"""

class CommandPattern:
    @staticmethod
    def process_groups(pattern):
        pattern_units = split_units(pattern)
        
        pattern_groups = []
        for unit in pattern_units:
            group = get_unit_group(unit)
            if group is not None:
                pattern_groups.append(group)


    @staticmethod
    def process_expression(pattern):
        pattern_units = split_units(pattern)


    def __init__(self, pattern):
        self.pattern_groups = CommandPattern.process_groups(pattern)
        self.expression = CommandPattern.process_expression(pattern)
