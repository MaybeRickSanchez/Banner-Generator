# Unicode Banner Generator

This repository contains a Python script that generates stylized
Unicode-like banner images from custom alphabet glyphs and background
textures.

## Features

-   Builds composite images using:
    -   Custom PNG alphabet glyphs located in the `Alphabets/` directory
    -   Multiple background templates stored in the `backgrounds/`
        directory
-   Automatically adjusts horizontal spacing based on predefined
    character widths
-   Outputs final images to the `UniCodes/` directory
-   Fully configurable and easy to extend with additional glyphs or
    backgrounds

## How It Works

1.  Each character has a width defined in the `widths` dictionary.
2.  The script loads glyph images from `Alphabets/`.
3.  Background images (`BG1.png` to `BG14.png`) are loaded from
    `backgrounds/`.
4.  For every entry in the `ranks` list, the script:
    -   Calculates the total width needed for the output
    -   Resizes and applies a background
    -   Pastes the glyphs onto the canvas at the correct positions
5.  The generated banner is saved into the `UniCodes/` folder.

## Folder Structure

    .
    ├── Alphabets/
    │   ├── A.png
    │   ├── B.png
    │   ├── ...
    │
    ├── backgrounds/
    │   ├── BG1.png
    │   ├── BG2.png
    │   ├── ...
    │
    ├── UniCodes/        # Output folder
    ├── _script.py       # Main code
    └── README.md

## Requirements

-   Python 3.x
-   Pillow (`pip install pillow`)
-   Properly prepared PNG glyphs with transparent backgrounds

## Usage

1.  Place your alphabet PNG files inside `Alphabets/`.

2.  Add background PNGs (named `BG1.png`, `BG2.png`, ...) inside
    `backgrounds/`.

3.  Run with default ranks:

    ``` bash
    python _script.py
    ```

4.  Or specify custom ranks as CLI arguments:

    ``` bash
    python _script.py "TEXT1" "TEXT2"
    ```

5.  The resulting images will appear in the `UniCodes/` folder.

## Author

**TheCleverMr**

Feel free to fork, improve, or submit issues!

------------------------------------------------------------------------

Enjoy creating custom banner images!