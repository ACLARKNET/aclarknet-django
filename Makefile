dump:
	curl -o latest.dump `heroku pgbackups:url`
push:
	git push
	git push heroku master
