# main.py
from screenshot_capture import capture_website_screenshots
from image_replacer import create_composite_image

# Configuration
url = "https://divineradianceclinic.braineir.com/"  # URL to capture screenshots
template_path = "template_with_transparency.png"  # Template image with transparent placeholders
output_path = "final_composite.png"  # Final output path

# Step 1: Capture website screenshots
screenshot_paths = capture_website_screenshots(url)

# Step 2: Create composite image with the captured screenshots
create_composite_image(template_path, screenshot_paths, output_path)