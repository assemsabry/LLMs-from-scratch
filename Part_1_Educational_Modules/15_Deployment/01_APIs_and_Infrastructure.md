# 1. Deployment and Infrastructure

Building an LLM is a science; serving it to millions of users is software engineering.

This is where AI stops being only a model and becomes a product.

---

## 1.1 APIs (Application Programming Interfaces)

Once an LLM is running in a serving engine (like vLLM), it needs to be accessible to web applications and users. We wrap the engine in a REST API.

*   **FastAPI:** The industry standard in the Python ecosystem. It is incredibly fast, natively async, and automatically generates Swagger documentation. Most open-source model servers use FastAPI to expose endpoints that mimic the OpenAI API format.
*   **Flask / Django:** Older Python web frameworks. While robust, they are generally considered too heavy and synchronous for the ultra-fast, async needs of real-time AI generation.

### Why APIs matter

An LLM without an API is difficult to integrate into real applications.

The API layer is what lets:

- websites call the model
- internal tools connect to it
- mobile apps use it
- logging and auth wrap around it

That makes the API layer part of the product architecture, not just a thin wrapper.

## 1.2 Hardware Infrastructure

AI workloads require specialized hardware, specifically GPUs, to handle the massive parallel matrix math.

*   **NVIDIA:** The undisputed king of AI hardware. The A100 and H100 Tensor Core GPUs are the backbone of modern AI data centers. They rely on CUDA, NVIDIA's proprietary parallel computing platform.
*   **AMD & Others:** AMD is catching up with their MI300X chips using ROCm (their alternative to CUDA). Google uses its own proprietary TPUs (Tensor Processing Units) specifically designed for deep learning.

### Why hardware choices affect software design

Different hardware affects:

- framework support
- inference engines
- memory limits
- deployment cost
- throughput optimization

This is why infrastructure and model serving cannot be designed independently.

## 1.3 Cloud vs. On-Premise

*   **Cloud Providers (AWS, GCP, Azure):** Ideal for startups. You rent GPUs by the hour. Azure offers deep integration with OpenAI models, GCP provides access to TPUs and Gemini, and AWS offers custom Trainium and Inferentia chips alongside standard NVIDIA GPUs.
*   **On-Premise:** Buying your own physical servers. While the upfront capital expenditure (CapEx) is massive (a single 8x H100 server costs hundreds of thousands of dollars), it becomes mathematically cheaper than the Cloud if you run the GPUs 24/7 at high utilization.

### A modern third path

In practice, many teams now use a hybrid approach:

- local or on-prem for private workloads
- cloud for burst capacity
- external APIs for the heaviest frontier tasks

This reduces both cost and operational rigidity.

## 1.4 Scaling and Reliability

*   **Load Balancing:** When you have thousands of users, a single GPU server will crash. Load balancers distribute incoming API requests across multiple physical servers.
*   **Continuous Batching:** A technique used by modern servers where new requests are dynamically injected into a batch that is already currently being processed by the GPU, maximizing throughput and minimizing idle compute time.

### Other reliability layers

A serious deployment usually also needs:

- request authentication
- rate limiting
- retries and timeouts
- logging and tracing
- health checks
- autoscaling
- fallback behavior

## 1.5 Safety and Governance in Deployment

By 2026, safe deployment became a core engineering requirement.

A real AI service often needs:

- content filtering
- approval gates for dangerous actions
- audit logs
- provenance handling
- policy enforcement around tools

This is especially important once the system can do more than generate text.

## 1.6 What Learners Should Build

If you want to understand LLM deployment in a practical way, build these in order:

1. a local inference script
2. a simple FastAPI endpoint
3. request logging
4. basic batching or queueing
5. safety or validation checks

That progression teaches the difference between:

- running a model
- operating a service
