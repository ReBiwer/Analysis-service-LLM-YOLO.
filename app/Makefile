.PHONY: migration upgrade

migration:
	alembic revision --autogenerate -m "$(m)"

upgrade:
	alembic upgrade head
