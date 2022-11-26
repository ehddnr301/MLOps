import sys
import requests
import prefect
from prefect import flow, task, get_run_logger


@task
def create_logger():
    return get_run_logger()


@task
def log_task(name, logger):
    logger.info(f"Hello {name}!")
    logger.info(f"Prefect Version = {prefect.__version__} 🚀")


@task
def req_url(url, key_name, logger):
    logger.info(f"URL: {url}!")
    res = requests.get(url).json()
    try:
        logger.info(f"{key_name} : {res[key_name]}")
    except KeyError as e:
        logger.error(f"{e} 라는 키 값은 존재하지 않습니다.")

    return True


@flow()
def log_flow(name: str, url: str, key_name: str):
    logger = create_logger()
    log_task(name, logger)
    req_url(url, key_name, logger)


if __name__ == "__main__":
    name = sys.argv[1]
    url = sys.argv[2]
    key_name = sys.argv[3]

    log_flow(name, url, key_name)
