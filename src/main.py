import random
from generator import RandomImageGenerator
import ascii_magic


def main():
    gen = RandomImageGenerator()
    img = gen.generate((60, 40), random.randint(100, 999))
    my_art = ascii_magic.obj_from_image(img)
    my_art.to_terminal(columns=60)


if __name__ == "__main__":
    main()
