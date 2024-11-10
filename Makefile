up:
	docker compose up -d

down:
	docker compose down 

restart:
	make down 
	make up

up_superset:
	docker compose -f ../superset/docker-compose-non-dev.yml up -d

down_superset:
	docker compose -f ../superset/docker-compose-non-dev.yml down