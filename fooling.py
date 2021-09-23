import numpy
import pandas as pd
import numpy as np
original_path = './results/results1/process_list_autogen.csv'
new_path = './results/results1/reformatted(1).csv'


def reformat_csv(og_path, new_path):
    """Reformats process_list_autogen.csv into a new csv
    Column names: case_id, slide_id, label

    """
    df = pd.read_csv(og_path)
    slide_names = df.loc[:, 'slide_id']  # gets the column of interest
    df_new = pd.DataFrame({
        "case_id": np.empty(len(slide_names), dtype=numpy.str, order='C'),
        "slide_id": np.empty(len(slide_names), dtype=numpy.str, order='C'),
        "label": np.empty(len(slide_names), dtype=numpy.str, order='C')
    })

    # reformat file names
    for i in range(len(slide_names)):
        name = slide_names[i]
        name = name.lower()
        name = name.split('.')[0]
        slide_num = int(name.split('_')[1])

        df_new["case_id"][i] = slide_num
        df_new["slide_id"][i] = name
        df_new["label"][i] = 'normal_tissue' if slide_num < 50 else 'tumor_tissue'

    # save csv
    df_new.to_csv(new_path)


reformat_csv(original_path, new_path)
