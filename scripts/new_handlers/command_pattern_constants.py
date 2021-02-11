TYPE_SPEC_OPEN = '<'
TYPE_SPEC_CLOSE = '>'
TYPE_SPEC_SEP = ':'
PATT_SPEC_OPEN = '('
PATT_SPEC_CLOSE = ')'

VALID_LITERAL_CHARS = set(
    "abcdefghijklmnopqrstuvwxyz" +
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + 
    "0123456789_" +
    " "
)

# type spec string to type converters/
# constructors
TYPE_SPEC_TYPES = {
    'string': str,
    'int': int,
    'float': float
}

# default type constructor
DEFAULT_TYPE = str
