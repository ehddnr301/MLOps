# Tutorial

## Directory Structure

```
.
├── .env
├── README.md
├── deployment.py
├── model_training.py
├── settings.py
├── start_minio.sh
└── start_mlflow.sh
```

## Command

- `start_minio.sh`
- `start_mlflow.sh`
- `python deployment.py`
  - `prefect agent start --work-queue "train_stock_model_queue_with_registry"`