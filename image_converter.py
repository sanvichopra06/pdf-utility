from PIL import Image

def validate_image(path):
    try:
        with Image.open(path) as img:
            img.verify()

        print("Valid Image")
        return True

    except Exception:
        print("Invalid/Corrupted Image")
        return False

def images_to_pdf(images_file, output_file):
    if not images_file:
        print("No images provided")
        return False
    images = []
    try:
        for path in images_file:
            with Image.open(path) as img:
                converted_img = img.convert("RGB")
                images.append(converted_img)
        images[0].save(
            output_file,
            save_all=True,
            append_images=images[1:]
        )

        print("Images converted")
        return True
    except Exception as e:
        print(f"Error {e}")
        return False
    finally:
        for img in images:
            img.close()