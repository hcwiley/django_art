from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

def prepare_deploy():
  local("git push")

def deploy():
  code_dir = '/home/hcwiley/git/hcwiley_art/portfolio'
  app_dir = '~/webapps/hcwiley_art/portfolio'
  with cd(code_dir):
    run("git pull")
    run("cp -r portfolio ~/webapps/hcwiley_art/")
  with cd(app_dir):
    run("python manage migrate")
    run("python manage collectstatic")
    run("~/webapps/hcwiley_art/apache2/bin/restart")
