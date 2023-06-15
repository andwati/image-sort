# Image sorter 

## ProjectTheia Branch
In this project route, the program is supposed to:
1. Check for valid pictures (in this case picutres with the meters).
2. isolate the valid pictures in a different folder.
3. finally remove or delete all the other pictures that didn't pass the test.

## Instructions from the main branch

### Installation

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

### How to use

--source" help="Path to the input folder containing the images"

--destination" help="Path to the pass folder for images that pass the test"

--rejects help="Path to the reject folder for images that fail the test"

```
python cli.py --source <image folder path> --destination <pass folder> --rejects <reject folder>
```

### TODO

- Sort images according to size
- Remove black or blank images
- Remove white/gray images
- Use multithreading to increase performance
