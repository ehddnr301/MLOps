from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import CronSchedule

from log_flow import log_flow
from model_training import training_flow


deployment = Deployment.build_from_flow(
    flow=log_flow,
    name="just_logging",
    parameters={
        "name": "DWLEE",
        "url": "https://api.coindesk.com/v1/bpi/currentprice.json",
        "key_name": "disclaimer",
    },
    infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}},
    work_queue_name="test_queue",
)

model_training_deployment = Deployment.build_from_flow(
    flow=training_flow,
    name="stock_model_training",
    parameters={"date": "daily"},
    work_queue_name="train_stock_model_queue",
    schedule=(CronSchedule(cron="0 1 * * *", timezone="Asia/Seoul")),
)

if __name__ == "__main__":
    deployment.apply()
    model_training_deployment.apply()
