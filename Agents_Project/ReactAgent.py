import WebSearch
import os
from WebSearch import WebSearch
from dotenv import find_dotenv, load_dotenv
from groq import Groq


class ResearchAgent:
    def __init__(self):
        """Initialize with API keys for Groq and Tavily."""
        load_dotenv(find_dotenv())
        groq_api_key = os.environ["GROQ_API_KEY"]
        self.client = Groq(api_key=groq_api_key)
        self.web_search = WebSearch()


    def generate_research_questions(self, topic):
        """Generate research questions using LLM."""
        prompt = "Generate five detailed research questions limited to 250 characters about the topic: %s." % topic
        response = self.client.chat.completions.create(messages=[{"role": "user",
                                                  "content": prompt}],
                                       model="llama3-8b-8192")

        questions = response.choices[0].message.content.split("\n")
        return [q.strip() for q in questions if q.strip()]

    def gather_information(self, topic):
        """Search for answers to generated research questions."""
        questions = self.generate_research_questions(topic)
        structured_info = {}

        for question in questions:
            search_results = self.web_search.search(question, num_results=3)
            structured_info[question] = search_results

        return structured_info

    def display_information(self, structured_data):
        """Nicely format collected data."""
        for question, results in structured_data.items():
            print(f"\nQuestion: {question}")
            for idx, result in enumerate(results, 1):
                print(f"  Result {idx}:")
                print(f"    Title: {result['title']}")
                print(f"    Content: {result['content'][:300]}...")  # Showing first 300 characters


# Example usage
if __name__ == "__main__":
    #OPENAI_API_KEY = "your_openai_api_key_here"
    #TAVILY_API_KEY = "your_tavily_api_key_here"

    agent = ResearchAgent()
    topic = "Artificial intelligency impacts on Software industry"

    research_data = agent.gather_information(topic)
    agent.display_information(research_data)