# mlflow

A quick demo on how to use MLFlow. \
The main.py file is an example of MLFlow run.\
Link to the doc: https://www.mlflow.org/docs/latest/tracking.html

## Introduction

MLflow is a tool that allows you to manage machine learning models lifecycle. It is used to track runs, save parameters, metrics and models in order to compare them. Moreover, it is possible to package your model and to serve it onto a server.

## Useful commands and functions

- <code>mlflow.set_tracking_uri(http://10.3.15.100:8080)</code> connects the run to the right server. If not specified, default port is **localhost:5000**.
- Use <code>mlflow.start_run()</code> to start a run and write your code underneath. 
The function can take optional parameters if needed, such as <code>experiment_id [str] </code>,
<code>run_name [str]</code> or <code>description [str]</code>. 
More details [here](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.start_run).

- Log parameters using <code>mlflow.log_params(name, parameter)</code>. More details [here](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_param).
- Log metrics using <code>mlflow.log_metric(name, metric)</code>. More details [here](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_metric).
- Log artifacts using <code>mlflow.log_artifact(path_to_file, artifact_path)</code>. <code>artifact_path</code> is the path to the folder that will contain the artifact. 
More details [here](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_artifact).
Artifacts can be viewed by clicking on the run's name on MLFlow server. They also can be retrieved directly from Minio where they are stored.
- Log models using <code>log_model(model, artifact_path)</code> function. The function depends on the model you are using. For example, if your model is from scikit-learn, 
you would use <code>mlflow.sklearn.log_model()</code>, if it is from keras, then use <code>mlflow.keras.log_model()</code> and so on. Note that <code>artifact_path</code> is optional and if spefified, 
it will also save the model as an artifact. You will details on <code>mlflow.sklearn.log_model()</code> [here](https://www.mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model). 


## MLFlow UI
After running your python script, logs are saved on the server and you can view them on **http://10.3.15.100:8080**. <br><br>
On the main page, you'll find the list of runs for each experiment along with their metrics and parameters. The experiment selected here is named **Default**. <br><br>
![mlflow ui](/images/mlflow_ui.PNG)

- If you click on the run's name, you'll access to its details, including artifacts. <br><br>
![details1](/images/run_details1.PNG) ![details2](/images/run_details2.PNG) <br><br>

- You can also plot metrics by clicking on it. <br><br>
![click_on_metric](/images/click_on_metric.PNG) ![plot_chart](/images/plot_chart.PNG)

## Create an experiment
MLflow is organized in experiments. One experiment can contain as many runs as needed but one run is associated with only one experiment. <br>
Finally, you can create a new experiment from your python code, by using <code>mlflow.create_experiment(name)</code>. But for more convenience, a python script has been made
for this purpose. From the terminal, go to the folder containing **create-experiment.py** and enter the command **python create-experiment [name]**. <br><br>
Here I entered **python create-experiment my-new-experiment**. It is immediately visible from the UI. <br><br> ![ui_new_exp](/images/ui_new_experiment.PNG) <br><br>

Experiments can also be created from MLFLow UI by clicking on the top-left **+** button.
