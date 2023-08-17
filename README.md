# Lora-Wildcard-maker
Lora Wildcard maker (Randomize Loras)
The "lora_wildcard_maker.py" script is designed to generate wildcard files for Loras (finetuned models) based on their categories within the Stable Diffusion project. When executed from the scripts folder in the Stable Diffusion directory, the script performs the following steps:

Define Directories: The script sets the input and output directories. The input directory is the "models/Lora" folder within the current working directory, while the output directory is the "extensions/stable-diffusion-webui-wildcards/wildcards" folder.

Retrieve Words and Loras: The script traverses through the subdirectories and files within the Lora directory. For each ".civitai.info" file found, it reads the file contents and extracts relevant information. The script removes unnecessary characters and parses the contents as JSON. It retrieves the trained words and the file name, and constructs a lora string based on the file name. The origin (subdirectory name) is appended to the lora string.

Write !loras.txt File: The script creates a file named "!loras.txt" in the output directory. It writes the words and corresponding loras in alphabetical order, excluding the origin information.

Write Subdirectory !loras_{subdirectory}.txt Files: The script creates separate wildcard files for each subdirectory within the Lora directory. For each subdirectory, it creates a file named "!loras_{subdirectory}.txt" in the output directory. It writes the words and corresponding loras that belong to the respective subdirectory, excluding the origin information.

By running this script, you can generate wildcard files that categorize Loras based on their associated words and subdirectories within the Stable Diffusion project. These wildcard files can be used for various purposes, such as filtering and organizing Loras based on their categories.
