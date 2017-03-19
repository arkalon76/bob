class NewClass(object):
    """docstring for NewClass."""
    ivar = bytearray([0x44,0x44])

    def __init__(self, arg):
        super(NewClass, self).__init__()
        self.arg = arg
