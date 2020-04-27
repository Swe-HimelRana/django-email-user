emailuser, make email the USERNAME\_FIELD , But username also exists.
=====================================

emailuser makes it easy to use email address as your identification token
instead of a username.

emailuser is a custom Django user model (extends ``AbstractBaseUser``) so it
takes a tiny amount of effort to use.

The only difference between emailuser and the vanilla Django ``User`` is email
address is the ``USERNAME_FIELD`` (and username also exist, If you not give it in create_user it will generate a random 12 char unique string as username).

emailuser supports Django 2.* to 3.* 

Why use emailuser?
--------------

Because you want everything in ``django.contrib.auth`` except for the
``username`` field and you also want users to **log in with email addresses**.
And you don't want to create your own custom user model or authentication
backend.

Install & Set up
----------------

**Important:** To keep things simple, the steps below will guide you through
the process of using emailuser's ``emailuser`` model for your Django project's user
model. However, it is strongly recommended that you set up a custom user model
that extends emailuser's ``Abstractemailuser`` class, even if emailuser's ``emailuser`` model
is sufficient for you (this way, you can customize the user model if the need
arises). If you would *not* like to follow this recommendation and just want to
use emailuser's ``emailuser`` model, simply follow the steps below (you can skip the
rest of this paragraph). If you *would* like to follow this recommendation, you
should still follow the steps below, but with the following adjustments: After
step 2, follow
`these instructions <https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project>`_,
but instead of using ``from django.contrib.auth.models import AbstractUser``
use ``from emailuser.models import Abstractemailuser`` and instead of using
``from django.contrib.auth.admin import UserAdmin`` use
``from emailuser.admin import UserAdmin``. Then for step 3 of the steps below, you
should set ``AUTH_USER_MODEL`` to your custom user model instead of emailuser's
``emailuser`` model. You should then run ``python manage.py makemigrations``. After
that, you may follow the remaining steps below just the way they are.


0. If your Django project previously used Django's default user model,
   ``django.contrib.auth.models.User``, or if you are unfamiliar with using
   custom user models, jump to **Notes** first (then come
   back). Otherwise, continue onward!

1. Install with ``pip``:

   .. code-block:: shell

       # Django 2.x, or 3.x
       
       `pip install django-emailuser`

2. Add ``emailuser`` to your ``INSTALLED_APPS`` setting:

   .. code-block:: python

       INSTALLED_APPS = [
           ...
           'emailuser',
       ]

3. Specify the custom model as the default user model for your project
   using the ``AUTH_USER_MODEL`` setting in your settings.py:

   .. code-block:: python

       AUTH_USER_MODEL = "emailuser.User"


4. Run migrations (Don't do any migrate before `emailuser` makemigrations).

   .. code-block:: shell

       python manage.py makemigrations emailuser
       python manage.py migrate

5. FOO@example.com will be replaced to foo@example.com automatically
    
 
Notes
-----

If you have tables referencing Django's ``User`` model, you will have to
delete those table and migrations, then re-migrate. This will ensure
everything is set up correctly from the beginning.

Instead of referring to User directly, you should reference the user model
using ``django.contrib.auth.get_user_model()``

When you define a foreign key or many-to-many relations to the ``User``
model, you should specify the custom model using the ``AUTH_USER_MODEL``
setting.

For example:

.. code-block:: python

    from django.conf import settings
    from django.db import models

    class Profile(models.Model):
        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )

License
-------

Released under the MIT license. See LICENSE for details.

Questions, comments, or anything else?
--------------------------------------

-  Open an issue
-  https://www.linkedin.com/in/swe-himelrana
-  contact@himelrana-swe.com
