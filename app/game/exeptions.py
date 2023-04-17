
from app.game.constants import ERROR_MESSAGES, GAME_TYPE_ERROR_FILE_CODE


class GameBaseException(Exception):
    def __init__(self, code: int, msg: str, extra=None):
        self.code = code
        self.msg = msg
        self.extra = extra

class GameTypeFileError(GameBaseException):
    
    code = GAME_TYPE_ERROR_FILE_CODE

    def __init__(self):
        self.msg = ERROR_MESSAGES[self.code]
        super().__init__(self.code, self.msg)