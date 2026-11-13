# ontouchstart-aws-emulator-lab

This repository is an exploratory research laboratory designed to investigate AWS API behaviors and capabilities using the [AWS Emulator](https://docs.aws.amazon.com/emulator/latest/userguide/getting-started-docker.html).

## The Research Plan

We maintain a clear separation between **Reference** (The Syllabus) and **Exploration** (The Laboratory):

1.  **Reference (The Syllabus):** We use the official [aws-emulator-evaluation-suite](https://github.com/aws/aws-emulator-evaluation-suite) as our primary data source. This repository defines the "Ground Truth" of how AWS behaves. We treat it as a read-only roadmap of features.
2.  **Laboratory (The Practice):** This repository (`ontouchstart-aws-emulator-lab`) is where we build, study, and debug those features. 

## Laboratory Methodology

Instead of cloning the entire evaluation suite, we use a **discovery-driven approach**:

*   **Metadata Exploration:** We build and run specialized tools (e.g., `suite-inspector`) as Docker services. These tools programmatically explore the upstream evaluation suite's repository (manifests, test IDs, and operation lists) to identify high-value behaviors.
*   **Client Prototyping:** Based on the behaviors discovered by our tools, we develop dedicated Docker-based services (e.g., `s3-client`, `dynamodb-client`).
*   **Isolation & Debugging:** Each client is containerized to provide a clean environment for AI agents to learn how specific AWS APIs react to different inputs. This allows for heavy logging and granular debugging of specific API nuances without interference.

## How to Run

The lab is designed to be operated with a single command. This handles the entire lifecycle: building the environment, starting the emulator, running the analysis tools and clients, and cleaning up.

```bash
make
```

### What `make` does:
1.  **Builds** the emulator, the suite-inspector tool, and all client services.
2.  **Starts** the `aws-emulator` in the background.
3.  **Runs `suite-inspector`**: Analyzes the upstream evaluation suite to map out available behaviors.
4.  **Executes exploration clients**: Runs the `s3-client` and `dynamodb-client` to perform the actual API interactions.
5.  **Cleans up** all containers and volumes upon completion.

## Why this structure?

*   **Agentic Learning:** By using loosely coupled Docker services, we provide AI agents with a controlled environment to learn how specific AWS APIs react to different inputs.
*   **High Observability:** Because each client is a separate service, we can easily modify individual clients to add heavy logging or specific debugging logic.
*   **Fidelity Mapping:** By mapping our lab services to the behaviors defined in the official evaluation suite, we ensure our research stays aligned with real AWS behavior.

## Resources & References

*   [AWS Emulator Official Documentation](https://docs.aws.amazon.com/emulator/latest/userguide/getting-started-docker.html)
*   [AWS Emulator on MiniStack](https://ministack.org/blog/aws-emulator)
*   [AWS Emulator and the Engineers' Job when Agents Write the Code](https://www.allthingsdistributed.com/2026/11/aws-emulator-and-the-engineers-job-when-agents-write-the-code.html)
*   [AWS Insights: Better Feedback for Building with Agents](https://aws.amazon.com/blogs/aws-insights/better-feedback-for-building-with-agents/)
*   [Upstream AWS Emulator Repository](https://github.com/aws/aws-emulator)

