import unittest
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def details(self):
        detail = f"{self.name}  {self.age}"
        return detail
    def calculate(self,amount):
        return self.age + amount
    def calculate_amount(self,amount1):
        return self.age + amount1
    def calculate_amount_all(self):
        show_amount = self.calculate_amount(32) + self.calculate(32)
        return show_amount


person1 = Person("urim cocaj",31)
print(person1.get_name() + " " + str(person1.get_age()))
print(person1.get_age())
print(person1.details())
print(person1.calculate(18))
print(person1.calculate_amount(22))
print(person1.calculate_amount_all())


#from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Urim", 32)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), "Urim")

    def test_set_name(self):
        self.person.set_name("Ilir")
        self.assertEqual(self.person.get_name(), "Ilir")

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), 32)

    def test_set_age(self):
        self.person.set_age(33)
        self.assertEqual(self.person.get_age(), 33)

    def test_details(self):
        self.assertEqual(self.person.details(), "Urim 32")

    def test_calculate(self):
        self.assertEqual(self.person.calculate(10), 42)

    def test_calculate_amount(self):
        self.assertEqual(self.person.calculate_amount(10), 42)

    def test_calculate_amount_all(self):
        self.assertEqual(self.person.calculate_amount_all(), 100)

if __name__ == '__main__':
    unittest.main()

