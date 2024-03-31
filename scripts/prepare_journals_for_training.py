import json
import os

def extract_date_from_filename(filename):
    # Extract the date from the filename
    # Assuming the filename format is 'YYYY-MM-DD-Title.md'
    date_part = filename.split('-')[:3]  # Extracts the year, month, and day
    return '-'.join(date_part)  # Joins them back together with hyphens

def extract_content_from_md(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove Markdown headers and return the content
        return ''.join([line for line in lines if not line.startswith('#')]).strip()

def process_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            date = extract_date_from_filename(filename)
            content = extract_content_from_md(file_path)
            yield {"date": date, "note": content}
