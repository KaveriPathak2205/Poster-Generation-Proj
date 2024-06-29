from PIL import Image, ImageDraw, ImageFont, ImageOps
import matplotlib.pyplot as plt

# Create a new image with white background
width, height = 800, 1200
poster = Image.new('RGBA', (width, height), 'white')

draw = ImageDraw.Draw(poster)

# Draw black rectangle for the top left section
draw.rectangle([(0, 0), (width - 300, height / 2 + 20)], fill='black')

# Draw a brown vertical border
draw.rectangle([(width - 300, 0), (width - 290, height / 2 + 20)], fill='brown')

# Draw a white horizontal border
draw.rectangle([(0, height / 2 + 20), (width - 300, height / 2 + 30)], fill='brown')

# Draw full rectangle for the right section
light_brown= "#F5F5EF"  
draw.rectangle([(width - 290, 0), (width, height)], fill= light_brown)

# Draw light blue rectangle for the bottom left section
light_blue = "#E9F1FF"  # RGB for beige
draw.rectangle([(0, height / 2 + 30), (width - 290, height)], fill=light_blue)

#def add_rounded_corners(image, radius):
 #   # Create a mask for rounded corners
  #  mask = Image.new("L", image.size, 0)
   # draw = ImageDraw.Draw(mask)
    #draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
    
    # Apply rounded mask to image
    #rounded_image = ImageOps.fit(image, mask.size)
    #rounded_image.putalpha(mask)
    #return rounded_image

# Open and paste the first image
image1 = Image.open(r'C:\Users\utpal\OneDrive\Desktop\advertgallery_images\image1.png').resize((360, 360))
#image1_rounded = add_rounded_corners(image1, radius=100)
poster.paste(image1, (width // 3 + 50, height // 3 - 50))

# Open and paste the second image
image2 = Image.open(r'C:\Users\utpal\OneDrive\Desktop\advertgallery_images\image2.png').resize((360, 360))
#image2_rounded = add_rounded_corners(image2, radius=200)
poster.paste(image2, (width // 2 + 110, height // 2 + 270))

# Add text to the poster
font_path = "arial.ttf"  # Update this with the path to your font file

# Title text
title_font = ImageFont.truetype(font_path, 80)
draw.text((50, 50), "TITLE", font=title_font, fill="white")

# Description text
desc_font = ImageFont.truetype(font_path, 25)
draw.text((50, height // 2 - 120), "DESCRIPTION.", font=desc_font, fill="white")

# Sub-heading text
subheading_font = ImageFont.truetype(font_path, 40)
draw.text((20, height / 2 + 80), "SUB-HEADING", font=subheading_font, fill='black')

# Location text
location_font = ImageFont.truetype(font_path, 30)
draw.text((30, height - 220), "location", font=location_font, fill='black')

# Contact us text
contact_font = ImageFont.truetype(font_path, 30)
draw.text((30, height - 100), "Contact us", font=contact_font, fill='black')

# Add Veehive.ai text and logo
veehive_font = ImageFont.truetype(font_path, 28)
draw.text((width - 250, 40), "Veehive.ai", font=veehive_font, fill="black")

logo = Image.open(r'C:\Users\utpal\OneDrive\Desktop\advertgallery_images\logo.png').resize((80, 80)).convert("RGBA")
poster.paste(logo, (width - 100, 20), logo)

# Saving the poster
poster.save(r'C:\Users\utpal\OneDrive\Desktop\poster.png')

# Display the poster
plt.imshow(poster)
plt.axis('off')
plt.show()
