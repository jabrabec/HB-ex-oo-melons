"""This file should have our order classes in it."""
from random import randint

class AbstractMelonOrder(object):
    """A melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        if self.species == "Christmas":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def get_base_price(self):
        """ Implement surge pricing"""

        base_price = randint(5,9)
        return base_price

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price."""

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.order_type = "government"
        self.tax = 0.00
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Takes boolean value 'passed' and updates passed_inspection attribute"""


        self.passed_inspection = passed
