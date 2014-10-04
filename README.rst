#################################
python-diminuendo - HTML minifier
#################################

This is a generic HTML minifier **NOT** using regular expressions. This minifier is fully HTML5 compatible.

The name is coming from the Harry Potter books and is `an incantation that
forces objects to shrink <http://harrypotter.wikia.com/wiki/Diminuendo>`_

This project was started because of the lack of a *maintained* HTML minifier
not using complex regexp. This project uses `beautifulsoup
<http://www.crummy.com/software/BeautifulSoup/>`_ to navigate the HTML flow.

.. image:: https://travis-ci.org/hrbonz/python-diminuendo.svg?branch=master
    :target: https://travis-ci.org/hrbonz/python-diminuendo
    :alt: Testing Status

.. image:: https://readthedocs.org/projects/python-diminuendo/badge/?version=latest
    :target: https://readthedocs.org/projects/python-diminuendo/?badge=latest
    :alt: Documentation Status

.. image:: http://img.shields.io/badge/license-BSD%203--Clause-blue.svg
    :target: http://opensource.org/licenses/BSD-3-Clause
    :alt: license BSD 3-Clause


Install
=======

.. code-block:: sh

    $ pip install python-diminuendo

Usage
=====

**TODO**

HTML minification
-----------------

.. code-block:: python

    >>> from diminuendo import htmlmin
    >>> html = """<html>
        <head>
            <title>Hello World!</title>
        </head>
        <body>
            <p>Good morning</p>
        </body>
    </html>"""
    >>> minified = htmlmin(html)
    >>> print minified
    '<html><head><title>Hello World!</title></head><body><p>Good morning</p></body></html>'

Development
===========

Add a minification test
-----------------------

To add a minification test, simply add the html code as
``test_name.html`` and its minified version as
``test_name-minified.html`` in ``test/html``.

Test
----

Test the package:

.. code-block:: sh

    $ python -m unittest discover

Automatic testing in various environments:

.. code-block:: sh

    $ tox

Release
-------

Use `bumpr` to release the package:

.. code-block:: sh

    $ bumpr -b -m
    [...]
    $ python setup.py sdist bdist_wheel upload

Project
=======

* `Source code on github <https://github.com/hrbonz/python-diminuendo>`_
* `Documentation on readthedocs <http://python-diminuendo.readthedocs.org/>`_
* `Package on pypi <https://pypi.python.org/pypi/python-diminuendo>`_

Other projects
==============

* `django-htmlmin <https://github.com/cobrateam/django-htmlmin>`_
* `htmlmin <https://github.com/mankyd/htmlmin>`_

License
=======

python-diminuendo is published under a BSD 3-clause license, see the LICENSE
file distributed with the project.
