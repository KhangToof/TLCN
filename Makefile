up:
	docker compose up -d
	docker compose -f ../superset/docker-compose.yml up -d

down:
	docker compose down 
	docker compose -f ../superset/docker-compose.yml down

restart:
	make down 
	make up