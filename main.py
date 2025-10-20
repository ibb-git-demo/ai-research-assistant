import os
import warnings

# Uyarıları gizle
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GLOG_minloglevel'] = '2'
warnings.filterwarnings('ignore')

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

# API anahtarını al
api_key = os.getenv("GEMINI_API_KEY")

# LLM'i başlat
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

def main():
    print("🤖 AI Research Assistant")
    print("Type 'quit' to exit\n")
    
    while True:
        query = input("What can I help you research? ")
        
        # Çıkış kontrolü
        if query.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        # Web araması yap
        print("\n🔍 Searching the web...")
        search_result = search_tool.invoke(query)
        
        # Wikipedia'da ara
        print("📚 Checking Wikipedia...")
        wiki_result = wiki_tool.invoke(query)
        
        # Özet oluştur
        print("🤖 Generating summary...\n")
        
        prompt = f"""You are a research assistant. Based on the following information sources, answer the user's question comprehensively but CONCISELY.

IMPORTANT: Use the actual search results provided below, not your general knowledge.
Keep your answer focused and to-the-point. Use bullet points for clarity.

Web Search Results:
{search_result}

Wikipedia Information:
{wiki_result}

User Question: {query}

Provide a detailed but CONCISE answer (max 300 words) using ONLY the information from the search results above."""
        
        # Yanıt al ve göster
        response = llm.invoke(prompt)
        print(f"✨ Summary:\n{response.content}\n")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()