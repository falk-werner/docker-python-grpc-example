# Docker Python gRPC Example

This repository contains an example how to use gRPC in a dockerized Python application.

> [!NOTE]
> This project builds an arm64 image by default.
> To build for other platforms change the `PLATFORM` variable in the 
> [build.sh](buildsh) script.

## Build

Before first build, docker multi-plaform build must be enabled:

```bash
./enable_multiplatform_build.sh
```

> [!NOTE]
> Multi-platform build must be re-enabled after reboot.

To build and export the image, the [build.sh](build.sh) script is used:

```bash
./build.sh
```

Find the exported image in the `out` directory.

## Run Greeter Service

Use the following command line to run the greeter service:

```bash
docker run -it --rm -v ./run:/var/run python-grpc-greeter serve
```

> [!NOTE]
> The greeter service binds to socket `/var/run/greeter.sock` on
> default. In order to use the service, a bind mount is provided
> using the `-v` option. It is also possible to specify a
> different address using the `--address` option (including TCP
> sockets).

## Run Greeter

Use the following command line to run the greeter:

```bash
docker run -it --rm -v ./run:/var/run python-grpc-greeter greet Bob
```

> [!NOTE]
> The greeter service must run in order to make this work.

## References

- [gRPC](https://grpc.io/)
- [gRPC Python Quick start](https://grpc.io/docs/languages/python/quickstart/)
- [gRPC Python Examples on github](https://github.com/grpc/grpc/tree/master/examples/python)
- [Docker multi-platform build](https://docs.docker.com/build/building/multi-platform/#build-multi-platform-images)