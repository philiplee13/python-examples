all:
	fastapi dev app/main.py

up:
	cd local-setup && docker-compose up -d
	cd ..

down:
	cd local-setup && docker-compose down -v
	cd ..
