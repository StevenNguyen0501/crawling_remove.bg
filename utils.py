# Requires "requests" to be installed (see python-requests.org)
import cv2
import os
import shutil
import requests
import http.client


def collect_all_file(path_src_parent_dir, path_summary):
    for subdir_src_name in os.listdir(path_src_parent_dir):
        # print(subdir_src_name)
        path_subdir_src = os.path.join(path_src_parent_dir, subdir_src_name)
        try:
            for file_name in os.listdir(path_subdir_src):
                path_file = os.path.join(path_subdir_src, file_name)
                file = cv2.imread(path_file)
                # print(path_file)
                if file.shape[0] > 500 and file.shape[1] > 500:
                    shutil.copy(path_file, os.path.join(path_summary, file_name))
        except:
            continue


def split_files_to_folders(path_src_summary, path_tar_split_parent_dir, NUMBER_OF_FILES_IN_EACH_FOLDER):
    TOTAL_OF_FILES = len(os.listdir(path_src_summary))
    NUMBER_OF_FOLDER = int(TOTAL_OF_FILES // NUMBER_OF_FILES_IN_EACH_FOLDER)
    for index, file_name in enumerate(os.listdir(path_src_summary)):
        for i in range(NUMBER_OF_FOLDER):
            path_tar_current_dir = os.path.join(path_tar_split_parent_dir, '{}'.format(i))
            if not os.path.exists(path_tar_current_dir):
                os.mkdir(path_tar_current_dir)
            if int(i * NUMBER_OF_FILES_IN_EACH_FOLDER) < index < int((i + 1) * NUMBER_OF_FILES_IN_EACH_FOLDER):
                shutil.copy(os.path.join(path_src_summary, file_name), os.path.join(path_tar_current_dir, file_name))


def response_no_bg_images(path_source_image_dir, path_no_bg_image_dir, api_key):
    """

    :param path_source_image_dir:
    :param path_no_bg_image_dir:
    :param api_key:
    :return:
    """
    for i, image_file in enumerate(os.listdir(path_source_image_dir)):
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(os.path.join(path_source_image_dir, image_file), 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': '{}'.format(api_key)},
        )
        if response.status_code == requests.codes.ok:
            with open(os.path.join(path_no_bg_image_dir, image_file.split('.')[0] + '.png'), 'wb') as out:
                out.write(response.content)
            print(i)
        else:
            print("Error:", response.status_code, response.text)


if __name__ == '__main__':
    # collect_all_file('/Users/0s/PycharmProjects/datasets/crawling_remove.bg/version1.0/version1.0_data',
    #                  '/Users/0s/PycharmProjects/datasets/crawling_remove.bg/version1.0/version1.0_summary')

    # split_files_to_folders('/Users/0s/PycharmProjects/datasets/crawling_remove.bg/version1.0/version1.0_summary',
    #                        '/Users/0s/PycharmProjects/datasets/crawling_remove.bg/version1.0/version1.0_split_files', 50)

    path_src_dir = '/Users/0s/PycharmProjects/datasets/crawling_remove.bg/version1.0/version1.0_split_files'
    path_tar_dir = '/Users/0s/PycharmProjects/datasets/crawling_remove.bg/version1.0/version1.0_no_bg'

    with open('/Users/0s/PycharmProjects/crawling_remove.bg/api_key.txt', 'r') as in_file:
        list_folders = os.listdir(path_src_dir)
        list_folders.remove('.DS_Store')
        for file_name in list_folders:
            path_src_subdir = os.path.join(path_src_dir, file_name)
            path_tar_subdir = os.path.join(path_tar_dir, file_name)
            if not os.path.exists(path_tar_subdir):
                os.mkdir(path_tar_subdir)
            for idx, line in enumerate(in_file):
                line = line.rstrip("\n")
                print('Removing background all images in folder {} using API key {} of line {}'.format(file_name, line, idx))
                response_no_bg_images(path_src_subdir, path_tar_subdir, line)
