dump:
	curl -o latest.dump `heroku pgbackups:url`
sync:
	heroku run python aclarknet/manage.py syncdb
up:
	git commit -a -m "Update"
	git push
	git push heroku master
