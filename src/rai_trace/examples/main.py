"""
main.py

Example script demonstrating how to use trace_metric_api.py to post metrics.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from rai_trace.trace_metrics_api import post_metrics_to_TRACE_Metric_API


def main():
    AUTH_TOKEN = "Your Auth Token"   # Replace with your real token

    metric_results = {
        "AnswerRelevancyMetric": 88,
        "ContextualPrecisionMetric": 85,
        "FaithfulnessMetric": 92,
        "HallucinationMetric": 45
    }

    application_name = "chat-application"
    version = "1.0.0"
    url = "https://api.example.com/chat"
    use_case = "transportation"

    # Post metrics for different providers
    # print("\nPosting Evidently metrics:")
    # post_metrics_to_TRACE_Metric_API(
    #     metric_results,
    #     AUTH_TOKEN,
    #     provider="evidently",
    #     application_name=application_name,
    #     version=version,
    #     url=url,
    #     use_case=use_case
    # )

    print("\nPosting DeepEval metrics:")
    post_metrics_to_TRACE_Metric_API(
        metric_results,
        AUTH_TOKEN,
        provider="deepeval",
        application_name=application_name,
        version=version,
        url=url,
        use_case=use_case
    )

    # print("\nPosting Opik metrics:")
    # post_metrics_to_TRACE_Metric_API(
    #     metric_results,
    #     AUTH_TOKEN,
    #     provider="opik",
    #     application_name=application_name,
    #     version=version,
    #     url=url,
    #     use_case=use_case
    # )


if __name__ == "__main__":
    main()
