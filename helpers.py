"""
DO NOT MODIFY THIS FILE!
"""

import os
import gdown
import shutil
import subprocess
import time
from IPython.display import clear_output, display
from git import Repo

ROOT_PATH = '.'

def check_download_file_info(filename: str, shared_url: str, relative_dir: str, url_prefix: str) -> None:
    """
    Validate the parameters for downloading a file.

    Args:
        filename (str): The name of the file to be downloaded.
        shared_url (str): The shared URL of the file.
        relative_dir (str): The relative directory where the file will be saved.
        url_prefix (str): The expected prefix for the URL.

    Raises:
        ValueError: If the URL does not start with the expected prefix, the filename contains '/',
                    or the relative directory is an absolute path.
    """
    if not shared_url.startswith(url_prefix):
        raise ValueError(f"Invalid URL: {shared_url}. It should start with '{url_prefix}'.")
    if '/' in filename:
        raise ValueError(f"Invalid filename: {filename}. It should not contain '/'.")
    if relative_dir.startswith('/'):
        raise ValueError(f"Invalid relative_dir: {relative_dir}. It should not be an absolute path.")


def google_drive_download(filename: str, shared_url: str, relative_dir: str) -> None:
    """
    Download a file from Google Drive.

    Args:
        filename (str): The name of the file to be downloaded.
        shared_url (str): The shared URL of the file on Google Drive.
        relative_dir (str): The relative directory where the file will be saved.

    Raises:
        ValueError: If the shared URL is invalid or other validation issues arise.
    """
    check_download_file_info(filename, shared_url, relative_dir, 'https://drive.google.com')
    save_path = os.path.join(ROOT_PATH, relative_dir)
    os.makedirs(save_path, exist_ok=True)
    output_file = os.path.join(save_path, filename)
    print(f"Downloading '{filename}' from Google Drive to {output_file}")
    gdown.download(url=shared_url, output=output_file, quiet=False, fuzzy=True)


def wget_download(filename: str, shared_url: str, relative_dir: str) -> None:
    """
    Download a file using wget.

    Args:
        filename (str): The name of the file to be downloaded.
        shared_url (str): The shared URL of the file.
        relative_dir (str): The relative directory where the file will be saved.

    Raises:
        ValueError: If the shared URL is invalid or other validation issues arise.
    """
    check_download_file_info(filename, shared_url, relative_dir, 'https://')
    save_path = os.path.join(ROOT_PATH, relative_dir)
    os.makedirs(save_path, exist_ok=True)
    output_file = os.path.join(save_path, filename)
    command = ['wget', shared_url, '-O', output_file, '-v']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            clear_output(wait=True)
            display(output.strip())
        time.sleep(0.1)  # Reduce flickering
    if process.returncode == 0:
        print(f"Download completed successfully: {filename}.")
    else:
        print(f"Download failed with return code {process.returncode}: {filename}.")


def git_clone_checkout(output_dir: str, url: str, branch: str, commit_sha: str) -> None:
    """
    Clone a Git repository and checkout a specific branch and commit.

    Args:
        output_dir (str): The directory where the repository will be cloned.
        url (str): The URL of the Git repository.
        branch (str): The branch to checkout.
        commit_sha (str): The commit SHA to checkout.

    Raises:
        ValueError: If the URL is invalid or other validation issues arise.
    """
    if os.path.exists(os.path.join(ROOT_PATH, output_dir)):
        print("Directory already exists. Skipping clone.")
        return
    if not url.startswith('https://'):
        raise ValueError(f"Invalid URL: {url}. It should start with 'https://'.")
    repo_path = os.path.join(ROOT_PATH, output_dir)
    os.makedirs(repo_path, exist_ok=True)
    repo = Repo.clone_from(url, repo_path)
    repo.git.checkout(branch)
    repo.git.checkout(commit_sha)
    print(f"Repository cloned to {repo_path} and checked out to {branch} at commit {commit_sha}.")


def unpack_file(file_path: str, output_dir: str) -> None:
    """
    Unpack a compressed file into a specified directory.

    Args:
        file_path (str): The path to the compressed file.
        output_dir (str): The directory where the unpacked files will be saved.

    Raises:
        ValueError: If the file does not exist or the format is unsupported.
    """
    full_file_path = os.path.join(ROOT_PATH, file_path)
    if not os.path.exists(full_file_path):
        raise ValueError(f"File not found: {full_file_path}")
    output_path = os.path.join(ROOT_PATH, output_dir)
    os.makedirs(output_path, exist_ok=True)
    file_format = os.path.splitext(full_file_path)[-1]
    print(f"Unpacking {full_file_path}...")
    format_map = {
        '.tar': 'tar', '.tar.gz': 'gztar', '.tar.xz': 'xztar', '.zip': 'zip'
    }
    if file_format in format_map:
        shutil.unpack_archive(full_file_path, output_path, format=format_map[file_format])
        print(f"Successfully unpacked to {output_path}.")
    else:
        raise ValueError(f"Unsupported format: {file_format}. Use .tar, .tar.gz, .tar.xz, or .zip.")
