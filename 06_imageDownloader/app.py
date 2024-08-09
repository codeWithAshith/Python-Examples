import os
import requests

# Create a folder called images
# https://www.python.org/static/community_logos/python-logo-master-v3-TM.png

def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']

    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image extension could not be located...')

    if os.path.isfile(image_name):
        raise Exception('File name already exists...')

    try:
        # Get the image as bytes and write it locally to our computer
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded: "{image_name}" successfully!')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    # Get the user input for the download
    input_url: str = input('Enter a url: ')
    input_name: str = input('What would you like to name it?: ')

    # Download the image
    print('Downloading...')
    download_image(input_url, name=input_name, folder='images')