# drf_api_views

**Awesome web-browsable Web APIs links.**

- [Function Based api_views][1st]
- [Class Based API Views][]

**Below**: _Screenshot from the browsable API_

![Screenshot][image]

**Below**: _Flow Chart of Generic Api View_

![genericview][image1]

---

# Requirements

- Python (3.6, 3.7, 3.8, 3.9, 3.10)
- Django (2.2, 3.0, 3.1, 3.2, 4.0)

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.

# Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API for accessing users and groups.

Startup up a new project like so...

    pip install django
    pip install djangorestframework
    django-admin startproject example .
    ./manage.py migrate
    ./manage.py createsuperuser

That's it, we're done!

    ./manage.py runserver

You can now open the API in your browser at `http://127.0.0.1:8000/`.

[image]: https://xp.io/storage/16T7uvf1.png
[image1]: https://xp.io/storage/18iM1xZP.png
[1st]: https://github.com/gauravshankarkumar/drf_api_views/commit/39dcacb53e74f7430d6bc2967b0622e098b263b3
