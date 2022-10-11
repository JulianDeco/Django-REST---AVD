### content of "create_user.py" file

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apiExpo.settings')
import django
django.setup()
from django.contrib.auth.models import User

# see ref. below
user = User.objects.create(
            username='root',
            email='juliandecopp@gmail.com',
            is_superuser=True,
            is_staff=True,
            password='1415Jilio#2001')  
user.save()
