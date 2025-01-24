# My_Mira_Project
This will give you about the diet ,based on a person preference(s)

# Diet Plan Generator  

## Overview  
The **Diet Plan Generator** is a personalized diet planning tool powered by Mira Flow. It generates custom meal plans based on user inputs like current weight, target weight, dietary preferences, and medical conditions.  

## Features  
- **Custom Diet Plans**: Personalized meal plans tailored to your goals.  
- **Supports Dietary Preferences**: Choose between vegetarian and non-vegetarian options.  
- **Medical Condition Considerations**: Adjusts recommendations to suit health needs.  
- **Easy Integration**: Use with Mira Flow APIs in multiple programming environments.  

## How It Works  
The diet plan is generated based on the following input parameters:  
- **Current weight**: User's current weight in kg/lbs.  
- **Target weight**: Desired weight in kg/lbs.  
- **Protein intake**: Current protein consumption in grams.  
- **Calories intake**: Current daily caloric intake in kcal.  
- **Dietary preference**: Veg or Non-Veg.  
- **Medical conditions**: Any existing health conditions like diabetes, hypertension, etc.  

## API Integration  

### **Using cURL**  
To generate a diet plan using the API, run the following `curl` command:  

```bash  
curl -X POST "https://flow-api.mira.network/v1/flows/flows/anudeep/diet-plan-generator?version=1.0.0" \
-H "content-type: application/json" \
-H "miraauthorization: YOUR_API_KEY" \
--data-raw '{
    "input": {
        "target_weight": "<your_target_weight>",
        "current_weight": "<your_current_weight>",
        "protein_intake": "<your_protein_intake>",
        "calories_intake": "<your_calories_intake>",
        "dietary_preference": "<veg_or_non_veg>",
        "medical_conditions": "<your_medical_conditions>"
    }
}'
```  

### **Using Python**  
Here’s how you can execute the flow using the **Mira SDK**:  

```python  
from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {
    "target_weight": "<your_target_weight>",
    "current_weight": "<your_current_weight>",
    "protein_intake": "<your_protein_intake>",
    "calories_intake": "<your_calories_intake>",
    "dietary_preference": "<veg_or_non_veg>",
    "medical_conditions": "<your_medical_conditions>"
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@anudeep/diet-plan-generator/{version}"
else:
    flow_name = "@anudeep/diet-plan-generator"

result = client.flow.execute(flow_name, input_data)
print(result)
```  

## Inputs Explanation  

| Parameter            | Description                                      | Example               |
|----------------------|--------------------------------------------------|-----------------------|
| `target_weight`      | Desired target weight in kg/lbs                 | `65`                 |
| `current_weight`     | Current weight in kg/lbs                        | `75`                 |
| `protein_intake`     | Current daily protein consumption in grams       | `50`                 |
| `calories_intake`    | Current daily caloric intake in kcal             | `2000`               |
| `dietary_preference` | User's dietary preference (`Veg` or `Non-Veg`)   | `Veg`                |
| `medical_conditions` | Existing medical conditions or allergies         | `Diabetes`           |

## Output  
The API will return a JSON response containing a detailed, personalized diet plan formatted as per the inputs provided.  

## Requirements  
- Python 3.8+ (if using the Mira SDK).  
- A valid Mira Flow **API Key**.  

## Installation  

### Mira SDK  
Install the Mira SDK for Python:  
```bash  
pip install mira-sdk
```  

## License  
This project is licensed under the MIT License.  

## Author  
**Anudeep**  

