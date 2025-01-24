from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {
    "target_weight": "",
    "current_weight": "",
    "protein_intake": "",
    "calories_intake": "",
    "dietary_preference": "",
    "medical_conditions": ""
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@anudeep/diet-plan-generator/{version}"
else:
    flow_name = "@anudeep/diet-plan-generator"

result = client.flow.execute(flow_name, input_data)
print(result)
