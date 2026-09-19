up:
	docker compose up --build
python-test:
	cd python-agent && pytest -q
java-test:
	cd java-crm-service && mvn test
