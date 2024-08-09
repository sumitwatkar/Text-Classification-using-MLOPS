import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/sumitwatkar/Text-Classification-using-MLOPS.mlflow")

dagshub.init(repo_owner='sumitwatkar', repo_name='Text-Classification-using-MLOPS', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)