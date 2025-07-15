"""
deepeval.py

A helper module to post DeepEval metric results to the TRACE Metric API.
This module provides a function to send computed metric scores to the TRACE Metric API.
It handles the HTTP request and response, including error handling.
"""

import requests
from typing import Dict, Any, Optional


def post_deepeval_metrics_to_TRACE_Metric_API(
    metric_results: Dict[str, Any], 
    auth_token: str, 
    application_name: str,
    version: str,
    url: str,
    use_case: str
) -> Optional[Dict[str, Any]]:
    """
    Posts DeepEval metric results to the TRACE Metric API.

    Args:
        metric_results (Dict[str, Any]): Dictionary of computed metric scores.
        auth_token (str): Authorization token for the API.
        application_name (str): Name of the application posting metrics.
        version (str): Version of the application.
        url (str): URL of the application or API endpoint.
        use_case (str): Use case or domain (e.g., "transportation", "finance", "healthcare").

    Returns:
        Optional[Dict[str, Any]]: Response JSON from the API, or None if error occurs.
    """
    BASE_URL = "https://api.cognitiveview.com"
    api_url = f"{BASE_URL}/metrics"

    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json",
    }

    payload = {
        "metric_metadata": {
            "application_name": application_name,
            "version": version,
            "url": url,
            "eval_provider": "deepeval",
            "use_case": use_case
        },
        "metric_data": {
            "deepeval": metric_results
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()
        json_response = response.json()
        print("Response JSON:", json_response)
        return json_response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
        print("Response Text:", response.text if response else "No response")
    return None


# Example usage (uncomment to test)
# if __name__ == "__main__":
#     # Replace with your actual credentials
#     AUTH_TOKEN = "Your-Authorization-Token-Here"
#
#     # Example metric results from DeepEval evaluation
#     metric_results = {
#         "answer_relevancy": 0.95,
#         "faithfulness": 0.92,
#         "hallucination": 0.08,
#         "bias": 0.05
#     }
#
#     # Application metadata
#     application_name = "chat-application"
#     version = "1.0.0"
#     url = "https://api.example.com/chat"
#     use_case = "transportation"
#
#     # Post metrics to TRACE API
#     response = post_deepeval_metrics_to_TRACE_Metric_API(
#         metric_results=metric_results,
#         auth_token=AUTH_TOKEN,
#         application_name=application_name,
#         version=version,
#         url=url,
#         use_case=use_case
#     )
#
#     if response:
#         print("Metrics successfully posted to TRACE API")
#     else:
#         print("Failed to post metrics")
