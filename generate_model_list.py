# Iterate through all files ending with .whl in the current directory
import glob

# Get all files ending with .whl
files = glob.glob("*.whl")
# Sort the files
files.sort()
# Print a markdown list with links to the files (append https://vuizur.github.io/spacy-model-mirror/ to the beginning of each file)
for file in files:
    print("* [" + file + "](https://vuizur.github.io/spacy-model-mirror/" + file + ")")

