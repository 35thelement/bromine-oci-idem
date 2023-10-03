*****************
Idem-Oci-Instance
*****************

.. todo:: (Set ``todo_include_todos = False`` in ``docs/conf.py`` to hide rst todos)

   Update project docs URL below

.. image:: https://img.shields.io/badge/made%20with-idem-teal
   :alt: Made with idem, a Python implementation of Plugin Oriented Programming
   :target: https://www.idemproject.io/

.. image:: https://img.shields.io/badge/docs%20on-docs.idemproject.io-blue
   :alt: Documentation is published with Sphinx on docs.idemproject.io
   :target: https://docs.idemproject.io/idem-oci-instance/en/latest/index.html

.. image:: https://img.shields.io/badge/made%20with-pop-teal
   :alt: Made with pop, a Python implementation of Plugin Oriented Programming
   :target: https://pop.readthedocs.io/

.. image:: https://img.shields.io/badge/made%20with-python-yellow
   :alt: Made with Python
   :target: https://www.python.org/

About
=====

oci Cloud Provider for Idem

* `idem-oci-instance source code <https://gitlab.com//idem-oci-instance>`__
* `idem-oci-instance documentation <https://docs.idemproject.io/idem-oci-instance/en/latest/index.html>`__

What is Idem?
-------------

This project is built with `idem <https://www.idemproject.io/>`__, an idempotent,
imperatively executed, declarative programming language written in Python. This project extends
idem!

For more information:

* `Idem Project Website <https://www.idemproject.io/>`__
* `Idem Project docs portal <https://docs.idemproject.io/>`__

Getting Started
===============

Prerequisites
-------------

* Python 3.8+
* git *(if installing from source, or contributing to the project)*

Installation
------------

.. note::

   If wanting to contribute to the project, and setup your local development
   environment, see the ``CONTRIBUTING.rst`` document in the source repository
   for this project.

You can install ``idem-oci-instance`` either  from PyPI or from source.

Install from PyPI
+++++++++++++++++

.. todo:: (Set ``todo_include_todos = False`` in ``docs/conf.py`` to hide rst todos)

   If package is available via PyPI, include the directions.

.. code-block:: bash

  pip install "idem-oci-instance"

Install from source
+++++++++++++++++++

Clone the ``idem-oci-instance`` repository and install with pip.

.. code-block:: bash

   # clone repo
   git clone git@<your-project-path>/idem-oci-instance.git
   cd idem-oci-instance

   # Setup venv
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e idem-oci-instance

Setup
=====

After installation oci idem provider execution and state modules will be accessible to the pop `hub`.
In order to use them we need to set up our credentials.

Create a new file called `credentials.yaml` and populate it with profiles.
The `default` profile will be used automatically by `idem` unless you specify one with `--acct-profile=profile_name` on the cli.

credentials.yaml

..  code:: sls

    oci:
      default:
        username: my_user
        password: my_good_password
        endpoint_url: https://console.oci.com/api

Now encrypt the credentials file and add the encryption key and encrypted file path to the ENVIRONMENT.

.. code:: bash

    idem encrypt credentials.yaml

output::

    -A9ZkiCSOjWYG_lbGmmkVh4jKLFDyOFH4e4S1HNtNwI=

Add these to your environment:

.. code:: bash

    export ACCT_KEY="-A9ZkiCSOjWYG_lbGmmkVh4jKLFDyOFH4e4S1HNtNwI="
    export ACCT_FILE=$PWD/credentials.yaml.fernet

You are ready to use ``idem-oci-instance``!

State Example
=============

Example of using oci state in SLS:

my_state.sls:

.. code:: sls

    ensure_sample_exists:
      oci.sample.present:
        - name: a_sample_name
        - description: Managed by Idem

Create sample state:

.. code:: bash

    idem state my_state.sls

Delete sample state:

.. code:: bash

    idem state my_state.sls --invert
