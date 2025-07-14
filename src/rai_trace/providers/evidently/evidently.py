"""
evidently.py

A helper module to post Evidently metric results to the TRACE Metric API.
This module provides a function to send computed metric scores to the TRACE Metric API.
It handles the HTTP request and response, including error handling.
"""

import requests
from typing import Dict, Any, Optional


def post_evidently_metrics_to_TRACE_Metric_API(
    metric_results: Dict[str, Any], 
    auth_token: str, 
    user_id: str,
    application_name: str,
    version: str,
    url: str,
    use_case: str
) -> Optional[Dict[str, Any]]:
    """
    Posts Evidently metric results to the TRACE Metric API.

    Args:
        metric_results (Dict[str, Any]): Dictionary of computed metric scores.
        auth_token (str): Authorization token for the API.
        user_id (str): User ID for the API.
        application_name (str): Name of the application posting metrics.
        version (str): Version of the application.
        url (str): URL of the application or API endpoint.
        use_case (str): Use case or domain (e.g., "transportation", "finance", "healthcare").

    Returns:
        Optional[Dict[str, Any]]: Response JSON from the API, or None if error occurs.
    """
    BASE_URL = "https://api.cognitiveview.com"
    api_url = f"{BASE_URL}/cv/v1/metrics"

    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json",
        "X-User-Id": user_id,
    }

    payload = {
        "metric_metadata": {
            "application_name": application_name,
            "version": version,
            "url": url,
            "provider": "evidently",
            "use_case": use_case
        },
        "metric_data": {
            "evidently": metric_results
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
#     USER_ID = "Your-User-ID-Here"
#
#     # Example metric results from Evidently evaluation
#     metric_results = {
#         "data_drift": 0.15,
#         "model_quality": 0.88,
#         "prediction_drift": 0.12
#     }
#
#     # Application metadata
#     application_name = "fraud-detection-model"
#     version = "2.1.0"
#     url = "https://api.mycompany.com/fraud-detection"
#     use_case = "finance"
#
#     # Post metrics to TRACE API
#     response = post_evidently_metrics_to_TRACE_Metric_API(
#         metric_results=metric_results,
#         auth_token=AUTH_TOKEN,
#         user_id=USER_ID,
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
