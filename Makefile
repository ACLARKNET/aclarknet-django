dump:
	curl -o latest.dump `heroku pgbackups:url`
push:
	git commit -a -m "Update"
	git push
	git push heroku master
sync:
	heroku run python aclarknet/manage.py syncdb
