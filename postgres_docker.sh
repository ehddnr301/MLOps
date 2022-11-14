#!/bin/bash
sudo docker run -d --name postgresql -p 5432:5432 -e POSTGRES_PASSWORD=postgres -v $HOME/pg_data:/var/lib/postgresql/data postgres:13.4
