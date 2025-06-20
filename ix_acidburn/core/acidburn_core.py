"""
IX-AcidBurn Core Reasoning Module

This module contains the core reasoning logic for IX-AcidBurn, now enhanced
to delegate complex domain-specific queries to IX-Gibson via the GibsonAdapter.
"""

from .gibson_adapter import GibsonAdapter

class AcidBurnCore:
    def __init__(self):
        self.gibson_adapter = GibsonAdapter()

    def answer_query(self, question: str) -> str:
        """
        Process a question, offloading domain-specific parts to IX-Gibson.

        Args:
            question (str): The question string to answer.

        Returns:
            str: Response answer from Gibson or fallback message.
        """
        # For demonstration, all queries routed to Gibson.
        response = self.gibson_adapter.query_gibson(question)
        if "error" in response:
            return f"[AcidBurn Error]: {response['error']}"
        return response.get("answer", "[AcidBurn]: No answer provided.")
