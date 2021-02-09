import re

"""

patterns:
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


functionality:
    command_pattern = CommandPattern(pattern)
    command_pattern.matches(expr)
    command_pattern.get_args(expr)

"""

class CommandPattern:
    @staticmethod
    def process_groups(pattern):
        pass


    @staticmethod
    def process_expression(pattern):
        pass


    def __init__(self, pattern):
        self.pattern_groups = CommandPattern.process_groups(pattern)
        self.expression = CommandPattern.process_expression(pattern)
