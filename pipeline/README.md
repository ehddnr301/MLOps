# Tutorial

## Task0 - Prefect 설치

- `pip install prefect==2.6.8`

## Task1 - Prefect Cloud 연결

- `https://app.prefect.cloud/workspaces/create` 접속하여 WorkSpace 생성
    - Create WorkSpace
      - Owner: 변경하지 않아도 됨.
      - Handle: Workspace명

- `prefect cloud login -k API_KEY`
- `prefect cloud workspace set --workspace "Owner/Handle"`

### Local

- Prefect Cloud를 이용하고 싶지 않은 경우
  - 위 cloud설정을 진행하였다면 `prefect config unset PREFECT_API_URL` 으로 삭제
- `prefect orion start`

#### Local2

- Prefect Database를 변경하고 싶은 경우 (To PostgreSQL)
  - `docker exec -it postgresql bash`
  - `psql -U postgres`
  - `create database prefect;`
  - `prefect config set PREFECT_ORION_DATABASE_CONNECTION_URL="postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/prefect"`

## Task2 Pipeline Deployment

- `python log_flow.py`
- `python deployment.py`
  - `prefect agent start --work-queue "test_queue"`