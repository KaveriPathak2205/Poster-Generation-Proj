import json
import torch
from langchain import LLMChain, PromptTemplate
from transformers import LlamaForCausalLM, LlamaTokenizer
from diffusers import StableDiffusionPipeline

# Path to the LLaMA model
model_path = "path_to_your_llama_model"  # Update this path to where your model is stored

# Load the LLaMA model and tokenizer
model = LlamaForCausalLM.from_pretrained(model_path)
tokenizer = LlamaTokenizer.from_pretrained(model_path)

# Set device to GPU if available, otherwise use CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define the system prompt template
system_prompt = PromptTemplate(input_variables=["user_input"],
    template="""
create a poster with these specifications: {user_input} and make sure to include title, background color, background image, text that should be included in the poster. All of this should be returned in the following JSON format:

{
    "poster_title": {"title": "title_value"},
    "poster_text": {"text": "text_value"},
    "poster_backgroundColor": {"background color": "color_value"},
    "poster_backgroundImage": {"background image": "image_value"}
}
"""
)

# Function to call LLaMA model and get a response
def llama3(user_input: str) -> dict:
    # Format the prompt with user input
    model_input = system_prompt.format(user_input=user_input)
    inputs = tokenizer(model_input, return_tensors='pt').to(device)
    outputs = model.generate(inputs['input_ids'])
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Parse the JSON response
    response_json = response[response.find("{"):response.rfind("}")+1]
    output = json.loads(response_json)
    
    return output

# Initialize the Stable Diffusion pipeline
sd_model_path = "path_to_your_stable_diffusion_model"  # Update this path to where your Stable Diffusion model is stored
sd_pipeline = StableDiffusionPipeline.from_pretrained(sd_model_path).to(device)

# Function to generate an image using Stable Diffusion
def generate_image(prompt: str, output_path: str):
    image = sd_pipeline(prompt).images[0]
    image.save(output_path)
    return output_path

# Test run example
user_input = "Design a poster for a summer event with beach theme, including sandy background, ocean waves, and event details."
text_output = llama3(user_input)
print("Generated text specifications:", text_output)

# Generate image based on the background image description
background_image_prompt = text_output["poster_backgroundImage"]["background image"]
image_output_path = "poster_image.png"
generated_image_path = generate_image(background_image_prompt, image_output_path)
print(f"Generated image saved at: {generated_image_path}")
