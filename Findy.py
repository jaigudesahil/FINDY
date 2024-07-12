# %% [markdown]
# <a href="https://colab.research.google.com/github/jaigudesahil/Javascript-projects/blob/main/Findy.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
import pandas as pd
import plotly.express as px
import IPython.display as dsp

# %%
dsp.Image(url='https://wallpaper.forfun.com/fetch/0b/0b269a9b0bc6b54f272ac66d2254c00d.jpeg')

# %%
df_netflix=pd.read_csv('netflix_titles.csv')


# %%
df_netflix.head()


# %%
df_netflix.shape


# %%
df_netflix.size


# %%
df_netflix.columns

# %%
df_netflix.info()

# %%


# %%
df_netflix.duplicated().sum()


# %%
df_netflix.memory_usage()

# %%
df_netflix.isna().sum()


# %%
df_netflix.dtypes.unique()


# %%
df_netflix.columns


# %%
df_netflix.select_dtypes('object').columns


# %%
df_netflix.select_dtypes('int').columns


# %%
object_columns=df_netflix.select_dtypes('object').columns
integer_columns=df_netflix.select_dtypes('int').columns
for column in df_netflix.columns:
    if column in object_columns:
        df_netflix[column]=df_netflix[column].fillna('Not Available')
    if column in integer_columns:
        df_netflix[column]=df_netflix[column].fillna(0)

# %%
df_netflix.isna().sum()


# %%
df_netflix['release_month']=df_netflix['date_added'].str.split(' ').str[0]
df_netflix['year_added']=df_netflix['date_added'].str.split(',').str[1]



# %%
df_netflix.head()

# %%
df_netflix.isna().sum()


# %%
df_netflix.dtypes.unique()


# %%
df_netflix.columns


# %%
df_netflix.select_dtypes('object').columns


# %%
df_netflix.select_dtypes('int').columns


# %%
object_columns=df_netflix.select_dtypes('object').columns
integer_columns=df_netflix.select_dtypes('int').columns
for column in df_netflix.columns:
    if column in object_columns:
        df_netflix[column]=df_netflix[column].fillna('Not Available')
    if column in integer_columns:
        df_netflix[column]=df_netflix[column].fillna(0)


# %%
df_netflix.isna().sum()


# %%
df_netflix.drop(columns=['date_added'],axis=1,inplace=True)


# %%
df_netflix.head()


# %%
df_netflix['duration'].unique()


# %%
df_netflix['duration']=df_netflix['duration'].str.replace('Seasons','Season')


# %%
df_netflix['duration'].unique()


# %%
for index,row in df_netflix.iterrows():
    if 'Jitendra Kumar' in row['cast']:
        print(row['type'],'||',row['title'],'||',row['director'],'||',row['cast'],'||',row['country'],'||',row['release_year'],'\n')

# %%
def get_actor_works(actor_name):
    # Filter the DataFrame by the actor's name (using string containment to match partial names)
    actor_works = df_netflix[df_netflix['cast'].str.contains(actor_name, na=False, case=False)]

    # Define the columns to display
    columns_to_display = ['title', 'director', 'release_year', 'rating', 'description']

    # Filter columns that exist in the DataFrame
    existing_columns = [col for col in columns_to_display if col in df_netflix.columns]

    # Display the relevant information
    return actor_works[existing_columns]

# Get actor's name from user input
actor_name = input("Enter the actor's name: ")

# Get the works of the actor
actor_works = get_actor_works(actor_name)

# Print the result
if not actor_works.empty:
    print(actor_works.to_markdown())
else:
    print(f"No works found for actor: {actor_name}")

# %%
from ipywidgets import interact, widgets
from IPython.display import display, HTML

# Function to handle actor search and display results
def search_actor(name):
    results = get_actor_works(name)
    if results.empty:
        display(HTML(f'<p>No works found for actor: <strong>{name}</strong></p>'))
    else:
        display(results)

# Create an input widget for actor's name
name_input = widgets.Text(
    placeholder='Enter actor\'s name',
    description='Actor:',
    disabled=False
)

# Display the input widget and search button
display(name_input)
interact(search_actor, name=name_input);



