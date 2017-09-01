===============================
django-spa
===============================


.. image:: https://img.shields.io/pypi/v/django-spa.svg
        :target: https://pypi.python.org/pypi/django-spa

.. image:: https://img.shields.io/travis/metakermit/django-spa.svg
        :target: https://travis-ci.org/metakermit/django-spa

.. image:: https://readthedocs.org/projects/django-spa/badge/?version=latest
        :target: https://django-spa.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/metakermit/django-spa/shield.svg
     :target: https://pyup.io/repos/github/metakermit/django-spa/
     :alt: Updates


Simple Django configuration to serve a single-page app (SPA).

The following SPA settings are handled in django-spa:

* index.html served on ``/``
* all ``/static/...`` files served on ``/...``
* Django's urls still work (Django admin, templates, Django REST framework APIs)
* everything else goes to ``/`` for frontend routing (e.g. `react-router`_)

Usage
------

First set up WhiteNoise_, as django-spa overrides some of its functionality.

Add django-spa to your *requirements.txt*::

    django-spa

Update *settings.py* with the django-spa middleware::

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'spa.middleware.SPAMiddleware',
    ]

Use the django-spa static file storage::

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

.. _Whitenoise: https://github.com/evansd/whitenoise/
.. _`Whitenoise issue`: https://github.com/evansd/whitenoise/issues/12
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`react-router`: https://reacttraining.com/react-router/
.. _MIT: LICENSE
