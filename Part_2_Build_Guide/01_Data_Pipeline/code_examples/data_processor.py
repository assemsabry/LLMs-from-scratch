import re
import hashlib

def clean_text(raw_text: str) -> str:
    """
    Applies basic normalization and cleaning to raw text.
    Removes HTML tags, normalizes whitespace, and strips trailing spaces.
    """
    # 1. Remove HTML tags (Simple regex for demonstration)
    text = re.sub(r'<[^>]+>', '', raw_text)
    
    # 2. Normalize whitespace (Replace multiple spaces/newlines with a single space)
    text = re.sub(r'\s+', ' ', text)
    
    # 3. Strip leading/trailing whitespace
    return text.strip()

def exact_deduplicate(dataset: list[str]) -> list[str]:
    """
    Demonstrates exact-match deduplication using cryptographic hashing.
    """
    seen_hashes = set()
    deduplicated_dataset = []
    
    for text in dataset:
        # Create an MD5 hash of the text
        text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
        
        # If we haven't seen this hash before, it's a unique document
        if text_hash not in seen_hashes:
            seen_hashes.add(text_hash)
            deduplicated_dataset.append(text)
            
    return deduplicated_dataset

def demonstrate_data_pipeline():
    print("--- LLM Data Cleaning Pipeline Demonstration ---")
    
    # Simulated messy raw data from the web
    raw_dataset = [
        "<html><body>This is a highly factual sentence about biology.</body></html>",
        "   This    is a highly factual sentence about biology.  ", # Exact duplicate (after cleaning)
        "Click here to buy cheap watches!!! http://spam.link",
        "The quick brown fox jumps over the lazy dog."
    ]
    
    print(f"\nOriginal Dataset Size: {len(raw_dataset)} documents")
    
    # Step 1: Clean
    cleaned_dataset = [clean_text(doc) for doc in raw_dataset]
    print("\nAfter Cleaning:")
    for doc in cleaned_dataset:
        print(f"- '{doc}'")
        
    # Step 2: Deduplicate
    deduplicated_dataset = exact_deduplicate(cleaned_dataset)
    print(f"\nAfter Deduplication Size: {len(deduplicated_dataset)} documents")
    for doc in deduplicated_dataset:
        print(f"- '{doc}'")
        
    # Step 3: Quality Filtering (Mock Example)
    # We remove sentences containing "spam.link" or that are too short
    final_dataset = [
        doc for doc in deduplicated_dataset 
        if "spam.link" not in doc and len(doc.split()) > 5
    ]
    
    print(f"\nFinal High-Quality Dataset Size: {len(final_dataset)} documents")
    for doc in final_dataset:
        print(f"- '{doc}'")

if __name__ == "__main__":
    demonstrate_data_pipeline()
