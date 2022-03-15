# Generate a one-off secret key in Django

CodingEntrepreneurs [Post](https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key/).

The code:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Original Source [CodingEntrepreneurs](https://github.com/codingforentrepreneurs/Try-Django-3.2/tree/main/references).