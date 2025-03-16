# Запуск web-сервиса
start:
	$ uv run uvicorn --factory src.presentation.api.main:create_app --port 8500 --host 127.0.0.1
