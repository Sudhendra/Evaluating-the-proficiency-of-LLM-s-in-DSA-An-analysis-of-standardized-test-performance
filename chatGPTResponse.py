from openai import OpenAI
from tqdm import tqdm
import os

key = ""
client = OpenAI(api_key=key)

prompts = [
    "",
    "",
    "You are an expert in Data Structures and Algorithms & you only give accurate solutions in python. You do not generate any additional text apart from the code.",
    "You are an expert Python developer focused on data structures and algorithms. Write an efficient Python function as provided in the code stub that adheres strictly to the problem's specifications and optimizes for both time and space. You do not generate any additional text or characters apart from the code.",
    "As a professional Python programmer specializing in data structures and algorithms, implement a solution for this LeetCode problem using the exact code signature provided. Ensure your code handles all constraints, edge cases and is optimized for performance. You do not generate any additional text apart from the code.",
    "You are tasked as a Python software engineer to develop code solving this algorithmic challenge. Write the cleanest and most efficient code, considering all given constraints and using the specified function names. You do not generate any additional text apart from the code.",
    "As a junior programmer, attempt to solve this problem in Python. Use what you’ve learned so far about data structures and algorithms. You do not generate any additional text apart from the code.",
    "You are a software engineering student. Please try to write Python code to solve this problem based on your current knowledge. You do not generate any additional text apart from the code.",
    "As an enthusiastic hobbyist coder, draft a Python script to tackle this algorithm problem efficiently. You do not generate any additional text apart from the code.",
]

class ResponseError(Exception):
    """Custom exception for handling response errors."""
    pass

def gptResponse(sample_question, prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": sample_question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        raise ResponseError(f"Stopping due to error with prompt: {prompt}")

def writeResponse(file_path, response):
    with open(file_path, 'w') as file:
        file.write(response)

def main():
    question_dir = "/home/mohit.y/chatGPT/questions"
    base_response_dir = "/home/mohit.y/chatGPT/responses"

    for idx, prompt in enumerate(prompts):
        prompt_dir = os.path.join(base_response_dir, str(idx+3))  # Adjusted as per your setup
        os.makedirs(prompt_dir, exist_ok=True)
        existing_files = set(os.listdir(prompt_dir))  # Get existing files once

        try:
            for q_file_name in tqdm(os.listdir(question_dir)):
                if q_file_name.startswith('q_') and q_file_name not in existing_files:
                    q_file_path = os.path.join(question_dir, q_file_name)
                    with open(q_file_path, 'r') as f:
                        question_content = f.read()
                        response_content = gptResponse(question_content, prompt)
                        if response_content is not None:
                            response_file_path = os.path.join(prompt_dir, q_file_name)
                            writeResponse(response_file_path, response_content)
        except ResponseError as re:
            print(re)  # Log the error message
            continue  # Move to the next prompt if an error occurs

if __name__ == "__main__":
    main()
    print("Processing complete!")
