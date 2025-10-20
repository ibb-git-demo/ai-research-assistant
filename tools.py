from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, DuckDuckGoSearchAPIWrapper
from langchain_core.tools import tool
from datetime import datetime

# Araştırma sonuçlarını dosyaya kaydetme aracı
@tool
def save_text_to_file(data: str, filename: str = "research_output.txt") -> str:
    """Saves structured research data to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Formatlanmış metni hazırla
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    
    # Dosyaya yaz
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

# DuckDuckGo web arama aracı - daha fazla sonuç
try:
    search_wrapper = DuckDuckGoSearchAPIWrapper(max_results=5)
    search = DuckDuckGoSearchRun(api_wrapper=search_wrapper)
    
    @tool
    def search_web(query: str) -> str:
        """Search the web for information using DuckDuckGo."""
        try:
            result = search.run(query)
            return result if result else "No results found"
        except Exception as e:
            return f"Search error: {str(e)}"
    
except Exception as e:
    # DuckDuckGo kurulu değilse alternatif kullan
    print(f"Warning: DuckDuckGo not available: {e}")
    
    @tool
    def search_web(query: str) -> str:
        """Search the web for information. (Mock version - install duckduckgo-search for real search)"""
        return f"Search results for: {query}\n(Note: Install duckduckgo-search for real web search)"

# Wikipedia arama aracını yapılandır
api_wrapper = WikipediaAPIWrapper(
    top_k_results=2,
    doc_content_chars_max=1000
)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# Tool'ları dışa aktar
search_tool = search_web
save_tool = save_text_to_file