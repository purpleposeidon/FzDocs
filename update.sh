#!/bin/bash

set -e

if [ ! -e /var/www/FzDocs ]; then
    echo "not exported"
    exit
fi

git checkout gh-pages
rm -rf * #Deletes this very script, but that's fine.
git checkout master *

wget -r http://localhost/FzDocs/ || true
mv localhost/FzDocs/* ./
rmdir -rf localhost
