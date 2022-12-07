#!/bin/bash
mlflow server --backend-store-uri postgresql://postgres:postgres@127.0.0.1:5432/mlflow_db \
     --default-artifact-root s3://machine-learning-engineering/ --host 0.0.0.0:5000 &
