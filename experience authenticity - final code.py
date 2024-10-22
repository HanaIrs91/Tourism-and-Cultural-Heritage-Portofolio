#author: Hana Arshid, date: 10/10/2024, topic: words associated with experience  
import pandas as pd
import plotly.express as px

# Frequencies of the words
synonym_frequencies = {
    'special': 12,
    'unique': 3,
    'fantastic': 2,
    'wonderful': 2,
    'impressive': 5,
}

# Prepare the data for visualisation
filtered_synonym_frequencies = {word: freq for word, freq in synonym_frequencies.items() if freq > 0}

# Create a DataFrame for the filtered data
df_synonym_frequencies = pd.DataFrame(list(filtered_synonym_frequencies.items()), columns=['Word', 'Frequency'])

# Sort the DataFrame by frequency in descending order
df_synonym_frequencies = df_synonym_frequencies.sort_values(by='Frequency', ascending=False)

# Create a bar chart for the synonym frequencies 
fig_synonym_frequencies = px.bar(
    df_synonym_frequencies,
    x='Word',
    y='Frequency',
    title='Words Associated with Experience (2022 - September 2024)',
    labels={'Word': 'Words', 'Frequency': 'Frequency'},
    text='Frequency'
)

# Layout
fig_synonym_frequencies.update_layout(
    width=800,  # Set a larger width
    height=600,  # Set a larger height
    title_font_size=18,
    title_x=0.5,
    font=dict(family='Times New Roman'),
)

# Show the plot
fig_synonym_frequencies.show()

# Save the visualisation as an HTML file 
fig_synonym_frequencies.write_html('words_associated_with_experience_sorted_2022_2024.html')
