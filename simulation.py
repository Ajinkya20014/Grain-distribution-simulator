import pandas as pd

def run_simulation(cg_df: pd.DataFrame, lg_df: pd.DataFrame, fps_df: pd.DataFrame):
    """
    Dummy simulation stub.
    Returns a summary sheet showing the number of rows in each uploaded dataset.

    Args:
        cg_df: DataFrame for Central Godown data
        lg_df: DataFrame for Local Godown data
        fps_df: DataFrame for Fair Price Shop data

    Returns:
        dict: One sheet named 'Summary' containing a DataFrame with counts.
    """
    summary = pd.DataFrame({
        'Dataset': ['Central Godown', 'Local Godown', 'Fair Price Shop'],
        'Row Count': [len(cg_df), len(lg_df), len(fps_df)]
    })
    return {'Summary': summary}
