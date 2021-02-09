import re

TYPE_SPEC_OPEN = '<'
TYPE_SPEC_CLOSE = '>'
TYPE_SPEC_SEP = ':'
PATT_SPEC_OPEN = '('
PATT_SPEC_CLOSE = ')'

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
            if not unit.startswith(TYPE_SPEC_OPEN):
                continue

            # if its a group get the type specifier
            type_spec_end = get_end_bracket(unit, 0,
                    TYPE_SPEC_OPEN, TYPE_SPEC_CLOSE)
            type_spec = unit[:type_spec_end + 1]

            # start a new group object
            group = {}
            assert type_spec.count(TYPE_SPEC_SEP) < 2
            if TYPE_SPEC_SEP in type_spec:


            if group





    @staticmethod
    def process_expression(pattern):
        pattern_units = split_units(pattern)


    def __init__(self, pattern):
        self.pattern_groups = CommandPattern.process_groups(pattern)
        self.expression = CommandPattern.process_expression(pattern)
