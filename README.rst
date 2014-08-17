======================
cookiecutter-pymodule
======================

.. image:: https://requires.io/github/pydanny/cookiecutter-pymodule/requirements.png?branch=master
     :target: https://requires.io/github/pydanny/cookiecutter-pymodule/requirements/?branch=master
     :alt: Requirements Status

A cookiecutter_ template for a single module (file) Python package.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Planned Features
-------------------

* Free software: BSD license
* Optional shell entry point powered by click_.
* Testing with pytest_
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3
* README.rst for documentation (Sphinx is overkill for single )

.. _click: http://click.pocoo.org/
.. _pytest: http://pydanny.com/pytest-no-boilerplate-testing.html

Usage
-----

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Then, we'll assume you have a snippet of Python code you want to turn into
a tested, documented, and installable package. For example, it might be
a function:

.. code-block:: python

    def do_something(value):
        raise NotImplementedError("Replace with your own code")


Alright, time to cenerate a single module Python package!::

    cookiecutter https://github.com/pydanny/cookiecutter-pymodule.git

You'll be prompted for some questions, answer them, and cookiecutter does a
bunch of work for you. Once it's done, enter the new package:

.. code-block:: bash

    cd <new-package-name>

Now, add your code to the just-generated module. To make sure your code is
going into the correct place, look for the following text::

    ######################################
    #
    # Your code goes here
    #
    ######################################


Once that's done we suggest you create a GitHub repo and put your new package there. Once it's properly secured there, write some tests in the `tests.py` module!

Uploading to PyPI
------------------

::

    python setup.py register





Not Exactly What You Want?
--------------------------

This is what I want. *It might not be what you want.*  Don't worry, you have options:


Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, let me know and I'll list it
 Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage`: https://github.com/tony/cookiecutter-pypackage
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
