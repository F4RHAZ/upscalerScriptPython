# upscalerScriptPython
Upscale images in a folder using this upscaler API from https://replicate.com/nightmareai/real-esrgan

Real-ESRGAN Image Upscaling Tool
This repository contains a Python script for upscaling images using Real-ESRGAN, a powerful image enhancement model. Real-ESRGAN can improve the quality and resolution of images, making them suitable for various applications.

Prerequisites
Before you begin, ensure you have met the following requirements:

Replicate API Token: To access the Real-ESRGAN model, you need an API token from Replicate. You can obtain your API token by visiting Replicate 
[Real-ESRGAN](https://replicate.com/nightmareai/real-esrgan). Real-ESRGAN and following their instructions.

Getting Started
To get started with this script, follow these steps:

Clone this repository to your local machine or download the script.

Set your Replicate API token as an environment variable for security purposes. You can do this by adding the following line to your environment or in your script:

python
os.environ["REPLICATE_API_TOKEN"] = "YOUR_API_TOKEN"
Replace "YOUR_API_TOKEN" with your actual API token.

Run the script and follow the prompts to upscale your images:

Enter the path to the folder containing the images you want to upscale.
The script will create an "upscaled" folder within the selected folder (if it doesn't already exist).
It will then list and process all the image files in the input folder, upscaling them and saving the results in the "upscaled" folder.
Usage
This script uses the Replicate API to access the Real-ESRGAN model and performs the following steps:

It checks if the specified input folder exists and if there are compatible image files inside it (JPEG, PNG, BMP, GIF).

For each image found in the input folder, it sends the image to the Real-ESRGAN model for upscaling with a scale factor of 2.

The upscaled images are then saved in the "upscaled" folder within the input folder with the same filenames.

Notes
If you have a large number of images to upscale, the process may take some time, as each image is processed one by one.

Make sure your Replicate API token is kept secure and not shared publicly.

You can adjust the scale factor or other parameters by modifying the script according to your requirements.

Acknowledgments

[Real-ESRGAN](https://replicate.com/nightmareai/real-esrgan)
Replicate Real-ESRGAN: For providing access to the Real-ESRGAN model.
Enjoy enhancing your images with Real-ESRGAN! If you encounter any issues or have questions, please feel free to reach out for assistance.




