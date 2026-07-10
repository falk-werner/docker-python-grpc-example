#!/usr/bin/env python3

"""
Python gRPC example.
Provides a simple gRPC greeter service and client.
"""

import argparse
from concurrent import futures

import grpc
import greeter_pb2
import greeter_pb2_grpc

class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f"Got a message from {request.name}, let's say hello.")
        return greeter_pb2.HelloReply(message=f"Hello, {request.name}!")

def serve(address: str, max_workers: int):
    server = grpc.server(futures.ThreadPoolExecutor(
        max_workers=max_workers))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(address)
    server.start()

    print(f"Greeter Service in running on \"{address}\"."
          "Press Ctrl+C to quit.")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt as ex:
        print("bye")

def greet(address: str, name: str):
    with grpc.insecure_channel(address) as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeter_pb2.HelloRequest(name=name))
        print(response.message)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", "-a", type=str, default="unix:///var/run/greeter.sock")
    subparsers = parser.add_subparsers(dest="command")
    serve_parser = subparsers.add_parser("serve")
    serve_parser.add_argument("--max-workers", "-w", type=int, default=2)
    greet_parser = subparsers.add_parser("greet")
    greet_parser.add_argument("name")
    args = parser.parse_args()

    if (args.command == "serve"):
        serve(args.address, args.max_workers)
    else:
        greet(args.address, args.name)

if __name__ == "__main__":
    main()
