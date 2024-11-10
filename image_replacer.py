from PIL import Image

# Paths to your images
image1_path = "desktop_screenshot.png"  # First image to insert
image2_path = "tablet_screenshot.png"  # Second image to insert
image3_path = "phone_screenshot.png"  # Third image to insert

# Coordinates for placeholders in the template image (x, y, width, height)
placeholders = [
    (2393, 3810, 5885, 3685),  # Placeholder 1 - Laptop
    (7589, 5390, 2714, 3902),  # Placeholder 2 - Tablet
    (5541, 6243, 1615, 3495),  # Placeholder 3 - Phone
]


# Function to resize and paste images onto the background
def paste_image(background, image_path, coords):
    with Image.open(image_path) as img:
        # Resize the image to fit placeholder dimensions with antialiasing for better quality
        img_resized = img.resize((coords[2], coords[3]), Image.LANCZOS)
        #img.thumbnail((coords[2], coords[3]), Image.LANCZOS)

        # Calculate the position to center the image in the placeholder
        #left = coords[0] + (coords[2] - img.width) // 2
        #top = coords[1] + (coords[3] - img.height) // 2

        # Paste the resized image onto the background at the calculated position
        background.paste(img_resized, (coords[0], coords[1]))


def create_composite_image(template_path, screenshot_paths, output_path):
    # Load the template image (with transparency)
    with Image.open(template_path).convert("RGBA") as template:
        # Create a blank background image with the same size as the template
        background = Image.new("RGBA", template.size, (255, 255, 255, 0))  # Transparent background

        # Paste each image onto the background in its respective placeholder position
        paste_image(background, image1_path, placeholders[0])
        paste_image(background, image2_path, placeholders[1])
        paste_image(background, image3_path, placeholders[2])

        # Composite the background and template layers together
        final_image = Image.alpha_composite(background, template)

        # Save or show the final image
        output_path = "final_composite.png"

        # Save the final composite image with lossless PNG format to preserve quality
        final_image.save(output_path, format="PNG")
        # with Image.open(output_path) as img:
        #     #img_resized = img.resize((1024,1024), Image.LANCZOS)
        #     img.thumbnail((1024,1024), Image.LANCZOS)
        #     img.save(output_path, format="PNG")
        print(f"Image saved as {output_path}")

# Uncomment below if you want to run this script directly with example files
# create_composite_image("template_with_transparency.png",
#                        ["desktop_screenshot.png", "tablet_screenshot.png", "phone_screenshot.png"],
#                        "final_composite.png")