class UserException(Exception):
    def __init__(self, message="", data=None, error: bool = True, status_code: int = 400):
        self.message = message
        self.data = data
        self.error = error
        self.status_code = status_code
        super().__init__(self.message)
