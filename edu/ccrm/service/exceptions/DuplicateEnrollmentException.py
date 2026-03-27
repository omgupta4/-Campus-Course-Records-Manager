# edu/ccrm/service/exceptions/DuplicateEnrollmentException.py

class DuplicateEnrollmentException(Exception):
    def __init__(self, message):
        super().__init__(message)