#!/bin/bash

# Delete sqlite database
rm db.sqlite3

# Delete migrations
rm -rf events/migrations
rm -rf orgs/migrations
rm -rf sharing_groups/migrations
rm -rf sync/migrations

python3 manage.py makemigrations events
python3 manage.py makemigrations orgs
python3 manage.py makemigrations sharing_groups
python3 manage.py makemigrations sync

python3 manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('testadmin', 'testadmin@example.com', 'test1234')" | python3 manage.py shell

