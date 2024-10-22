#author: Hana Arshid, date: 10/10/2024, topic: topic modelling of emotional experience 
import plotly.express as px
import pandas as pd
import plotly.io as pio

# Define emotional words and frequencies
topics_data = {
    'Positive Emotions': {
        "enthusiastic": 1,
        "fantastic": 1,
        "exciting": 3,
        "overwhelmed": 1,
        "fun": 1,
        "warmly": 1,
        "warm welcome": 3,
        "impressive": 1,
        "enjoyed": 1,
        "great": 1,
        "nice": 1,
        "interesting": 1,
        "richer": 1,
    },
    'Negative Emotions': {
        "cold": 1,
        "impersonal": 1,
        "claustrophobia": 1,
        "balance disorder": 1,
        "stuffy": 1,
        "awkward": 1,
    },
    'Reflective': {
        "awe for those who cannot see": 1,
        "confronting": 1,
        "in the shoes of a blind person": 1,
        "under the skin of a blind person": 1,
    }
}

# Create DataFrame
data = []
for topic, words in topics_data.items():
    for word, frequency in words.items():
        data.append({'Topic': topic, 'Word': word, 'Frequency': frequency})

df = pd.DataFrame(data)

# Total frequencies per topic
total_frequencies = df.groupby('Topic')['Frequency'].sum().reset_index()

# Define lighter colours
color_map = {
    'Positive Emotions': '#90EE90',  # green
    'Negative Emotions': '#FFB6C1',  # red
    'Reflective': '#ADD8E6'          # blue
}

# Assign colours
df['Color'] = df['Topic'].map(color_map)

# Create the sunburst chart
fig = px.sunburst(df, path=['Topic', 'Word'], values='Frequency',
                  color='Color', 
                  title='Topic Modelling of Emotional Experience',
                  hover_data={'Frequency': False})

# Update layout
fig.update_layout(
    title_font_size=18,
    title_x=0.5,
    annotations=[
        dict(
            text='2022 - September 2024',
            xref='paper', yref='paper',
            x=0.5, y=1.05,
            showarrow=False,
            font=dict(size=14, family='Times New Roman')
        )
    ],
    font=dict(family='Times New Roman'),
)

# Set text to show topic labels and frequencies
fig.update_traces(
    textinfo='label+value',  
    insidetextfont=dict(size=10, family='Times New Roman')
)

# Hover template to show frequencies on hover
fig.for_each_trace(lambda t: t.update(hovertemplate='%{label}<br>Frequency: %{value}<extra></extra>'))

# Add legend
fig.update_layout(
    legend_title_text='Emotional Topics',
    legend=dict(
        title_font=dict(size=14, family='Times New Roman'),
        font=dict(size=12, family='Times New Roman'),
        itemsizing='constant'
    )
)

# Save as an HTML file 
fig.write_html('emotional_experience_topic_modelling.html')

# Show plot
fig.show()






