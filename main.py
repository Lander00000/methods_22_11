class User():
    def __init__(username, password, name, shippinginfo, paymentinfo):
        self.username = username
        self.password = password
        self.name = name
        self.shippinginfo = shippinginfo
        self.paymentinfo = paymentinfo
        self.employee = False
    def updateShipping(self, s):
        self.shippinginfo = s
    def updatePayment(self, p):
        self.paymentinfo = p

