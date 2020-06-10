*******
twitkit
*******

Some tools for managing your twitter data.





Usage
=====

To use the CLI:

.. code-block:: bash

    poetry run cli

To check if you're properly authenticated as a user:

.. code-block:: bash

    poetry run cli whoami


Tweepy stuff
============

Authenticate like the tweepy tutorial says: http://docs.tweepy.org/en/latest/auth_tutorial.html


**twitkit** by default expects a credentials file to exist at ``~/twitkitrc`` — use ``--credspath`` flag to specify a different file. Look at the `sample.twitkitrc <sample.twitkitrc>`_ file in this repository to see the expected structure.



Development
===========

This project uses `poetry <https://python-poetry.org/docs/cli/>`_


To install dependencies and local usage:

.. code-block:: bash

    poetry install


