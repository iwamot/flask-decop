FROM python:3.8-buster
RUN pip install flask pytest coverage black flake8 twine
WORKDIR /sample_app
EXPOSE 3000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "3000"]
