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
- in-love (only used where ``sexuality`` [!=][] ``asexual``)
  - ``person``
- married
  - ``person``
- pregnant (only used where ``gender`` [==][] ``female``)
  - (``since`` <- won't be required/used because the program cycles one year.
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
- name


### Notes On The Properties
The properties ``happiness`` and ``hunger`` are values between ``0``
and ``1``.

While I was naming ``sexuality`` as a property I didn't mention ``romantic``.
This is so because I want it not *too* complex at the moment. Eventually I'll
implement ``romantic`` in a later version.

When a person is an adult (21 and older) the ``money`` plays a big role. The person 'll
automatically have a job and the cash the person receives depends on the ``IQ``.
If the person has a high ``IQ`` the person 'll have more money than a person with a
lower ``IQ``.

The ``happiness`` is also affected by money (from the parents if they're still kids
(20 and younger) and ``hunger``).
Worth mentioning is being part of a couple increases the ``happiness`` and loving a
person without a relationship decreases it. It should be mentioned that a too low
``happiness`` can end in depression and suicide.

The behavior of ``hunger`` depends on the money and is mostly high.
It decreases only if food is too expensive (the price only explodes when
the [worker-population-ratio][] is too low).

About the love I have only one thing to say: it's wonderful!
If a couple is in a heterosexual-relationship there is a chance that the woman
gets pregnant. While she's pregnant she can't work.

Children don't have any money which affects their ``happiness``, but the money from
the parents affects this property.
If a children looses both parents the children 'll be adopted by another couple. This
automatically adds the new parents to the ``parents`` and the children 'll also be
added to the ``children``-property from the couple.

For two persons to happen to be a couple they just need to be ``in-love``, but at the
same time and for the marriage they have to spend some money (in %).

And to be nice every person has a ``name`` **:)**.





[properties]: #properties-for-the-individuals
[property notes]: #notes-on-the-properties
[==]: # "A is equal to B"
[!=]: # "A is not qual to B"
[worker-population-ratio]: # "WORKER / POPULATION = RATIO"
