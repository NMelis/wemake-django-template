#!/usr/bin/env sh

set -o errexit
set -o nounset


# Run python specific scripts:
# Running migrations in startup script might not be the best option, see:
# docs/_pages/template/going-to-production.rst
python /code/manage.py migrate --noinput
python /code/manage.py collectstatic --noinput
python /code/manage.py compilemessages

# Start gunicorn with 4 workers:
/usr/local/bin/gunicorn server.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code
