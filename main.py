import pandas as pd

# Things we could add:
#   -Data showing total births for a year, to accurately determine which name was most popular


def main():
    # Read in dataframe from Excel document
    df = pd.read_excel('Baby Names Dataset.xlsx')

    # Rename columns
    df.columns = ['year_of_birth', 'name', 'sex', 'count']

    # Add column containing number of letters in name
    df['letter_count'] = df['name'].apply(lambda x: len(x))

    print(df)


def most_popular_name(df):
    pass
    # Male name listed the most times

    # Female name listed the most times

    # Male name with highest count

    # Female name with highest count


main()
