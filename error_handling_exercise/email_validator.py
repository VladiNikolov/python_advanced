class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "org", "net"]

input_line = input()

while input_line != "End":
    email_address = input_line
    email_address_parts = email_address.split("@")

    if len(email_address_parts) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    user_name = email_address_parts[0]
    domain_name = email_address_parts[1]

    if len(user_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = domain_name.split('.')[-1]

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    input_line = input()













