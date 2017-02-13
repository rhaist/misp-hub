#!/bin/bash

# Delete sqlite database
rm db.sqlite3

# Delete migrations
rm -rf events/migrations
rm -rf orgs/migrations
rm -rf sharing_groups/migrations
rm -rf sync/migrations

python3 manage.py makemigrations
python3 manage.py migrate
