from PIL import Image, ImageFilter
import os

def blur_image(image_path, output_path, blur_factor=2):
    try:
        # Open the image and convert it to RGB mode
        image = Image.open(image_path).convert("RGB")

        # Apply the Gaussian blur filter
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_factor))

        # Save the blurred image
        blurred_image.save(output_path)

    except Exception as e:
        print(f"An error occurred while processing '{image_path}': {e}")

def main():
    input_folder = "E:\\Programs\\project\\the_files\\numbers\\unused\\set_2"
    output_folder = "E:\\Programs\\project\\the_files\\numbers\\set_2"
    blur_factor = 1  # You can adjust this value to control the blur intensity

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            blur_image(input_path, output_path, blur_factor)
            print(f"'{filename}' has been processed and saved.")

if __name__ == "__main__":
    main()
