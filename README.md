# Evolutionary Human
A project by AlbertUnruh


## The Idea Behind This
The idea was it to create an animation (not visual,just in the terminal) of the human.
I try to animate behavior and evolution based on some [properties][] for each individual
and the results 'll be displayed in the terminal.


## Properties For The Individuals
The following properties are used 
for better understanding you can take a look into the [property notes][]):
- happiness
- hunger
- thirst
- in-love (only used where ``sexuality`` [!=][] ``asexual``)
  - ``person``
- pregnant (only used where ``gender`` [==][] ``female``)
  - (``since`` <- won't be required because the program cycles one year.
    In the cycle after the woman gets pregnant she's going to receive a baby)
- gender
  - ``male``
  - ``female``
  - ``non-binary``
  - ``genderless``
- sexuality
  - ``heterosexual``
  - ``homosexual``
  - ``bisexual``
  - ``pansexual``
  - ``asexual``
- age
- money
- IQ
- family
  - ``parents``
  - ``children``


### Notes On The Properties
The properties ``happiness``, ``hunger`` and ``thirst`` are values between ``0``
and ``1``.

While I was naming ``sexuality`` as a property I didn't mention ``romantic``.
This is so because I want it not *too* complex at the moment. Eventually I'll
implement ``romantic`` in a later version.

When a person is an adult (21 and older) the ``money`` plays a big role. The person 'll
automatically have a job and the cash the person receives depends on the ``IQ``.
If the person has a high ``IQ`` the person 'll have more money than a person with a
lower ``IQ``.

The ``happiness`` is also affected by money (from the parents if they're still kids
(20 and younger), ``hunger`` and ``thirst``).
Worth mentioning is that a relationship (two persons love each other) increases the
``happiness`` and loving a person without a relationship decreases it.
It should be mentioned that a too low ``happiness`` can end in depression and suicide.

The behavior of ``hunger`` and ``thirst`` depend on the money and are mostly high.
They decrease only if food and water are too expensive (the prices only explodes when
the [worker-population-ratio][] is too low).

About the love I have only one thing to say: it's wonderful!
And a person has a 




[properties]: #properties-for-the-individuals
[property notes]: #notes-on-the-properties
[==]: # "A is equal to B"
[!=]: # "A is not qual to B"
[worker-population-ratio]: # "WORKER / POPULATION = RATIO"
