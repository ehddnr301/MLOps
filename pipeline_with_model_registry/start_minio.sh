#!/bin/bash
mkdir -p ~/minio/data

docker run \
   -d \
   --rm \
   -p 9000:9000 \
   -p 9090:9090 \
   --name minio \
   -v ~/minio/data:/data \
   -e MINIO_ACCESS_KEY=TEST \
   -e MINIO_SECRET_KEY=TESTPASSWORD \
   -e MINIO_ROOT_USER=ROOTNAME \
   -e MINIO_ROOT_PASSWORD=CHANGEME123 \
   quay.io/minio/minio server /data --console-address ":9090"