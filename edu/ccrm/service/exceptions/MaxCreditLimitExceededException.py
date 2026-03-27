# edu/ccrm/service/exceptions/MaxCreditLimitExceededException.py

class MaxCreditLimitExceededException(Exception):
    def __init__(self, message):
        super().__init__(message)