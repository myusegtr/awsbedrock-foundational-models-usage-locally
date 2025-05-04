import boto3
import json

# Define your input prompt
input_text = "Give me the code for palindrome number in python"

# Prepare the payload for Titan model
payload = {
    "inputText": input_text,
    "textGenerationConfig": {
        "maxTokenCount": 3072,
        "stopSequences": [],
        "temperature": 0.7,
        "topP": 0.9
    }
}

# Convert payload to JSON string
body = json.dumps(payload)

# Define model ID for Titan Premier
model_id = "amazon.titan-text-premier-v1:0"

# Initialize the Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# Invoke the model
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Read and parse the response
response_body = json.loads(response.get("body").read())

# Print the generated text
generated_text = response_body['results'][0]['outputText']
print(generated_text)
