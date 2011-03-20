============
 Migrations
============

To migrate run::

   manage.py migrate

If the migrations fail on the first pass it is probably because there have been issues applying the initial migration. To fix it::

   1. Drop the current database
      (by executing "dropdb cococloud" as the postgres user)

   2. Create it again
      (by executing "createdb -T template_postgis cococloud" as the postgres user)

   3. apply the initial migratios
      (by executing "manage.py migrate --all --fake 0001")


