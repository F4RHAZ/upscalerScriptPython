import os
import replicate
import requests

# Define your API token
#Take the API token from https://replicate.com/nightmareai/real-esrgan and put it in an .....
#... environment file for security purpose and use it here or just do as done in this code

api_token = "apit token ommited"

# Setup client API
os.environ["REPLICATE_API_TOKEN"] = "apit token"

# Prompt the user to select a folder containing images
input_folder = input("Enter the path to the folder containing images: ")

# Check if the selected folder exists
if not os.path.exists(input_folder):
    print(f"The folder '{input_folder}' does not exist.")
else:
    # Create the "upscaled" folder within the selected folder
    output_folder = os.path.join(input_folder, "upscaled")
    os.makedirs(output_folder, exist_ok=True)

    # List all the image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", "JPG"))]

    # Check if there are images in the folder
    if not image_files:
        print(f"No image files found in '{input_folder}'.")
    else:
        # Iterate through the image files, run them through replicate, and save the upscaled images
        for i, image_file in enumerate(image_files, start=1):
            input_image_path = os.path.join(input_folder, image_file)

            # Provide a progress update
            print(f"Processing image {i} of {len(image_files)}: {image_file}")

            output = replicate.run(
                "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
                input={"image": open(input_image_path, "rb"), "scale": 2}
            )
            url = output

            # Send an HTTP GET request to the URL
            response = requests.get(url)

            if response.status_code == 200:
                # Specify the local file path where you want to save the downloaded file
                local_file_path = os.path.join(output_folder, image_file)
                # Open the local file in binary write mode and write the content of the response to it
                with open(local_file_path, "wb") as local_file:
                    local_file.write(response.content)
                print(f"Image {i} scaled and saved to '{local_file_path}'.")
            else:
                print(f"Failed to download the file for image {i}. Status code: {response.status_code}")

    print("Image upscaling completed.")
