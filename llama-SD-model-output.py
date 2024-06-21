import json
import torch
from langchain import PromptTemplate
from llama_cpp import Llama
from diffusers import StableDiffusionPipeline


# Loading LLaMA model from the specified path
llm = Llama(model_path="llama3env/Llama3Pipline/models/phi3.gguf",
            n_ctx=1000,
            n_threads=8,
            n_gpu_layers=35,
            verbose=False)


# Define the prompt template
# This template defines how the input will be structured for the LLaMA model.
system_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
create a poster with these specifications: {user_input}. Make sure to include title, background color, background image,
text that should be included in the poster.

"""
)


# Generating the Poster Specifications
# Function to call LLaMA model and get a response
# This function sends the formatted input to the LLaMA model and parses the response as JSON.
def llama3(user_input: str) -> dict:
    model_input = system_prompt.format(user_input=user_input)
    response = llm(model_input, max_tokens=512)
    response_text = response['choices'][0]['text']

    # Parse response text as JSON
    response_json = json.loads(response_text)
    return response_json


# Loading the Stable Diffusion Model
# This initializes the Stable Diffusion pipeline and moves it to the appropriate device (GPU or CPU).
model_path = "CompVis/stable-diffusion-v-1-4-original"  # Update this path
sd_pipeline = StableDiffusionPipeline.from_pretrained(model_path).to("cuda" if torch.cuda.is_available() else "cpu")


# Function to generate an image using Stable Diffusion
# This function generates an image based on the given prompt and saves it to the specified path.
def generate_image(prompt: str, output_path: str):
    image = sd_pipeline(prompt).images[0]
    image.save(output_path)
    return output_path


# Example user input
# The combined code gets poster specifications from the LLaMA model and uses the background image description to generate an image with the Stable Diffusion model.
user_input = "a summer event with beach theme, including sandy background, ocean waves, and event details."
poster_specifications = llama3(user_input)
print("Generated Poster Specifications:", poster_specifications)

# Generate image based on the background image description
background_image_prompt = poster_specifications["poster_backgroundImage"]["background image"]
image_output_path = "poster_image.png"
generated_image_path = generate_image(background_image_prompt, image_output_path)
print(f"Generated image saved at: {generated_image_path}")
