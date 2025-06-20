"""
IX-AcidBurn Gibson Adapter

Handles reliable communication with IX-Gibson, enabling AcidBurn to
delegate queries and receive domain-specific insights.
"""

import requests
import time
from config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS

class GibsonAdapter:
    def __init__(self):
        self.endpoint = GIBSON_API_URL
        self.timeout = REQUEST_TIMEOUT_SECONDS
        self.retries = RETRY_ATTEMPTS
        self.backoff = RETRY_BACKOFF_SECONDS

    def query_gibson(self, query: str) -> dict:
        """
        Sends a query to IX-Gibson and returns the parsed response.

        Args:
            query (str): The user or system query.

        Returns:
            dict: Parsed JSON response or error info.
        """
        payload = {
            "domain": "acidburn",
            "query": query,
            "source": "ix-acidburn"
        }
        for attempt in range(1, self.retries + 1):
            try:
                response = requests.post(self.endpoint, json=payload, timeout=self.timeout)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"[AcidBurn HTTP {response.status_code}] {response.text}")
            except requests.RequestException as e:
                print(f"[AcidBurn] Gibson request error (attempt {attempt}): {e}")

            if attempt < self.retries:
                time.sleep(self.backoff)

        return {"error": "Failed to retrieve response from IX-Gibson after retries."}
