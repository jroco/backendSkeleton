class User:
    def __init__(self, nick=None, firstName=None, lastName=None, email=None, phoneNumber=None, business=None, enterprise=None, pwd=None, userType="Normal"):
        self.nick = nick
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNumber = phoneNumber
        self.business = business
        self.enterprise = enterprise
        self.pwd = pwd
        self.userType = userType

    def __repr__(self):
        return f"User(nick={self.nick}, firstName={self.firstName}, lastName={self.lastName}, email={self.email}, phoneNumber={self.phoneNumber}, business={self.business}, enterprise={self.enterprise}, userType={self.userType})"