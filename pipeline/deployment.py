from log_flow import log_flow
from prefect.deployments import Deployment

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

if __name__ == "__main__":
    deployment.apply()
