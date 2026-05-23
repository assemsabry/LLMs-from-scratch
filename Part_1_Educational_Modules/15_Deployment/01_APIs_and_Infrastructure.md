# 1. Deployment and Infrastructure

Building an LLM is a science; serving it to millions of users is software engineering.

---

## 1.1 APIs (Application Programming Interfaces)

Once an LLM is running in a serving engine (like vLLM), it needs to be accessible to web applications and users. We wrap the engine in a REST API.

*   **FastAPI:** The industry standard in the Python ecosystem. It is incredibly fast, natively async, and automatically generates Swagger documentation. Most open-source model servers use FastAPI to expose endpoints that mimic the OpenAI API format.
*   **Flask / Django:** Older Python web frameworks. While robust, they are generally considered too heavy and synchronous for the ultra-fast, async needs of real-time AI generation.

## 1.2 Hardware Infrastructure

AI workloads require specialized hardware, specifically GPUs, to handle the massive parallel matrix math.

*   **NVIDIA:** The undisputed king of AI hardware. The A100 and H100 Tensor Core GPUs are the backbone of modern AI data centers. They rely on CUDA, NVIDIA's proprietary parallel computing platform.
*   **AMD & Others:** AMD is catching up with their MI300X chips using ROCm (their alternative to CUDA). Google uses its own proprietary TPUs (Tensor Processing Units) specifically designed for deep learning.

## 1.3 Cloud vs. On-Premise

*   **Cloud Providers (AWS, GCP, Azure):** Ideal for startups. You rent GPUs by the hour. Azure offers deep integration with OpenAI models, GCP provides access to TPUs and Gemini, and AWS offers custom Trainium and Inferentia chips alongside standard NVIDIA GPUs.
*   **On-Premise:** Buying your own physical servers. While the upfront capital expenditure (CapEx) is massive (a single 8x H100 server costs hundreds of thousands of dollars), it becomes mathematically cheaper than the Cloud if you run the GPUs 24/7 at high utilization.

## 1.4 Scaling and Reliability

*   **Load Balancing:** When you have thousands of users, a single GPU server will crash. Load balancers distribute incoming API requests across multiple physical servers.
*   **Continuous Batching:** A technique used by modern servers where new requests are dynamically injected into a batch that is already currently being processed by the GPU, maximizing throughput and minimizing idle compute time.
