# # emailuser, make email the `USERNAME_FIELD` , But unique username also exists.

emailuser makes it easy to use email address as your identification token instead of a username.
emailuser is a custom Django user model (extends  `AbstractBaseUser`) so it takes a tiny amount of effort to use.

The only difference between emailuser and the vanilla Django  `User`  is email address is the  `USERNAME_FIELD`  (and username also exist, If you not give it in `create_user` it will generate a `random 12 char unique string as username`).

emailuser supports Django 2.* to 3.*

# Why use emailuser?

I have created this custom user package for my university final project where I need to create user using university email also all user must have a profile link using unique username.

# Install and setup

 1. Install with `pip`:
  ```
    #Django 2.x, or 3.x

    pip install django-emailuser 
  ```
 2. Add `emailuser` to your `INSTALLED_APPS` setting:
 
  ```  
    
    INSTALLED_APPS = [

        ...

        'emailuser',

    ]
    
  ```
 3. Specify the custom model as the default user model for your project using the `AUTH_USER_MODEL` setting in your setting:
 
  ```
    
    AUTH_USER_MODEL = "emailuser.User"

  ```
 5. Run migrations (Don't do any migrate before `emailuser` makemigrations).
 
   f you have tables referencing Django  `User`  model, you will have to delete those table and migrations, then re-migrate. This will ensure everything is set up correctly from the beginning.
  
    ```
  python manage.py makemigrations emailuser
    python manage.py migrate
    ```
    
 6. Instead of referring to User directly, you should reference the user model using  `django.contrib.auth.get_user_model()`

  When you define a foreign key or many-to-many relations to the  `User`  model, you should specify the custom model using the  `AUTH_USER_MODEL`  setting.

  ```
  from django.conf import settings
  from django.db import models

  class Profile(models.Model):
      user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
  )
  ```
 Note. FOO@example.com will be replaced to foo@example.com automatically

 
## License

Released under the MIT license. See LICENSE for details.

## [](https://github.com/Swe-HimelRana/django-email-user#questions-comments-or-anything-else)Questions, comments, or anything else?
-   [Contribute](https://github.com/Swe-HimelRana/django-email-user/)
-   [Open an issue](https://github.com/Swe-HimelRana/django-email-user/issues)
-   [https://www.linkedin.com/in/swe-himelrana](https://www.linkedin.com/in/swe-himelrana)
-   [contact@himelrana-swe.com](mailto:contact@himelrana-swe.com)
 
 Give a thanks by [Donation](https://commerce.coinbase.com/checkout/c3eafb3c-65ba-40b5-b555-2037989de629)
 