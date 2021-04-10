def rotate(_array: list):
    print('Input matrix: ', *['\t'.join(map(str, _x)) for _x in _array], sep='\n\t')
    _array.reverse()
    _result_array = \
        [[_array[_external][_internal] for _external in range(len(_array))] for _internal in range(len(_array[0]))]
    print('\nOutput matrix: ', *['\t'.join(map(str, _x)) for _x in _result_array], sep='\n\t')
