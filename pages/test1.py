import requests

# Define the API endpoint and API key
endpoint = "https://api.openai.com/v1/engines/text-davinci/jobs"
api_key = "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"

# Define the text to generate
prompt = "The quick brown fox jumps over the lazy dog."

# Define the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define the request body
data = {
    "prompt": prompt,
    "max_tokens": 100,
    "temperature": 0.5,
}

# Send the API request
response = requests.post(endpoint, headers=headers, json=data)

# Check the API response status
if response.status_code != 200:
    raise Exception("Failed to generate text: " + response.text)

# Print the generated text
generated_text = response.json()["choices"][0]["text"]
print(generated_text)
