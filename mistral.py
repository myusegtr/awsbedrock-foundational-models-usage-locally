import boto3
import json

prompt_data = """
Give me latest news on AI
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "prompt": "[INST] " + prompt_data + " [/INST]",
    "max_tokens": 200,
    "temperature": 0.5,
    "top_p": 0.9,
    "top_k": 50
}

body = json.dumps(payload)
model_id = "mistral.mistral-7b-instruct-v0:2"

response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())

# ✅ The actual key is likely 'outputs', not 'message'
generated_text = response_body.get("outputs", [{}])[0].get("text", "No output text found.")
print("Model response:\n", generated_text)
