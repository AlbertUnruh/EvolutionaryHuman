import unittest
from EvolutionaryHuman import models


class TestModels(unittest.TestCase):
    def test_create(self):
        with self.assertRaises(AssertionError):
            models.Person(
                gender=None,
                sexuality=None,
                name="TestCase",
                iq=-1,
            )

        with self.assertRaises(AssertionError):
            models.Gender(
                None,
            )

        with self.assertRaises(AssertionError):
            models.Sexuality(
                None,
                None,
            )

        with self.assertRaises(AssertionError):
            models.Family(
                parents=[-1],
            )
        with self.assertRaises(AssertionError):
            models.Family(
                parents=range(42),
            )

        gender = models.Gender(
            "male",
        )
        self.assertEqual(
            gender.type,
            "male",
        )

        sexuality = models.Sexuality(
            "homosexual",
            gender,
        )
        self.assertEqual(
            sexuality.type,
            "homosexual",
        )
        self.assertTrue(
            sexuality.can_love(
                gender="male",
            )
        )
        for g in models.genders:
            if g != "male":
                self.assertFalse(
                    sexuality.can_love(
                        gender=g,
                    )
                )
        del g

        person = models.Person(
            gender=gender,
            sexuality=sexuality,
            name="TestCase",
            iq=42,
        )
        self.assertIsInstance(
            models.Person.create_person(
                gender=gender,
                sexuality=sexuality,
                name="TestCase",
                iq=42,
            ),
            models.Person,
        )

        family = models.Family(
            parents=person,
        )
        self.assertEqual(
            family.parents,
            [person.id],
        )


if __name__ == "__main__":
    unittest.main()
