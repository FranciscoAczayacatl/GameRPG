from app.movements.constants import ATTASCKS_ERROR_CODE, MOVES_ERROR_CODE, ERROR_MESSAGES


class MoveBaseException(Exception):
    def __init__(self, code: int, msg: str, extra=None):
        self.code = code
        self.msg = msg
        self.extra = extra

class MovesError(MoveBaseException):
    
    code = MOVES_ERROR_CODE

    def __init__(self):
        self.msg = ERROR_MESSAGES[self.code]
        super().__init__(self.code, self.msg)

class AttascksError(MoveBaseException):
    
    code =ATTASCKS_ERROR_CODE

    def __init__(self):
        self.msg = ERROR_MESSAGES[self.code]
        super().__init__(self.code, self.msg)