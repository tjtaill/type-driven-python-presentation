"""
Value Objects
"""
from collections import namedtuple
from validate_email import validate_email
from collections import namedtuple


class EmailAddress(namedtuple("ImmutableValue", "val")):
    def __init__(self, val: str) -> None:
        pass  # just so you can't pass None or non str types to constructor

    def __new__(cls, val: str):
        if not validate_email(val):
            raise ValueError(f"{val} is not a valid email address")
        return super().__new__(cls, val)


def email_notification(email_address: EmailAddress) -> None:
    pass


EmailAddress(None)  # won't type check
EmailAddress("not_valid_email")  # throws exception
valid_email = EmailAddress("foo@bar.com")  # ok
email_notification(valid_email)
email_notification("foo@bar.com")  # send_email doesn't except strings
