from command_pattern_constants import *

# invisible helper functions
def get_end_bracket(pattern, start, open_char, close_char):
    '''
    returns the matching end bracket to the open brackets
    starting at `start`
    '''
    assert pattern[start] == open_char
    
    open_count = 0 # number of unclosed open brackets
    
    # trace the bracket count until an end bracket is found
    for i in range(start, len(pattern)):
        # take the character
        if pattern[i] == open_char:
            open_count += 1
        elif pattern[i] == close_char:
            open_count -= 1

        # check if it closes the initial bracket
        if open_count == 0:
            return i

    return None


def is_group_unit(unit):
    '''
    returns True if the unit is a capturable group
    and False otherwise
    '''
    return unit.startswith(TYPE_SPEC_OPEN)


def get_unit_type_spec(unit):
    '''
    returns the type specifier of the group if the unit has one
    otherwise returns None
    '''
    if not is_group_unit(unit):
        return None

    end = unit.get_end_bracket(unit, 0, TYPE_SPEC_OPEN, TYPE_SPEC_CLOSE)
    return unit[:end + 1]


def get_type_spec_pair(type_spec):
    stripped_spec = type_spec[1:-1]
    split_spec = stripped_spec.split(TYPE_SPEC_SEP)
    
    if len(split_spec) == 2:
        return tuple(split_spec)

    return 



        


def get_type_spec_type(type_spec):
    if not TYPE_SPEC_SEP in type_spec:
        return None

    return type_spec.split(TYPE_SPEC_SEP)[0]


def get_type_spec_name(type_spec):
    if not TYPE_SPEC_SEP in type_spec:
        return 


def get_unit_expression(unit):
    if not is_group_unit(unit):
        return unit



    
def split_units(pattern):
    '''
    returns a list of the function split by units

    e.g.

    input:
        r'literal <int:num>((\d+)) hi<string:name>((\w+))'
    returns
        ['literal ', '<int:num>(\d+)', ' hi', '<string:name>(\w+)']
    '''
    output_units = []

    # pointer to the start of the unprocessed suffix
    process_start = 0
    while process_start < len(pattern):
        if pattern[process_start] == TYPE_SPEC_OPEN:
            end_bracket_pos = get_end_bracket(pattern, process_sart,
                    TYPE_SPEC_OPEN, TYPE_SPEC_CLOSE)

            assert end_bracket_pos < len(pattern)
            assert end_bracket_pos == PATT_SPEC_OPEN

            start_bracket_pos = get_bracket_start
            output_units.append(pattern[process_start : end_bracket_pos + 1])
            process_start = end_bracket_pos + 1

        else:
            next_bracket = pattern.index(TYPE_SPEC_OPEN, process_start)

            if not next_bracket:
                next_bracket = len(pattern)

            output_units.append(pattern[process_start] : next_bracket)
            process_start = next_bracket

    return output_units
