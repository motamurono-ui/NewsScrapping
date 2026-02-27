import asyncio
import httpx
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent
from typing import List, Dict

async def fetch_news() -> None:
    """
    Fetches the top 10 news from Hacker News and saves them to a CSV file.
    """
    url: str = "https://news.ycombinator.com/"
    ua = UserAgent()
    headers: Dict[str, str] = {"User-Agent": ua.random}

    print(f"Accessing {url}...")

    async with httpx.AsyncClient(headers=headers) as client:
        try:
            response = await client.get(url)
            response.raise_for_status() 
            
            soup = BeautifulSoup(response.text, "html.parser")
            titles = soup.select(".titleline > a")
            
            data: List[Dict[str, str]] = []
            
            for item in titles[:10]:
                data.append({
                    "Title": item.get_text(),
                    "Link": item["href"]
                })
            
            # Data processing
            df = pd.DataFrame(data)
            print("\nFOUND:")
            print(df)
            
            # Export to CSV
            filename: str = "tech_news.csv"
            df.to_csv(filename, index=False)
            print(f"\nFile '{filename}' generated successfully.")
            
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(fetch_news())