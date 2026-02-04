# ============================================
# IMAGE GENERATION USING STABLE DIFFUSION
# (BEGINNER FRIENDLY - PRETRAINED MODEL)
# ============================================

# Step 1: Install required libraries (run once)
!pip install diffusers transformers accelerate torch safetensors

# Step 2: Import required modules
import torch
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt

# Step 3: Load pre-trained Stable Diffusion model
print("Loading Stable Diffusion model...")

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16
)

pipe = pipe.to("cuda")  # Use GPU

# Step 4: Enter your text prompt
prompt = "A futuristic city with flying cars at sunset, ultra realistic"

# Step 5: Generate image from text
image = pipe(prompt).images[0]

# Step 6: Save the generated image
image.save("generated_image.png")

# Step 7: Display the image
plt.imshow(image)
plt.axis("off")
plt.title("Generated Image")
plt.show()

print("Image generation completed and saved as generated_image.png")
