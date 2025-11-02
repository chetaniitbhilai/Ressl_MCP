import os
from typing import List

def search_keyword_in_file(file_path: str, keyword: str) -> List[str]:
    if not os.path.exists(file_path):
        return [f"Error: {file_path} not found"]

    keyword = keyword.lower()  # 🔹 Convert keyword to lowercase
    results = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
            if keyword in line.lower():  # 🔹 Convert line to lowercase
                results.append(f"Line {idx}: {line.strip()}")

    if not results:
        return [f"No matches found for '{keyword}'"]

    return results
