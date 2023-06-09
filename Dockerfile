FROM python:3.10-slim
WORKDIR /task_manager
RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --without develop
COPY ../pythonProject11/task_manager/ .
EXPOSE 8000
CMD gunicorn -b 0.0.0.0:8000 task_manager.wsgi --workers=2 --threads=2