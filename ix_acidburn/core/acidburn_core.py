"""
IX-AcidBurn Core Module

Processes queries related to cryptography and secure communications,
leveraging IX-Gibson for domain knowledge.
"""

from .gibson_adapter import GibsonAdapter

class AcidBurnCore:
    def __init__(self):
        self.gibson = GibsonAdapter()

    def handle_query(self, query: str) -> str:
        """
        Sends query to IX-Gibson and returns the cryptography-focused response.

        Args:
            query (str): User input related to cryptography.

        Returns:
            str: Answer string or error message.
        """
        response = self.gibson.query_gibson(query)
        if "error" in response:
            return f"[AcidBurn Error] {response['error']}"
        return response.get("answer", "[AcidBurn] No answer available.")
