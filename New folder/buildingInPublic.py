
import os
import shutil
import pyfiglet


def print_centered_ascii():
    # 1. Get the current terminal size (columns and rows)
    terminal_size = shutil.get_terminal_size(fallback=(80, 24))
    term_width = terminal_size.columns
    term_height = terminal_size.lines

    # 2. Generate the ASCII art text using pyfiglet
    # You can change the font (e.g., "slant", "standard", "isometric1", "doom")
    text = "Building in public"
    ascii_art = pyfiglet.figlet_format(text, font="slant")

    # 3. Process the art line-by-line for horizontal centering
    art_lines = ascii_art.splitlines()
    max_art_width = max(len(line) for line in art_lines) if art_lines else 0

    # Calculate left padding for horizontal centering
    h_padding = max(0, (term_width - max_art_width) // 2)
    centered_lines = [(" " * h_padding) + line for line in art_lines]

    # 4. Calculate vertical padding for vertical centering
    art_height = len(centered_lines)
    v_padding = max(0, (term_height - art_height) // 2)

    # 5. Clear the screen and print with vertical spacing
    os.system("cls" if os.name == "nt" else "clear")

    # Print blank lines to push the text down to the vertical center
    print("\n" * v_padding, end="")

    # Print the centered ASCII art lines
    for line in centered_lines:
        print(line)


if __name__ == "__main__":
    print_centered_ascii()