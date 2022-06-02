import mlflow
import sys

mlflow.set_tracking_uri("http://10.3.15.100:8080")
if __name__ == '__main__':
    run_id = str(sys.argv[1])
    mlflow.delete_run(run_id)
