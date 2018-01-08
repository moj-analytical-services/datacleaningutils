from datacleaningutils.utils import read_json
from datacleaningutils.data_types import rough_heuristic_pd_column_type_check

def check_compatible_with_metadata(df, metadata_path):
    """
    Check that a pandas dataframe is compatible with metadata

    Does the df contain all the columns specified in the metadata?
    Are the columns in the correct order?
    Also performs a rough heuristic check to see whether the data types are ok

    Args:
        df: The dataframe you want to check against the metadata definition
        metadata_path:  File path to the json metadata file

    Returns:
        Nothing
    """
    spec = read_json(metadata_path)

    metadata_type_lookup = {v["name"]:v["type"] for v in spec["columns"]}
    metadata_cols = [c["name"] for c in spec["columns"]]
    metadata_cols_set = set(metadata_cols)
    df_cols_set = set(df.columns)

    # Check check all the columns exist in the right order
    if list(df.columns) != metadata_cols:

        message = ""

        # Figure out the problem
        in_df_not_metadata = df_cols_set - metadata_cols_set

        if len(in_df_not_metadata) > 0:
            message1 = "Your df contains the following cols not in the metadata: {}".format(in_df_not_metadata)
            message += message1

        in_metadata_not_in_df = metadata_cols_set - df_cols_set

        if len(in_metadata_not_in_df) > 0:
            message2 = "Metadata contains the following cols not in your df: {}".format(in_metadata_not_in_df)
            message += message2

        if len(in_df_not_metadata) + len(in_metadata_not_in_df) == 0:
            message3 = []
            message3.append("The columns in your df match those in the metadata, but they're in the wrong order:")
            message3.append("Cols in metadata: {}".format(metadata_cols))
            message3.append("Cols in your df:  {}".format(list(df.columns)))
            message3 = "\n".join(message3)
            message += message3

        raise ValueError(message)

    # Check whether each column is of the right type
    for col in metadata_cols:
        rough_heuristic_pd_column_type_check(df[col], metadata_type_lookup[col])

