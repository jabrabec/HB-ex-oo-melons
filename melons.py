"""This file should have our order classes in it."""
from random import randint
import datetime as d

class AbstractMelonOrder(object):
    """A melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_time = d.datetime.now()

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
        if d.date.weekday(self.order_time) <= 4:  #  Implement rush hour pricing
            order_time = self.order_time.hour * 100 + self.order_time.minute
            if order_time >= 800 and order_time <= 1100:
                base_price += 4
        return base_price

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code


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

    order_type = "government"
    tax = 0.00
    passed_inspection = False

    def mark_inspection(self, passed):
        """Takes boolean value 'passed' and updates passed_inspection attribute"""

        self.passed_inspection = passed
