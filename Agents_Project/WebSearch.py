from tavily import TavilyClient
import tavily
import os
from dotenv import find_dotenv, load_dotenv
class WebSearch:
    tavilyclient = "" # Assign TavilyClient
    def __init__(self):
        """Initialize with Tavily API key."""
        load_dotenv(find_dotenv())
        self.tavilyclient = TavilyClient(os.environ["TAVILY_API_KEY"])


    def search(self, query, num_results=5):
        """Perform web search and extract relevant information."""
        response = self.tavilyclient.search(query=query, max_results=num_results)
        results = []
        for result in response['results']:
            title = result.get("title", "No title available")
            content = result.get("content", "No content available")
            results.append({"title": title, "content": content})

        return results

