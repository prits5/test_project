up:
	docker-compose up -d

build:
	docker-compose up --build -d

down:
	docker-compose down

down-v:
	docker-compose down -v

clean:
	docker-compose down --volumes --remove-orphans

logs:
	docker-compose logs -f

prune-volumes:
	docker volume prune -f

test:
	 docker-compose exec web poetry run python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=90 --log-level ERROR
