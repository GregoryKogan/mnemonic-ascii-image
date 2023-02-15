from mnemonic import Mnemonic


def main():
    words = ["Hello", "world", "!"]
    for word in words:
        print(f"Seed: '{word}'")
        Mnemonic.display_ascii_image(size=(60, 40), seed=word, char="█")


if __name__ == "__main__":
    main()
