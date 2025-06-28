from serpapi import GoogleSearch

# Setup parameters for API request
params = {
    "engine": "amazon",
    "product_id": "B09B8V1LZ3",  # Example ASIN (Product ID)
    "api_key": "75656e424eca033d452fbfed41cf516870c90dbbcd0a04ae8d4f70879ef0e8a0",
    "page": "1"  # Scraping reviews from page 1
}

# Initialize SerpApi client
search = GoogleSearch(params)
result = search.get_dict()

# Extract reviews
reviews = result.get("reviews", [])
for review in reviews:
    print(f"Rating: {review['rating']}")
    print(f"Title: {review['title']}")
    print(f"Content: {review['content']}")
    print("-----")
