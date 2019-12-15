==========
django-spa
==========


.. image:: https://badge.fury.io/py/django-spa.svg
    :target: https://badge.fury.io/py/django-spa

.. image:: https://travis-ci.org/metakermit/django-spa.svg?branch=master
    :target: https://travis-ci.org/metakermit/django-spa

.. image:: https://readthedocs.org/projects/django-spa/badge/?version=latest
    :target: https://django-spa.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://pyup.io/repos/github/metakermit/django-spa/shield.svg
    :target: https://pyup.io/repos/github/metakermit/django-spa/
    :alt: Updates

.. image::  https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/metakermit/django-spa/master/LICENSE
    :alt: GitHub license


Django package to serve a single-page app (SPA).

The following settings that make serving SPAs easier
are handled in django-spa:

* *index.html* served when ``/`` requested
* all ``/static/…`` files served on ``/…`` as well
* Django's urls still work (Django admin, templates, Django REST framework APIs)
* everything else goes to ``/`` for frontend routing (e.g. `react-router`_)

Usage
------

For an example of using django-spa to serve a create-react-app frontend
that consumes a Django REST framework API, check out generator-django-rest_.

As part of setting up django-spa, you also need to set up WhiteNoise_,
which we'll summarise here.

First, add ``django-spa`` to your *requirements.txt*
and ``pip install -r requirements.txt`` (or ``pipenv install django-spa``).
Whitenoise is installed as a dependency, so no need to specify it extra.

Update *settings.py* with the Whitenoise & django-spa middleware::

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'spa.middleware.SPAMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

Disable runserver's static file serving by adding ``runserver_nostatic``
to the top of your INSTALLED_APPS list::

    INSTALLED_APPS = [
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',
        # ...
    ]

Set the django-spa static file storage::

    STATICFILES_STORAGE = 'spa.storage.SPAStaticFilesStorage'

You should be good to go!

Credits
---------

Used some parts of the solution suggested in this `WhiteNoise issue`_
for serving index.html on ``/``.
This package was created with Cookiecutter_
and the `audreyr/cookiecutter-pypackage`_ project template.

License
--------

MIT_

.. _Whitenoise: http://whitenoise.evans.io/en/stable/django.html
.. _`Whitenoise issue`: https://github.com/evansd/whitenoise/issues/12
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`react-router`: https://reacttraining.com/react-router/
.. _generator-django-rest: https://github.com/metakermit/generator-django-rest
.. _MIT: LICENSE
