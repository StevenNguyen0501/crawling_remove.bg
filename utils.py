# Requires "requests" to be installed (see python-requests.org)
import os
import requests


def response_no_bg_images(path_source_image_dir, path_no_bg_image_dir, api_key):
    """

    :param path_source_image_dir:
    :param path_no_bg_image_dir:
    :param api_key:
    :return:
    """
    for image_file in os.listdir(path_source_image_dir):
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(os.path.join(path_source_image_dir, image_file), 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': '{}'.format(api_key)},
        )
        if response.status_code == requests.codes.ok:
            with open(os.path.join(path_no_bg_image_dir, image_file.split('.')[0] + '.png'), 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)

