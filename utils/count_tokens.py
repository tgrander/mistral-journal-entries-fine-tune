import os
print("Current Working Directory:", os.getcwd())

def count_tokens(file_path):
    try:
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Tokenize the text; this simple split method considers words as tokens
        tokens = text.split()

        # Count the tokens
        return len(tokens)

    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Replace 'your_file.txt' with your text file's path
file_path = 'data/raw/stories/incest/ex-con-uncle-adam-comes-to-stay/ex-con-uncle-adam-comes-to-stay-1.txt'
token_count = count_tokens(file_path)
print(f"Number of tokens in the file: {token_count}")
