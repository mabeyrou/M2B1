from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def split(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def preprocessing(df):
    """
    Fonction pour effectuer le prétraitement des données :
    - Imputation des valeurs manquantes.
    - Standardisation des variables numériques.
    - Encodage des variables catégorielles.
    """
    numerical_cols = ['revenu_estime_mois', 'risque_personnel', 'loyer_mensuel']
    categorical_cols = ['age_group', 'sport_licence', 'niveau_etude', 'region', 'smoker', 'situation_familiale']
    too_few_data_cols = ['score_credit', 'historique_credits']
    target_col = 'montant_pret'

    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])

    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])

    preprocessor = ColumnTransformer([
        ("num", num_pipeline, numerical_cols),
        ("cat", cat_pipeline, categorical_cols)
    ])

    # Prétraitement
    X = df.drop(columns=too_few_data_cols)
    y = df[target_col]

    X_processed = preprocessor.fit_transform(X)
    return X_processed, y, preprocessor