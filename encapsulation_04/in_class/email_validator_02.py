"""
Create a class called EmailValidator. Upon initialization it should receive min_length
(of the username; example: in "peter@gmail.com" "peter" is the username),
mails (list of the valid mails; example: "gmail", "abv"), domains (list of valid domains; example: "com", "net").
Create three private methods:
    • validate_name(name) - returns whether the name is greater than or equal to the min_length (True/False)
    • validate_mail(mail) - returns whether the mail is in the possible mails list (True/False)
    • validate_domain(domain) - returns whether the domain is in the possible domains list (True/False)
Create one public method:
    • validate(email) - using the three private methods returns whether the email is valid (True/False)
"""
class EmailValidator:

    def __init__(self, length_username: int, mails_list: list, domains_list: list):
        self.min_length: int = length_username
        self.mails: int = mails_list
        self.domains: int = domains_list

    def __validate_name(self, name):
        return name and len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains


    def validate(self, email):
        username = email.split("@")[0]
        mail = email.split("@")[1].split(".")[0]
        domain = email.split("@")[1].split(".")[1]
        return self.__validate_domain(domain) and\
               self.__validate_mail(mail) and\
               self.__validate_name(username)

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("peter77@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

