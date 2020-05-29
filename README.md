# Python Download Data

Python script to scrape / download various data sources.

## Setup

1. Clone this repo:

   ```bash
   git clone git@github.com:yegorski/python-scrape-data.git
   cd python-scrape-data
   ```

1. Install Python script dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

### From Zillow Static

Downloads files from <http://files.zillowstatic.com>.

1. Make a `.env` file with the zillowstatic URL you want to download from:

   ```ini
   URL=http://files.zillowstatic.com/research/public_v2/zhvi/Metro_Zhvi_AllHomes.csv
   SAVE_TO=files/Metro_Zhvi_AllHomes.csv
   ```

1. Run `python3 zillowstatic.py`.

### Kaggle

Downloads `median-listing-price-1-bedroom` data from [Kaggle][].

1. Create a [Kaggle][] account.
1. Make a `.env` file with your Kaggle credentials:

   ```ini
   KAGGLE_USERNAME=<username>
   KAGGLE_PASSWORD=<password>
   URL=https://www.kaggle.com/zillow/median-listing-price-1-bedroom/download
   SAVE_TO=files/listings.zip
   ```

1. Run `python3 kaggle.py`.
1. Unzip and inspect the downloaded file.

[kaggle]: https://www.kaggle.com/
