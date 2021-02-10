def test_func(arguments, function, expected=None):
    print(f'Testing function {function.__name__} with arguments:')
    for arg in arguments:
        print('\t', arg, sep = '')
    print(f'Output: {function(*arguments)}')
    if expected is not None:
        print(f'Expected: {expected}')
