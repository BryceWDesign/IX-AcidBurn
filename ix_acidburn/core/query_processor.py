"""
IX-AcidBurn Query Processor

Handles security exploit questions and vulnerability definitions,
utilizing the exploit knowledge module for fast and precise answers.
"""

from core.exploit_knowledge import ExploitKnowledge

class IXAcidBurnQueryProcessor:
    def __init__(self):
        self.knowledge = ExploitKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            return (
                "I am IX-AcidBurn, your digital forensics and exploits expert. "
                "Ask me things like 'What is SQL injection?', 'Define zero-day', or 'Explain rootkit'."
            )

# Standalone test
if __name__ == "__main__":
    qp = IXAcidBurnQueryProcessor()
    print(qp.process_query("Define buffer overflow"))
    print(qp.process_query("Explain sql injection"))
    print(qp.process_query("What is a rootkit?"))
