from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import CronSchedule

from model_training import training_flow

model_training_deployment = Deployment.build_from_flow(
    flow=training_flow,
    name="stock_model_training_with_registry",
    parameters={"date": "daily"},
    work_queue_name="train_stock_model_queue_with_registry",
    schedule=(CronSchedule(cron="0 1 * * *", timezone="Asia/Seoul")),
)

if __name__ == "__main__":
    model_training_deployment.apply()
