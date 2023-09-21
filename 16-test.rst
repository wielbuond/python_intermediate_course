

Test Doctest
============
* Tests are always the most up-to-date code documentation
* Tests cannot get out of sync from code
* Checks if function output is exactly as expected
* Useful for regex modifications
* Can add text (i.e. explanations) between tests


Docstring
---------
* Docstring is a first multiline comment in: File/Module, Class, Method/Function
* Used for generating ``help()`` documentation
* It is accessible in ``__doc__`` property of an object
* Used for ``doctest``
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters
* More information in `Function Doctest`


Syntax
------
* Docstring is a first multiline comment in: File/Module, Class, Method/Function
* Used for generating ``help()`` documentation
* It is accessible in ``__doc__`` property of an object
* Used for ``doctest``
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three double quote (``"""``) characters


Running Tests
-------------


Test Int, Float
---------------


Test Bool
---------


Test Str
--------
* Python will change to single quotes in most cases
* Python will change to double quotes to avoid escapes
* ``print()`` function output, don't have quotes


Test Ordered Sequence
---------------------


Test Unordered Sequence
-----------------------


Test Mapping
------------


Test Nested
-----------


Test Exceptions
---------------


Test Type
---------


Test Python Expressions
-----------------------


Flags
-----
* ``DONT_ACCEPT_TRUE_FOR_1``
* ``DONT_ACCEPT_BLANKLINE``
* ``NORMALIZE_WHITESPACE``
* ``ELLIPSIS``
* ``IGNORE_EXCEPTION_DETAIL``
* ``SKIP``
* ``COMPARISON_FLAGS``
* ``REPORT_UDIFF``
* ``REPORT_CDIFF``
* ``REPORT_NDIFF``
* ``REPORT_ONLY_FIRST_FAILURE``
* ``FAIL_FAST``
* ``REPORTING_FLAGS``


Test Unittest
=============
* https://martinfowler.com/articles/microservice-testing/#testing-component-out-of-process-diagram
* https://docs.python.org/3/library/unittest.mock.html


Glossary
--------


Running tests with your IDE
---------------------------
* View menu -> Run... -> Unittest in ``myfunction``


From code
---------


From command line
-----------------


Methods
-------
* ``self.assertEqual()``
* ``self.assertAlmostEqual(0.1+0.2, 0.3, places=16)``
* ``self.assertTrue()``
* ``self.assertFalse()``
* ``self.assertDictEqual()``
* ``self.assertIn()``
* ``self.assertIs()``
* ``self.assertIsInstance()``
* ``self.assertIsNotNone()``
* ``self.assertRaises()``


Mock
----
* Mock and MagicMock objects create all attributes and methods as you access them and store details of how they have been used.


Side effect
-----------
* Raising an exception when a mock is called


patch
-----
* The object you specify will be replaced with a mock (or other object) during the test and restored when the test ends


Stub
----
* writing classes or functions but not yet implementing them
* After you have planned a module or class, for example by drawing it's UML diagram, you begin implementing it.
* As you may have to implement a lot of methods and classes, you begin with stubs.
* This simply means that you only write the definition of a function down and leave the actual code for later.
