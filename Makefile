up:
	docker compose up -d
	docker compose -f ../superset/docker-compose.yml up -d

down:
	docker compose down -v
	docker compose -f ../superset/docker-compose.yml down

restart:
	down up