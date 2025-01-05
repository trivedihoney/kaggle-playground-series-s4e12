import os
import zipfile
import sys
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_competition_data(dataset_name: str):
    input_folder = os.getenv('KAGGLE_INPUT_PATH', 'kaggle/input')
    dataset_folder = os.path.join(input_folder, dataset_name)
    
    if not os.path.exists(dataset_folder):
        # Create the input folder if it doesn't exist
        os.makedirs(input_folder, exist_ok=True)
        
        # Initialize Kaggle API
        api = KaggleApi()
        api.authenticate()
        
        # Download the dataset
        print(f'Downloading {dataset_name} dataset...')
        api.competition_download_files(dataset_name, path=input_folder)
        
        # Extract the dataset
        zip_path = os.path.join(input_folder, f'{dataset_name}.zip')
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dataset_folder)
        os.remove(zip_path)
        print('Dataset downloaded and extracted.')
    else:
        print('Dataset already downloaded.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python download_data.py <dataset_name>')
        sys.exit(1)
    download_kaggle_competition_data(sys.argv[1])