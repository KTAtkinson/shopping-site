"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this
    def __init__(self, firstname, lastname, email, password):
        """Initialize Ubermelon customer class."""

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        class_info = str(self.__class__)
        return "{}, first name: {}, last name: {}{}".format(class_info[:-1],
                                                            self.firstname,
                                                            self.lastname,
                                                            class_info[-1])


def get_customer_info():
    """Returns a dictionary of customer info keyed by email."""
    
    customers = {}
    with open('customers.txt') as customer_file:
        for customer in customer_file:
            customer = customer.rstrip()
            (firstname,
             lastname,
             email,
             password) = customer.split('|')
            customers[email] = Customer(firstname, lastname, email, password)

    return customers


def get_by_email(email):
    """Given an email, retrieves customer data from records."""

    customer = get_customer_info().get(email, None)

    if customer:
        return customer

    raise NoSuchCustomerError


class NoSuchCustomerError(KeyError):
    """No customer was found."""

    def __init__(self):
        return super(NoSuchCustomerError, self).__init__("No customer found.")
