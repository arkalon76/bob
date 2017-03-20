from binary import Binary

def test_binary_init_int():
    binary = Binary(6)
    assert int(binary) == 6
