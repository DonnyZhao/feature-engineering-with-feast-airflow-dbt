from feast import FeatureService

from features import sales_features, coordinate_features, population_features

location_feature_service = FeatureService(
    name="location_features",
    features=[sales_features, coordinate_features, population_features]
)