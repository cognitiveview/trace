"""
main.py

Example script demonstrating how to use trace_metric_api.py to post metrics.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from rai_trace.trace_metrics_api import post_metrics_to_TRACE_Metric_API
from rai_trace.providers.deepeval.deepeval import  post_deepeval_metrics_to_TRACE_Metric_API


def main():
    AUTH_TOKEN = "Your Subscription key"   # Replace with your real token

    metric_results = {
        "AnswerRelevancyMetric": 88,
        "ContextualPrecisionMetric": 85,
        "FaithfulnessMetric": 92,
        "HallucinationMetric": 45
    }

    application_name = "chat-application"
    version = "1.0.0"
    use_case = "transportation"


    # print("\nPosting DeepEval metrics:")
    # post_metrics_to_TRACE_Metric_API(
    #     metric_results,
    #     AUTH_TOKEN,
    #     provider="deepeval",
    #     application_name=application_name,
    #     version=version,
    #     use_case=use_case
    # )
    print("\nPosting DeepEval metrics through deepeval_trace_api:")
    post_deepeval_metrics_to_TRACE_Metric_API(
        metric_results,
        AUTH_TOKEN,
        application_name=application_name,
        version=version,
        use_case=use_case
    )


if __name__ == "__main__":
    main()
