# Docker & Kubernetes Documentation

**ApexaIQ – Week 4 Documentation**

## What is SDLC?

**SDLC (Software Development Life Cycle)** defines the process for planning, creating, testing, and deploying an information system.

### Common SDLC Phases:

1. **Design**
2. **Development**
3. **Testing**
4. **Staging**
5. **Deployment**
6. **Maintenance**

---

## Monolithic Architecture vs Microservices

| Feature          | Monolithic Architecture      | Microservices Architecture                |
| ---------------- | ---------------------------- | ----------------------------------------- |
| Structure        | Single unified unit          | Collection of small, independent services |
| Deployment       | Entire app deployed together | Each service deployed independently       |
| Scalability      | Hard to scale                | Easy to scale specific services           |
| Failure Impact   | Affects whole app            | Isolated to specific service              |
| Technology Stack | Usually single               | Different tech stacks per service         |

> **Example:**  
> A shopping app with one backend = Monolithic.  
> Same app split into `user-service`, `cart-service`, `payment-service` = Microservices.

---

## Blue-Green Deployment

**Blue-Green Deployment** is a strategy for **zero downtime deployment**.

- **Blue Environment**: Current live version.
- **Green Environment**: New version of the app.

Once testing succeeds in _Green_, the load balancer switches traffic from _Blue_ to _Green_ — no downtime!

---

## Docker – Introduction

**Docker** is an open-source platform that enables developers to **build, ship, and run applications** inside **containers**.

### Key Concepts

- **Image**: A lightweight, stand-alone, executable package that includes code, runtime, and dependencies.
- **Container**: A running instance of an image.
- **Dockerfile**: Script that defines the image.
- **Docker Hub**: Central repository for container images.

---

## Why Use Docker?

| Advantage           | Description                          |
| ------------------- | ------------------------------------ |
| Portability         | Works the same on any system         |
| Isolation           | Each app runs in its own environment |
| Speed               | Containers start in seconds          |
| Resource Efficiency | Uses less RAM/CPU than VMs           |
| Version Control     | Consistent deployment                |

---

## Problems with Docker Alone

1. Manual management of containers
2. Complex scaling and updates
3. Difficult migration between servers
4. Limited self-healing
5. Downtime during deployment

To overcome these, we use **Kubernetes**.

---

## What is Kubernetes (K8s)?

**Kubernetes (K8s)** is an **open-source container orchestration system** designed by Google, written in **Go (Golang)**.

### Meaning

The word _“Kubernetes”_ is Greek for **“Helmsman”** or **“Pilot”** — symbolizing control and navigation of container ships (clusters).

---

## Why Kubernetes?

- Automates **deployment**, **scaling**, and **management** of containerized applications.
- Supports **self-healing** and **auto-scaling**.
- Simplifies **load balancing** and **service discovery**.

---

## Features of Kubernetes

1. **Storage Orchestration** – Auto-mount storage systems.
2. **Automated Rollouts & Rollbacks** – Manage app updates smoothly.
3. **Secret & Config Management** – Manage credentials safely.
4. **Horizontal Scaling** – Scale apps up/down based on load.
5. **Service Discovery & Load Balancing** – Routes traffic automatically.

---

## Kubernetes Architecture Overview

Kubernetes has **two main components**:

1. **Control Plane (Master Node)**
2. **Worker Nodes**

---

### 1. Control Plane Components

| Component                       | Role                                    |
| ------------------------------- | --------------------------------------- |
| **API Server (kube-apiserver)** | Entry point for all commands & requests |
| **etcd**                        | Key-value store for cluster state       |
| **Controller Manager**          | Ensures desired cluster state           |
| **Scheduler**                   | Assigns Pods to nodes                   |
| **Cloud Controller Manager**    | Manages cloud-specific control loops    |

---

### 2. Node (Worker Node) Components

| Component                                        | Role                                    |
| ------------------------------------------------ | --------------------------------------- |
| **Kubelet**                                      | Ensures containers are running properly |
| **kube-proxy**                                   | Handles network routing                 |
| **Container Runtime (e.g., Docker, containerd)** | Runs containers                         |

---

### Pod

A **Pod** is the smallest deployable unit in Kubernetes — it **wraps one or more containers** together.

```text
Pod
 ├── Container 1 (e.g., Nginx)
 └── Container 2 (e.g., Sidecar Logger)
```

---

## Kubernetes Workflow

```text
User → kubectl command → API Server → Scheduler → Node (Kubelet) → Container Runtime → Pod running
```

---

## Kubernetes Objects

| Object               | Description                                |
| -------------------- | ------------------------------------------ |
| **Pod**              | Basic unit that runs a container           |
| **Service**          | Exposes a set of Pods as a network service |
| **Deployment**       | Defines how Pods are created/updated       |
| **ReplicaSet**       | Ensures a specific number of Pods          |
| **Namespace**        | Logical grouping within cluster            |
| **ConfigMap/Secret** | Store configuration and sensitive data     |

---

## 💻Docker Commands

```bash
# Check Docker version
docker --version

# List all images
docker images

# List running containers
docker ps

# Build image from Dockerfile
docker build -t myapp .

# Run a container
docker run -d -p 8080:80 myapp

# Stop container
docker stop <container_id>

# Remove container/image
docker rm <container_id>
docker rmi <image_id>
```

---

## Kubernetes Commands (kubectl)

```bash
# Check version
kubectl version --client

# View cluster info
kubectl cluster-info

# Get all pods/services/deployments
kubectl get pods
kubectl get services
kubectl get deployments

# Create a deployment
kubectl create deployment nginx --image=nginx

# Expose deployment as a service
kubectl expose deployment nginx --type=LoadBalancer --port=80

# Scale deployment
kubectl scale deployment nginx --replicas=3

# Delete resources
kubectl delete pod <pod_name>
kubectl delete service <service_name>
```

---

## Blue-Green Deployment in Kubernetes

1. Create two deployments: `blue` and `green`.
2. Run the new version (`green`) alongside the old (`blue`).
3. Use the **service** object to switch traffic to the new version.
4. Delete the old deployment after verification.

---

## Summary

| Topic                    | Summary                                                       |
| ------------------------ | ------------------------------------------------------------- |
| **Docker**               | Enables app containerization for portability and consistency. |
| **Problems with Docker** | Lacks orchestration, scaling, and self-healing.               |
| **Kubernetes**           | Automates deployment, scaling, and management of containers.  |
| **Architecture**         | Control Plane + Worker Nodes for full orchestration.          |
| **Commands**             | `docker` and `kubectl` are primary management tools.          |
| **Deployment Strategy**  | Blue-Green ensures zero downtime.                             |

---
