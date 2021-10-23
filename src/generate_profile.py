#!/usr/bin/env python3
from PIL import Image, ImageOps
import random
import click

# Set the width and height of each quarter (The image is always square)
dim = 10


def quarter(dimension, colour) -> Image:
    # Initialize empty image
    one_quarter = Image.new("RGB", (dimension, dimension))

    # Loop over every pixel and set it to one of two colours
    for i in range(dimension):
        for j in range(dimension):
            # Each pixel has a 1/3rd chance of being coloured
            is_coloured = random.randint(0, 2)
            if is_coloured == 1:
                one_quarter.putpixel((i, j), colour)
            else:
                # Set the non-coloured pixels to white
                one_quarter.putpixel((i, j), (255, 255, 255))
    return one_quarter

@click.command()
@click.option("--size", default=10, prompt="Size of each mosaic of the image")
@click.option("--name", default="output", prompt="Name of the output file")
def genpic(size: int = 10, name: str = "output"):
    colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Initialize the full image
    full_dim = size * 2
    full_pfp = Image.new("RGB", (full_dim, full_dim))

    # Generate the 4 quarters by flipping and mirroring the first one
    top_left = quarter(size, colour)
    top_right = ImageOps.mirror(top_left)
    bottom_left = ImageOps.flip(top_left)
    bottom_right = ImageOps.mirror(ImageOps.flip(top_left))

    # Stitch the 4 images together
    full_pfp.paste(top_left, (0, 0))
    full_pfp.paste(top_right, (size, 0))
    full_pfp.paste(bottom_left, (0, size))
    full_pfp.paste(bottom_right, (size, size))

    # Make sure we end in the right file extension
    if name[4:] != ".png":
        name += ".png"
    full_pfp.save(name)


if __name__ == "__main__":
    genpic()