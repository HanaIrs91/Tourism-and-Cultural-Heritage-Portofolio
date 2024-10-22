#author: Hana Arshid, date: 10/10/2024, topic: topic modelling of cognitive experience 
import pandas as pd
import plotly.express as px
from collections import Counter
import re

# Provided text
text = """
An 'eye-opener', awareness moment, an eye opener, you can't imagine what it's like to be visually impaired/blind, Respect for the tour guides, patience and humour, your other senses are constantly on edge, The experience was very impressive and you will experience it together with a friendly tour guide, Respect for the way we were shown around. Never seen so much in the dark, other senses are constantly on edge, The experience was very impressive, a friendly tour guide, Respect for the way we were shown around. Never seen so much in the dark, of interactive things, but also educational facts, it was of course in pitch dark and with a walking stick, respect for blind or partially sighted people, even more respect for the blind and partially sighted to participate in our society, Thanks to the supervisors for their openness and explanation!, very engaging in sharing their experiences and also had great senses of humour, very special experience. Very friendly staff, clear explanations, a clear explanation and introduction, A fantastic experience, A unique experience, You become much more aware of things that are completely normal (for us) and that do not apply to these people, great guidance, A wonderful experience, to create awareness. Well organised in different languages, interesting to experience, accomplished by an expert guide, Special experience!, get an introduction and stick lesson. Then you step into the pitch black, The experience is really interesting, The guides are amazingly kind and shared information and experiences with us and made us feel more aware of their situation, helps creating a sense of community and the urge to understand, accept and help each other, Really an awareness and great opportunity. Fine people and good Guide Tatjana, good explanation and a real open attitude!!, Very special to experience, Good explanation by a visually impaired person, Very special experience, absolutely recommended. Guide Jack provided a brilliant 'city trip' based on sound and feeling and was open about his own life as a partially sighted person, Very special experience. The tour in the dark with the Guide was pleasant and very personal, We were well guided by Guide, We thought it was a very special experience, What a special experience, but our guides Marco and Sander were calm and clear, Good to become aware of how blind and visually impaired people, Then 10 minutes of audio; The Guide was very kind and patient, The collection and exhibition is educational and fun, “An experience of a special kind,” The tour guide who introduces you to the world of darkness is visually impaired. A very open person who you can ask anything., After the tour you see the world through different eyes, you focus more on your other senses and are fascinated and amazed how well visually impaired people can master everyday life, This was an interesting experience, also a fun and educational experience, A great, accessible, safe and also entertaining introduction to a world in which 'seeing' is no longer a given. What a pleasant guides, how nice that there was so much 'light' in their stories, "One of the most unique and educational experiences that we've ever had, What an experience and an impressive experience! Great Guide, After the dark experience, the chocolate tasting we all agreed: It was an interesting, special experience, the guides were reassuring, supportive, Absolutely eye-opening tour in complete darkness. Special thanks to our awesome guide, Great to experience, seeing everything is 'normal but not obvious to everyone'. It's an eye opener, It was a very interesting experience, It's a mega experience, Absolutely a fantastic and special experience, something unique, The experience is very diverse and interesting, wonderful experience, instructive & pleasant Guide. Special to experience in real-life what it must be like when your vision is reduced. From now on, you won't just put your bike in the middle of the pavement. spontaneous employees on the do-plein who are very open about their eye condition, therefore very accessible, an experience we will not soon forget, were able to experience what it is like to be blind and to rely completely on your other senses. We were very impressed, What an impressive experience. 

Very impressive to feel and experience what daily life looks like for a visually impaired or blind person. 

The chocolate tasting was also a beautiful experience. We used our other senses at the tasting and were therefore more aware of the flavours.

We had 2 nice guides during the experiences. Nice explanation with here and there a trip to a joke or joke.
"""

# Clean and split the text into words
words = re.findall(r'\w+', text.lower())  

# Create a Counter to hold the frequencies of all words
word_counts = Counter(words)

# Define updated topics and keywords with clusters
clusters = {
    'Awareness': ['eye opener', 'aware', 'awareness', 'respect', 'eye-opener'],
    'Guidance & Learning': ['guide', 'guides', 'friendly', 'clear', 'expert', 'supervisor', 
                            'explanation', 'support', 'assistance', 'educational', 
                            'interesting', 'learn', 'informative', 'understanding', 
                            'engaging', 'inclusive', 'open', 'activity'],
    'Sensory Engagement': ['senses', 'dark', 'chocolate', 'taste', 'touch', 'hear', 
                          'flavours', 'sound', 'light', 'tasting'],
    'Entertainment': ['fun', 'enjoy', 'joke', 'entertaining']  
}

# Prepare detailed data with every individual word that has a non-zero frequency
filtered_data = []

# Count frequencies for each keyword and add to filtered_data if frequency > 0
for topic, keywords in clusters.items():
    for keyword in keywords:
        keyword_frequency = word_counts[keyword]
        if keyword_frequency > 0:
            filtered_data.append({'Topic': topic, 'Most Common Word': keyword, 'Frequency': keyword_frequency})

# Create a DataFrame for detailed visualisation without zero frequency keywords
df_filtered_cognitive = pd.DataFrame(filtered_data)

# Add frequency for 'eye-opener' explicitly
eye_opener_frequency = 4
df_filtered_cognitive = pd.concat([df_filtered_cognitive, pd.DataFrame([{'Topic': 'Awareness', 'Most Common Word': 'eye-opener', 'Frequency': eye_opener_frequency}])], ignore_index=True)

# Sort the DataFrame within each topic from most to least frequent
df_filtered_cognitive.sort_values(by=['Topic', 'Frequency'], ascending=[True, False], inplace=True)

# Count the number of associated words for each topic
topic_word_count = df_filtered_cognitive.groupby('Topic')['Frequency'].sum().reset_index()
topic_word_count.sort_values(by='Frequency', ascending=False, inplace=True)

# Order topics from most to least based on total frequency
sorted_filtered_data = []
for _, row in topic_word_count.iterrows():
    topic = row['Topic']
    topic_data = df_filtered_cognitive[df_filtered_cognitive['Topic'] == topic]
    sorted_filtered_data.extend(topic_data.to_dict('records'))

# Create a DataFrame for sorted detailed visualisation
df_sorted_filtered_cognitive = pd.DataFrame(sorted_filtered_data)

# Create a bar chart for the sorted filtered frequencies
fig_sorted_cognitive_filtered = px.bar(
    df_sorted_filtered_cognitive,
    x='Most Common Word',
    y='Frequency',
    color='Topic',
    title='Topic Modelling of Cognitive Experience (2022 - September 2024)',
    labels={'Most Common Word': 'Words', 'Frequency': 'Frequency'},
    text='Frequency'
)

# layout 
fig_sorted_cognitive_filtered.update_layout(
    width=1200,  # Set a larger width
    height=800,  # Set a larger height
    title_font_size=18,
    title_x=0.5,
    font=dict(family='Times New Roman'),
)

# Show the plot
fig_sorted_cognitive_filtered.show()

# Save the sorted visualisation as an HTML file 
fig_sorted_cognitive_filtered.write_html('topic_modelling_cognitive_experience_2022_2024.html')
