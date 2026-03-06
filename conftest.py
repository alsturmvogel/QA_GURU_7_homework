import os
import pytest
from zipfile import ZipFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')
ARCHIVE_PATH = os.path.join(RESOURCES_DIR, 'archive.zip')


@pytest.fixture()  # Объявляем функцию фикстурой
def create_archive():
    if not os.path.exists(RESOURCES_DIR):
        os.mkdir(RESOURCES_DIR)

    with ZipFile(ARCHIVE_PATH, 'w') as zip_file:
        zip_file.write(os.path.join(BASE_DIR, 'doc pdf.pdf'), arcname='doc pdf.pdf')
        zip_file.write(os.path.join(BASE_DIR, 'doc xlsx.xlsx'), arcname='doc xlsx.xlsx')
        zip_file.write(os.path.join(BASE_DIR, 'doc csv.csv'), arcname='doc csv.csv')
