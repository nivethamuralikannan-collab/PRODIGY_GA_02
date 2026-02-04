# 🖼️ Image Generation Using Stable Diffusion
## 📌 What is this project?
This project demonstrates how to generate images from text prompts using a pretrained Stable Diffusion model. By giving a simple text description, the model creates a realistic image based on your prompt.
## 🤖 What is Stable Diffusion?
Stable Diffusion is a deep learning text-to-image model that converts natural language descriptions into high-quality images.
It is widely used for:
AI art generation
Concept design
Creative illustrations
This project uses the Stable Diffusion v1.5 pretrained model from Hugging Face.
## 🎯 What is the goal of this project?
To understand how text-to-image generation works
To learn how to use pretrained AI models
To generate realistic images using Python
## 🧰 What technologies are used?
Python
PyTorch
Diffusers library
Transformers
Stable Diffusion v1.5
Matplotlib
CUDA (GPU support)
## 💻 What are the system requirements?
Python 3.8 or above
NVIDIA GPU with CUDA support (recommended)
At least 6 GB VRAM
Internet connection (to download the model)
## 📦 Which libraries are required?
Install the required libraries using the following command:
```
pip install diffusers transformers accelerate torch safetensors
```
### ⚙️ How does the code work?
Step 1: Install libraries
Installs all necessary Python packages for running Stable Diffusion.
Step 2: Import modules
Imports PyTorch, Stable Diffusion pipeline, and Matplotlib for displaying images.
Step 3: Load the pretrained model
Loads Stable Diffusion v1.5 from Hugging Face and prepares it for GPU usage.
Step 4: Provide a text prompt
A descriptive sentence that tells the model what image to generate.
Example:
```
A futuristic city with flying cars at sunset, ultra realistic
```
Step 5: Generate the image
The model converts the text prompt into an image.
Step 6: Save the image
The generated image is saved as:
```
generated_image.png
```
Step 7: Display the image
The image is displayed using Matplotlib.
## 🖼️ Sample Output
The output is a high-quality AI-generated image based on the given text prompt.
## ✅ Advantages of this project
Beginner friendly
Uses pretrained model (no training required)
Produces realistic images
Easy to modify prompts
## ⚠️ Limitations
Requires a GPU for faster performance
Image generation may take time on low-end systems
Large model size
## 🚀 Future Improvements
Add different image styles
Allow multiple image generations
Create a simple web interface
Add image upscaling
## Author
Nivetha Muralikannan
