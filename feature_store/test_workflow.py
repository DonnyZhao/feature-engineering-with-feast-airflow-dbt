from datetime import datetime
import pandas as pd

from feast import FeatureStore


def run_demo():

    store = FeatureStore(repo_path="./feature_repo")

    entity_df = pd.DataFrame.from_dict(
        {
            "LOCATION_ID": [10928],
            "event_timestamp": [
                datetime(2023, 9, 1, 10, 59, 42) # the timestamp when the features were valid
            ]
        }
    )

    # this df contains the all valid features defined for location 109287 in the location_features feature service
    df = store.get_historical_features(
        entity_df=entity_df,
        features=store.get_feature_service("location_features"),
    ).to_df()

    print(df.head())


if __name__ == "__main__":
    run_demo()
