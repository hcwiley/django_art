#!/bin/sh
CODE_DIR='/home/hcwiley/git/hcwiley_art/portfolio'
APP_DIR='/home/hcwiley/webapps/hcwiley_art/portfolio'

cd $CODE_DIR
git pull
cp -r portfolio ~/webapps/hcwiley_art/

cd $APP_DIR
source ../.env
python manage.py migrate
python manage.py collectstatic --noinput
../apache2/bin/restart

