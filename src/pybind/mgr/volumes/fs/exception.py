class VolumeException(Exception):
    def __init__(self, error_code, error_message):
        self.errno = error_code
        self.error_str = error_message

    def to_tuple(self):
        return self.errno, "", self.error_str

    def __str__(self):
        return "{0} ({1})".format(self.errno, self.error_str)
