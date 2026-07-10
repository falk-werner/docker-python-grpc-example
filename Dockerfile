FROM python:3.14-alpine AS builder

RUN python3 -m pip install grpcio grpcio-tools

WORKDIR /app
COPY * /app
RUN python3 -m grpc_tools.protoc \
    -I . \
    --python_out=. \
    --pyi_out=. \
    --grpc_python_out=. \
    greeter.proto

FROM python:3.14-alpine AS image

RUN python3 -m pip install grpcio protobuf

WORKDIR /app
COPY --from=builder /app/* /app/

ENTRYPOINT ["python3", "greeter.py"]