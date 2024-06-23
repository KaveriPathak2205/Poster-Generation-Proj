from PIL import Image, ImageDraw, ImageFont

def create_poster(template_path, text, text_pos, text_color, font_path, font_size, additional_image_path, image_position, image_size):
    # Open the template image
    template_image = Image.open(template_path)

    # Open and resize the additional image
    additional_image = Image.open(additional_image_path)
    additional_image = additional_image.resize(image_size)  # Resize to the specified size

    # Paste the additional image onto the template
    template_image.paste(additional_image, image_position, additional_image)

    # Create an ImageDraw object
    d = ImageDraw.Draw(template_image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Draw the text on the image
    d.text(text_pos, text=text, fill=text_color, font=font)

    # Save the modified image
    output_path = f"{text}_img.png"
    template_image.save(output_path)
    return output_path

# Example usage
template_path = "template.png"
text = "No_One"
text_pos = (820, 760)
text_color = (0, 0, 0)
font_path = "arial.ttf"
font_size = 100

# Collection of additional images and their properties
additional_images = [
    {"path": "additional_image1.png", "position": (500, 500), "size": (300, 300)},
    {"path": "additional_image2.png", "position": (600, 400), "size": (200, 200)},
    {"path": "additional_image3.png", "position": (400, 300), "size": (250, 250)},
]

# Select an additional image and its properties from the collection
selected_image = additional_images[0]  # Change the index to select a different image

# Generate the poster
output_path = create_poster(
    template_path, 
    text, 
    text_pos, 
    text_color, 
    font_path, 
    font_size, 
    selected_image["path"], 
    selected_image["position"], 
    selected_image["size"]
)

print(f"Poster saved to: {output_path}")
