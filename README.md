# erepro

Repository contains the microservices source code and the k8s infrastructure definition together with the istio routing rules.

# Dependencies

* minikube v0.28.0
* kubernetes v1.10.0
* istio v0.8.0
* bazel@latest
* dockr@latest

# Build

```bash
make build
```

docker-compose
```
make up
make kill
```

# Run
```bash
make run
```
