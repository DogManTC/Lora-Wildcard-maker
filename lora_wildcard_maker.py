import os
import json

# Define directories 
directory = os.path.join(os.getcwd(), "..", "models", "Lora")
output_dir = os.path.join(os.getcwd(), "..", "extensions", "stable-diffusion-webui-wildcards", "wildcards")

# Get words and loras from .civitai.info files
words = {}
subdirectories = set()  # Store the subdirectories

for root, dirs, files in os.walk(directory):
    origin = os.path.basename(root)  # Get the subdirectory name as the origin
    subdirectories.add(origin)  # Add the subdirectory to the set
    for filename in files:
        if filename.endswith(".civitai.info"):
            file_path = os.path.join(root, filename)
            with open(file_path, "r") as file:
                file_contents = file.read()
                modified_contents = file_contents.replace('<lora:', '').replace('>', '') 
                json_data = json.loads(modified_contents)
                trained_words = json_data.get("trainedWords", [])
                if trained_words:
                    word = trained_words[0].strip().strip("\"'[{(").split(",")[0].strip("\"' ]})")
                    file_name = filename.rsplit('.', 1)[0].replace(".civitai", "")
                    lora = f"(lora:{file_name}:1)"  
                    words[word] = f"{lora}-{origin}"  # Append origin to the lora

# Write !loras.txt file
loras_file_path = os.path.join(output_dir, "!loras.txt")
with open(loras_file_path, "w", encoding="utf-8") as file:
    for word, lora in sorted(words.items(), key=lambda x: x[0].lower()):
        lora_without_origin = lora.rsplit('-', 1)[0]  # Remove the "-{origin}" from the line
        file.write(f"{word}, {lora_without_origin}\n")

# Write subdir !loras_{subdirectory}.txt files and remove "-{origin}" from lines
for subdir in subdirectories:
    sub_output_file = os.path.join(output_dir, f"!loras_{subdir}.txt")
    with open(sub_output_file, "w", encoding="utf-8") as file:
        for word, lora in sorted(words.items(), key=lambda x: x[0].lower()):
            if lora.endswith(f"-{subdir}"):  # Check if the line belongs to the current subdirectory
                lora_without_origin = lora.rsplit('-', 1)[0]  # Remove the "-{origin}" from the line
                file.write(f"{word}, {lora_without_origin}\n")