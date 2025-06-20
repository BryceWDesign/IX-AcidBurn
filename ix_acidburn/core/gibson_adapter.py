"""
IX-AcidBurn Gibson Adapter

Provides the interface for IX-AcidBurn to communicate with the IX-Gibson
central knowledge hub for domain-specific expert queries.
"""

import requests
import time
from config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS

class GibsonAdapter:
    def __init__(self):
        self.api_url = GIBSON_API_URL
        self.timeout = REQUEST_TIMEOUT_SECONDS
        self.retries = RETRY_ATTEMPTS
        self.backoff = RETRY_BACKOFF_SECONDS

    def query_gibson(self, question: str) -> dict:
        """
        Send a question to IX-Gibson and return the response JSON.

        Args:
            question (str): The domain-specific question to ask.

        Returns:
            dict: JSON response from Gibson or error details.
        """
        payload = {
            "domain": "acidburn",
            "question": question,
            "from": "ix-acidburn"
        }
        for attempt in range(1, self.retries + 1):
            try:
                response = requests.post(self.api_url, json=payload, timeout=self.timeout)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Gibson HTTP {response.status_code}: {response.text}")
            except requests.RequestException as e:
                print(f"Gibson request error attempt {attempt}: {e}")

            if attempt < self.retries:
                time.sleep(self.backoff)

        return {"error": "Failed to communicate with IX-Gibson after retries."}
