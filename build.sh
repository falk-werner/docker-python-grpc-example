#!/usr/bin/env bash

set -e

PLATFORM=linux/arm64

mkdir -p out
docker build "--platform=$PLATFORM" --tag python-grpc-greeter -f Dockerfile app
docker save "--platform=$PLATFORM" -o out/python-grpc-greeter.tar python-grpc-greeter