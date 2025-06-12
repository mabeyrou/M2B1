from modules.preprocess import preprocessing
import pandas as pd
import joblib
from os.path import join as join
from pathlib import Path

unprocessed_data_path = join('data','ethical_data.csv')
df_preprocessed = pd.read_csv(unprocessed_data_path)

_, _, preprocessor = preprocessing(df_preprocessed)

Path('models').mkdir(exist_ok=True)
preprocessor_path = join('models','preprocessor.pkl')
joblib.dump(preprocessor, preprocessor_path)
