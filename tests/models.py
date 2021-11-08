import typing
import unittest
from EvolutionaryHuman import models


T = typing.TypeVar("T")


def generator(*args: T) -> T:
    for arg in args:
        yield arg


class TestModels(unittest.TestCase):
    def test0_gender(self):
        with self.assertRaises(AssertionError):
            models.Gender(
                None,
            )

        gender = models.Gender(
            "male",
        )

        self.assertEqual(
            gender.type,
            "male",
        )

    def test1_sexuality(self):
        with self.assertRaises(RuntimeError):
            models.Sexuality(
                "homosexual",
                models.Gender(
                    "male",
                ),
            )

        models.Sexuality.setup(
            gender_cls=models.Gender,
        )

        with self.assertRaises(AssertionError):
            models.Sexuality(
                None,
                None,
            )

        sexuality = models.Sexuality(
            "homosexual",
            models.Gender(
                "male",
            ),
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

    def test2_person(self):
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

        models.Person.setup(
            family_cls=models.Family,
        )
        # if the test ``test1_sexuality`` hasn't run
        if models.Sexuality.setup_missing():
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

        person = models.Person(
            gender=models.Gender(
                "male",
            ),
            sexuality=(
                sexuality := models.Sexuality(
                    "homosexual",
                    (
                        gender := models.Gender(
                            "male",
                        )
                    ),
                )
            ),
            name="TestCase",
            iq=42,
        )

        self.assertNotEqual(person.alive, person.dead)

        self.assertTrue(
            person.is_lgbtiq()
        )  # since ``person.sexuality`` is "homosexual"

        self.assertIsInstance(
            models.Person.create_person(
                gender=gender,
                sexuality=sexuality,
                name="TestCase",
                iq=42,
            ),
            models.Person,
        )

    def test4_family(self):
        with self.assertRaises(AssertionError):
            models.Family(
                parents=[-1],
            )

        with self.assertRaises(AssertionError):
            models.Family(
                parents=range(42),
            )

        family = models.Family(
            parents=generator(
                "Parent 1",
                "Parent 2",
            ),
        )

        self.assertEqual(
            family.parents,
            {"Parent 1", "Parent 2"},
        )

        family = models.Family(
            parents=(
                person := models.Person(
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
            ),
        )
        self.assertEqual(
            family.parents,
            {person.id},
        )


if __name__ == "__main__":
    unittest.main()
