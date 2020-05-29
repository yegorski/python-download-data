# -*- coding: utf-8 -*-
import os
import logging
import zipfile

from dotenv import find_dotenv, load_dotenv
from io import BytesIO
from requests import session 


def main(url, save_to, username, password):
    logger.info(f"👇 Downloading data file from {url}")
    with session() as c:
        login_response = c.post("https://www.kaggle.com/account/login", data={
            'action': 'login',
            'username': username,
            'password': password,
        })
        with open(save_to, 'wb') as handle:
            response = c.get(url, stream=True)
            for block in response.iter_content(1024):
                handle.write(block)
    logger.info(f"✅ Downloaded data file from {url}")


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    log_fmt = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    username = os.environ.get("KAGGLE_USERNAME")
    password = os.environ.get("KAGGLE_PASSWORD")
    url = os.environ.get("URL")
    save_to = os.environ.get("SAVE_TO")

    main(url, save_to, username, password)
