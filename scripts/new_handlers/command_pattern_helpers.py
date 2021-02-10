# TYPE_SPEC and PATT_SPEC
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


def is_valid_literal(unit):
    return all(char in VALID_LITERAL_CHARS for char in unit)


def is_valid_unit(unit):
    # unit literals must only contain letters and numbers
    if not unit.startswith(TYPE_SPEC_OPEN):
        return is_valid_literal(unit)

    # unit variables must have a valid type specifier
    open_char, close_char = TYPE_SPEC_OPEN, TYPE_SPEC_CLOSE
    end_type_spec = get_end_bracket(unit, 0, open_char, close_char)

    if end_type_spec is None:
        return False

    type_spec = unit[:end_type_spec + 1]
    # and the type specifier must have at most one seperator
    if type_spec.count(TYPE_SPEC_SEP) > 1:
        return False

    # and the words between can only consist of valid literal characters
    type_spec_words = type_spec[1:-1].split(TYPE_SPEC_SEP)
    if not all(is_valid_literal(word) for word in type_spec_words):
        return False

    
    # and if the unit has a type it must be in the TYPE_SPEC_TYPES dictionary
    if len(type_spec_words) == 2 and type_spec_words[0] not in TYPE_SPEC_TYPES:
        return False


    patt_spec = unit[end_type_spec + 1:]
    # unit variables must have a valid pattern specifier
    if not patt_spec[0] == PATT_SPEC_OPEN not patt_spec[-1] == PATT_SPEC_CLOSE:
        return False

    # CONT: patterns must have valid regex?

    return True


# unit helpers
def is_group_unit(unit):
    '''
    considers a VALID unit as an argument
    returns True if the unit is a capturable group
    and False otherwise
    '''
    return unit.startswith(TYPE_SPEC_OPEN)


def get_unit_type_spec(unit):
    '''
    considers a VALID unit as an argument

    returns the type specifier of the group if the unit has one
    otherwise returns None
    (only requires a type spec to be at the start of the string)
    '''
    if not is_group_unit(unit):
        return None

    end = unit.get_end_bracket(unit, 0, TYPE_SPEC_OPEN, TYPE_SPEC_CLOSE)
    return unit[:end + 1]


def get_type_spec_pair(unit):
    '''
    considers a VALID unit as an argument

    returns a pair containing the variable type
    and the variable name as strings

    e.g. returns (type: str, name: str)
    '''
    type_spec = get_unit_type_spec(unit)

    stripped_spec = type_spec[1:-1]
    split_spec = stripped_spec.split(TYPE_SPEC_SEP)
    
    if len(split_spec) == 2:
        return tuple(split_spec)

    return (None, *split_spec)


def get_patt_spec(unit):
    '''
    considers a VALID unit as an argument
    returns the pattern specifier
    '''
    patt_open_ind = unit.find(PATT_SPEC_OPEN)
    return unit[patt_open_ind:]
    


def get_unit_expression(unit):
    '''
    considers a VALID unit as an argument
    returns the unit converted into a expression
    '''

    # literals are already expressions
    if not is_group_unit(unit):
        return unit

    # variables must be translated
    # <var_type:var_name>(pattern) to (?P<var_name>pattern)
    type_spec_pair = get_type_spec_pair(unit)
    patt_spec = get_patt_spec(unit)

#CONT
    

    pass
    

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

    for unit in output_units:
        assert is_valid_unit(unit)

    return output_units


