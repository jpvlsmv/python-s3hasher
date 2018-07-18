========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - | |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-s3hasher/badge/?style=flat
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/python-s3hasher

.. |travis| image:: https://travis-ci.org/jpvlsmv/python-s3hasher.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/jpvlsmv/python-s3hasher

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/jpvlsmv/python-s3hasher?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/jpvlsmv/python-s3hasher

.. |requires| image:: https://requires.io/github/jpvlsmv/python-s3hasher/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/jpvlsmv/python-s3hasher/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/jpvlsmv/python-s3hasher/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/github/jpvlsmv/python-s3hasher

.. |codecov| image:: https://codecov.io/github/jpvlsmv/python-s3hasher/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/jpvlsmv/python-s3hasher

.. |landscape| image:: https://landscape.io/github/jpvlsmv/python-s3hasher/master/landscape.svg?style=flat
    :target: https://landscape.io/github/jpvlsmv/python-s3hasher/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg
    :target: https://app.codacy.com/project/jpvlsmv/python-s3hasher/dashboard
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/jpvlsmv/python-s3hasher/badges/gpa.svg
   :target: https://codeclimate.com/github/jpvlsmv/python-s3hasher
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/s3hasher.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/s3hasher

.. |commits-since| image:: https://img.shields.io/github/commits-since/jpvlsmv/python-s3hasher/v0.1.1.svg
    :alt: Commits since latest release
    :target: https://github.com/jpvlsmv/python-s3hasher/compare/v0.1.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/s3hasher.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/s3hasher

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/s3hasher.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/s3hasher

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/s3hasher.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/s3hasher

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/jpvlsmv/python-s3hasher/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/jpvlsmv/python-s3hasher/


.. end-badges

Walk S3 bucket(s) and compute hashes

* Free software: BSD 2-Clause License

Installation
============

::

    pip install s3hasher

Documentation
=============

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
