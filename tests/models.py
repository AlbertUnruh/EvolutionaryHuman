import typing
import unittest
from EvolutionaryHuman import models


T = typing.TypeVar("T")


def generator(*args: T) -> T:
    for arg in args:
        yield arg


class TestModels(unittest.TestCase):
    def test0_setup(self):
        with self.assertRaises(RuntimeError):
            models.Person(
                gender=models.Gender(
                    "male",
                ),
                sexuality=models.Sexuality(
                    "homosexual",
                    models.Gender(
                        "male",
                    ),
                ),
                name="TestCase",
                iq=42,
            )
        with self.assertRaises(RuntimeError):
            models.Sexuality(
                "homosexual",
                models.Gender(
                    "male",
                ),
            )

        models.Person.setup(
            family_cls=models.Family,
        )
        models.Sexuality.setup(
            gender_cls=models.Gender,
        )

        models.Person(
            gender=models.Gender(
                "male",
            ),
            sexuality=models.Sexuality(
                "homosexual",
                models.Gender(
                    "male",
                ),
            ),
            name="TestCase",
            iq=42,
        )
        models.Sexuality(
            "homosexual",
            models.Gender(
                "male",
            ),
        )

    def test1_create(self):
        models.Person.setup(
            family_cls=models.Family,
        )
        models.Sexuality.setup(
            gender_cls=models.Gender,
        )

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
        family = models.Family(
            parents=generator("Parent 1", "Parent 2"),
        )
        self.assertEqual(
            family.parents,
            {"Parent 1", "Parent 2"},
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
            {person.id},
        )


if __name__ == "__main__":
    unittest.main()
