# ML_in_prod_Final_project





# Kidney-Disease-Classification-MLflow-DVC
The Link of the dataset : https://www.kaggle.com/datasets/nazmul0087ct-kidney-dataset-normal-cyst-tumor-and-stone?resource=download

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yam
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/NathanMacktravis/ML_in_prod_Final_project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```






## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI= https://dagshub.com/wandjinathan1/ML_in_prod_project_final_version.mlflow \
MLFLOW_TRACKING_USERNAME=wandjinathan1 \
MLFLOW_TRACKING_PASSWORD=813ef70d2d245e1e8c025432792616ac0acb84df \
python script.py
Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/wandjinathan1/ML_in_prod_project_final_version.mlflow 


export MLFLOW_TRACKING_USERNAME=wandjinathan1 


export MLFLOW_TRACKING_PASSWORD=3476583c51c3474d69abdda93a0f9bb67e700b3d

```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)


