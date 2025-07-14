"""
main.py

Example script demonstrating how to use trace_metric_api.py to post metrics.
"""

from src.rai_trace.trace_metrics_api import post_metrics_to_TRACE_Metric_API


def main():
    AUTH_TOKEN = "Your-Authorization-Token-Here"   # Replace with your real token
    USER_ID = "Your-User-ID-Here"                  # Replace with your real user ID

    metric_results = {
        "accuracy": 0.95,
        "f1_score": 0.91
    }

    application_name = "chat-application"
    version = "1.0.0"
    url = "https://api.example.com/chat"
    use_case = "transportation"

    # Post metrics for different providers
    print("\nPosting Evidently metrics:")
    post_metrics_to_TRACE_Metric_API(
        metric_results,
        AUTH_TOKEN,
        USER_ID,
        provider="evidently",
        application_name=application_name,
        version=version,
        url=url,
        use_case=use_case
    )

    print("\nPosting DeepEval metrics:")
    post_metrics_to_TRACE_Metric_API(
        metric_results,
        AUTH_TOKEN,
        USER_ID,
        provider="deepeval",
        application_name=application_name,
        version=version,
        url=url,
        use_case=use_case
    )

    print("\nPosting Opik metrics:")
    post_metrics_to_TRACE_Metric_API(
        metric_results,
        AUTH_TOKEN,
        USER_ID,
        provider="opik",
        application_name=application_name,
        version=version,
        url=url,
        use_case=use_case
    )


if __name__ == "__main__":
    main()
