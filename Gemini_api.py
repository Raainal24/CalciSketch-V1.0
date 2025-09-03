
import google.generativeai as genai

genai.configure(api_key="insert api key")

generation_config = {
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

prompt_parts = [
    genai.upload_file("D:\\Studies\\Mini Project 3\\Python\\canvas_image.jpg"),
    "give me the answer to this calculation."
]

response = model.generate_content(prompt_parts)

try:
    print(response.text)
except Exception as e:
    print("Exception:\n", e, "\n")

    print("Response:\n", response.candidates)
