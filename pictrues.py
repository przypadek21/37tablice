from argparse import ArgumentParser
from glob import glob
from PIL import Image

parser = ArgumentParser(description='Zamiana JPG na czarno-białe.')
parser.add_argument('--input', help='Folder z ktorego pobieramy', required=True)
parser.add_argument('--output', help='Folder do ktorego wrzucam', required=True)
args = parser.parse_args()

for path in glob(args.input + '/*'):
    directory, filename = path.split('\\')
    print(path, directory, filename)

    with Image.open(path) as new_image:
        grayscale_image = new_image.convert('L')
        grayscale_image.save(args.output + '/' + filename)
