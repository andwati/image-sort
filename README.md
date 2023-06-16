# Image sorter

# Installation

Requires `python >=3.7`

1. Create a python virtual environment

```
python -m venv venv
```

2. Activate the virtual environment

```
./venv/Scripts/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

# How to use

--source" help="Path to the input folder containing the images"

--destination" help="Path to the pass folder for images that pass the test"

--rejects help="Path to the reject folder for images that fail the test"

```
python cli.py --source <image folder path> --destination <pass folder> --rejects <reject folder>
```

# TODO

- Sort images according to size
- Remove black or blank images
- Remove white/gray images
- Remove blurry images
- Use multithreading to increase performance
- Remove images with no meter readings
- Progress functionality
