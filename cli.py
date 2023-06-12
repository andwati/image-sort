import argparse
from pathlib import Path
from sorter.image_sorter import process_image

# CLI argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description="Clean images from electricity meter readings.")
    parser.add_argument("--source", type=str, help="Path to the input folder containing the images")
    parser.add_argument("--destination", type=str, help="Path to the pass folder for images that pass the test")
    parser.add_argument("--rejects", type=str, help="Path to the reject folder for images that fail the test")
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()
    
    # Set paths for input and output folders
    input_folder = Path(args.source)
    pass_folder = Path(args.destination)
    reject_folder = Path(args.rejects)
    
    # Create output folders if they don't exist
    pass_folder.mkdir(parents=True, exist_ok=True)
    reject_folder.mkdir(parents=True, exist_ok=True)
    
    # Get the list of image paths in the input folder
    image_paths = list(input_folder.glob("*.jpg")) + list(input_folder.glob("*.png"))
    
    # Process the images
    for image_path in image_paths:
        process_image(image_path, pass_folder, reject_folder)
    
    print("Sorting complete.")

if __name__ == "__main__":
    main()
