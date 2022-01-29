# Сomment analyzer

## Overview

This is Kedro project, which was generated using `Kedro 0.17.6`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) for full information about Kedro.
###### Project was run on Ubuntu 20.04 and Python3.8
## How to setting

 - Create a new virtual environment:
 ```
 python3 -m venv moder_env
 ```
 - And activate it:
 ```
 source moder_env/bin/activate
 ```
 - Update pip:
 ```
 python3 -m pip install --upgrade pip
 ```
 - Clone repository:
```
git clone this repository
```
- Install project requirements:
```
cd comment_analyzer
pip install -r src/requirements.txt
```

## How to start

- To see the project in graphical view enter:
```
kedro viz         
```
###### For a question about analytics enter N
- To generate a project documentation enter: 
```
kedro build-docs    
```
###### And than open index.html file in directory: docs/build/html/
- To process the data put the data in a folder: 
```
data/01_raw/my_data.csv  
```
###### At the moment, processing is configured for csv files, however, the source of input data can be either a txt file or S3 cloud storage service
- It is also necessary to configure the processing parameters, at least we will specify the names of the columns that contain identifiers and comments 
```
conf/base/parameters.yml: id_col_name: "id_col_name"  
conf/base/parameters.yml: comment_col_name: "comment_col_name"
```
- And now we can start processing:
```
kedro run
```
###### In log we can to see <INFO - Completed 6 out of 6 tasks>
- The processing result will be in the folder: data/05_model_input

