

Math IEEE-754
=============


Problem
-------
* Source: [#PyDocFloatingPoint]_


IEEE 754 standard
-----------------


Floats in Doctest
-----------------


Decimal Type
------------


Solutions
---------
* Round values to 4 decimal places (generally acceptable)
* Store values as ``int``, do operation and then divide. For example instead of 1.99 USD, store price as 199 US cents
* Use ``Decimal`` type
* ``Decimal`` type is much slower


Math Random
===========


``random``
----------


Pseudo and Pure random numbers
------------------------------
* What are pseudorandom numbers?
* Why it is not possible to generate a pure random number?
* What is ``random.seed(0)``?
