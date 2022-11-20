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