# 14. Deployment

A trained model has limited practical value if it remains only inside notebooks or offline experiments.
Deployment is the process of turning a model into a usable system that people or other software can interact with reliably.

This stage is where machine learning meets product engineering.

---

## 14.1 What Deployment Really Means

Deployment is not just "put the model on a server."

In practice, deployment often includes:

- loading the model efficiently
- exposing an inference interface
- handling traffic safely
- measuring latency and failures
- controlling cost
- updating model versions without breaking clients

This is why deployment is more than hosting.
It is operational system design.

---

## 14.2 Inference APIs

Most deployed models are exposed through an API so that applications can send requests and receive predictions.

Common options include:

- FastAPI
- Flask
- specialized LLM serving frameworks such as vLLM or TensorRT-LLM

The serving layer must manage:

- request parsing
- batching
- response formatting
- GPU utilization
- concurrency

For LLMs, the serving framework can dramatically affect throughput and latency.

---

## 14.3 Containerization

A model that works on one machine may fail on another if dependencies are inconsistent.

Containerization solves this by packaging:

- the model code
- Python environment
- system libraries
- CUDA dependencies
- runtime configuration

Docker is the most common tool for this.

Why it matters:

- reproducibility
- portability
- easier cloud deployment
- cleaner environment management

---

## 14.4 Observability and Monitoring

Once a model is live, you need visibility into how it behaves.

Important signals include:

- request volume
- latency
- error rate
- GPU memory usage
- output quality indicators
- drift in input distributions

This is part of MLOps.

Without monitoring, a deployed model can degrade or fail silently while the team assumes everything is fine.

---

## 14.5 Drift and Real-World Change

Models are trained on historical data, but production traffic keeps changing.

Common forms of change include:

- new slang
- domain shift
- user behavior changes
- new adversarial patterns
- changing product requirements

This is why deployment should include a plan for:

- evaluation after release
- retraining or refreshing
- safe rollback

---

## 14.6 Reliability and Product Concerns

A production AI system often needs much more than inference.

Typical requirements:

- authentication
- rate limiting
- retries and timeouts
- health checks
- versioning
- audit logs
- cost controls

These are standard engineering concerns, but they become especially important when inference is expensive or high-impact.

---

## 14.7 Deployment in Modern LLM Systems

Modern LLM systems often include additional moving parts:

- retrieval infrastructure
- tool execution
- conversation memory
- safety filters
- prompt templating
- approval logic
- logging and trace capture

So deploying an LLM usually means deploying a full runtime pipeline around the base model.

---

## 14.8 Practical Mental Model

Training creates model capability.
Deployment turns that capability into a usable service.

If training is about making the model smart enough, deployment is about making the system dependable enough.

The strongest AI products require both.
