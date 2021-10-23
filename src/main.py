from PIL import Image, ImageOps
import random

# Set the width and height of each quarter (The image is always square)
dim = 10

# Set the global colour so that each coloured pixel is monotone
colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def quarter(dimension) -> Image:
    # Initialize empty image
    one_quarter = Image.new("RGB", (dimension, dimension))

    # Loop over every pixel and set it to one of two colours
    for i in range(dimension):
        for j in range(dimension):
            # Each pixel has a 50% chance of being coloured
            is_coloured = random.randint(0, 2)
            if is_coloured == 1:
                one_quarter.putpixel((i, j), colour)
            else:
                # Set the non-coloured pixels to white
                one_quarter.putpixel((i, j), (255, 255, 255))
    return one_quarter


def generate_multiply_stitch() -> Image:
    # Initialize the full image
    full_dim = dim * 2
    full_pfp = Image.new("RGB", (full_dim, full_dim))

    # Generate the 4 quarters by flipping and mirroring the first one
    top_left = quarter(10)
    top_right = ImageOps.mirror(top_left)
    bottom_left = ImageOps.flip(top_left)
    bottom_right = ImageOps.mirror(ImageOps.flip(top_left))

    # Stitch the 4 images together
    full_pfp.paste(top_left, (0, 0))
    full_pfp.paste(top_right, (dim, 0))
    full_pfp.paste(bottom_left, (0, dim))
    full_pfp.paste(bottom_right, (dim, dim))

    return full_pfp


generate_multiply_stitch().save("output.png")
