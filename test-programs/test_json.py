# This is a program to test json I/O.

import json
def test_run():
    #import json
    result = []
    with open('testfile3', 'r') as f:
        result = json.load(f)
    return result
