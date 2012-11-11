from fabric.api import local, lcd

def prepare(branch_name='develop'):
	local('python manage.py test')
	local('git push github master')

def run():
	local('python manage.py migrate gametable')
	local('python manage.py runserver')
