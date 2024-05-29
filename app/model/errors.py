class BarCodeError(Exception):
    pass


class InvalidCodeStructureError(BarCodeError):
    pass


class InvalidControlDigitError(BarCodeError):
    pass