# MLFlow server's dockerfile
FROM python:3.8.2-slim

RUN pip install mlflow boto3 psycopg2-binary

ENTRYPOINT ["mlflow", "server", \
	"-h", "0.0.0.0", \
	"--artifacts-destination", "s3://ml-bucket/mlartifacts", \
	"--serve-artifacts"]

