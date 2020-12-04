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

    most_popular_name(df)
    
    sustained_names_by_cent(df)


def most_popular_name(df):
    # Dataframe showing which names have appeared on the list the most times
    name_appearances_df = df.groupby(['name', 'sex'])['count'].count().to_frame()
    name_appearances_df = name_appearances_df.reset_index()
    name_appearances_df = name_appearances_df.sort_values(by=['count', 'name'], ascending=False)
    print(name_appearances_df.head(160))

    # Male name listed the most times

    # Female name listed the most times

    # Male name with highest count

    # Female name with highest count
    
def sustained_names_by_cent(df):
  cent_df = df.groupby("Century")["name"].value_counts().to_frame(name = "count")
  cent_df = cent_df.reset_index()
  
  
  top10_19th_df = cent_df[:10]
  x = [0,1,2,3,4,5,6,7,8,9]
  labels = top10_19th_df["name"]
  plt.figure()
  top10_19th_df.plot(kind = "bar")
  plt.title("Most Popular Names in the 19th Century")
  plt.xticks(x, labels, rotation = 90) 
  plt.xlabel("Name")
  plt.ylabel("Count of years over 100")
  
  top10_20th_df = cent_df[527:537]
  x = [0,1,2,3,4,5,6,7,8,9]
  labels = top10_20th_df["name"]
  plt.figure()
  top10_20th_df.plot(kind = "bar")
  plt.title("Most Popular Names in the 20th Century")
  plt.xticks(x, labels, rotation = 90) 
  plt.xlabel("Name")
  plt.ylabel("Count of years over 100")
  
  
  top10_21st_df = cent_df[5633:5643]
  x = [0,1,2,3,4,5,6,7,8,9]
  labels = top10_21st_df["name"]
  plt.figure()
  top10_21st_df.plot(kind = "bar")
  plt.title("Most Popular Names in the 21st Century")
  plt.xticks(x, labels, rotation = 90) 
  plt.xlabel("Name")
  plt.ylabel("Count of years over 100")

  print(top10_19th_df)
  print(top10_20th_df)
  print(top10_21st_df)

  return

main()
