FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install pytest coverage

CMD ["coverage", "run", "-m", "pytest", "tests/"]
