#!/usr/bin/env bash

set -e

PLATFORM=linux/arm64

mkdir -p out
docker build \
    "--platform=$PLATFORM" \
    --tag python-grpc-greeter \
    --output type=docker,dest=out/python-grpc-greeter.tar \
    .

