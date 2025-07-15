"""
trace_metric_api.py

Reusable helper module to post metric results from different providers
(e.g., 'evidently', 'deepeval', 'opik') to the TRACE Metric API.

License: Add your license here (e.g., MIT, Apache-2.0)
"""

import requests
from typing import Dict, Any, Optional


def post_metrics_to_TRACE_Metric_API(
    metric_results: Dict[str, Any],
    auth_token: str,
    provider: str,
    application_name: str,
    version: str,
    url: str,
    use_case: str
) -> Optional[Dict[str, Any]]:
    """
    Posts metric results to the TRACE Metric API.

    Args:
        metric_results: Dictionary of computed metric scores.
        auth_token: Authorization token for the API.
        user_id: User ID for the API.
        provider: Metric provider name (e.g., 'evidently', 'deepeval', 'opik').
        application_name: Name of the application posting metrics.
        version: Application version.
        url: URL of the application or API.
        use_case: Short description of the use case.

    Returns:
        Response JSON from the API as a dictionary, or None if an error occurs or response is not JSON.
    """
    BASE_URL = "https://app.cognitiveview.com"
    api_url = f"{BASE_URL}/api/cv/v1/metrics"

    headers = {
        "Authorization": auth_token,
        "Content-Type": "application/json",
    }

    payload = {
        "metric_metadata": {
            "application_name": application_name,
            "version": version,
            "url": url,
            "eval_provider": provider,
            "use_case": use_case
        },
        "metric_data": {
            provider: metric_results
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Request payload: {payload}")  # Debug: show what we're sending
        response.raise_for_status()
        json_response = response.json()
        print("Response JSON:", json_response)
        return json_response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response text: {response.text}")  # Show the actual error message
    except Exception as err:
        print(f"An error occurred: {err}")
        print("Response Text:", response.text if response else "No response")
    return None
