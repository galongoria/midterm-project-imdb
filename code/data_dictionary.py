import pandas as pd
import os


IN_PATH = os.path.join("data", "clean", "imdb_clean.csv")
OUTPUT_PATH = os.path.join("data", "clean", "data_dictionary.csv")

def make_data_dictionary(in_path):
    '''Creates an initial data dictionary'''
        
    df = pd.read_csv(in_path)
    cols = df.columns
    
    DataDict = {}
    
    for col in cols:
        DataDict[col] = {
            "Data Type": str(df.dtypes[col]),
            "Example Values": df[col].unique().tolist()[:4]
        }
    df_DataDict = pd.DataFrame(DataDict).transpose()
    
    return df_DataDict

def give_data_description(df_data_dict, out_path):
    '''Adds column definitions to the data frame and creates a csv '''
    
    definition_list = [
        "Title of the movie",
       "Year the movie was released",
       "Motion Picture Association rating of the movie",
       "Length of the movie in minutes",
       "Movie category based on narrative elements",
       "A brief description of the movie plot",
       "IMDB rating of the movie (1 to 10)",
       "Metascore of the movie assigned by movie critics (0 to 100)",
       "The number of votes cast by IMDB users for the movie",
       "Gross revenue of the movie in millions of dollars"
    ]
    
    
    df_data_dict.insert(0, "Definition", definition_list)
    df_data_dict.to_csv(out_path)
    
    
if __name__ == "__main__":
    
    df_DataDict = make_data_dictionary(IN_PATH)
    give_data_description(df_DataDict, OUTPUT_PATH)
    

