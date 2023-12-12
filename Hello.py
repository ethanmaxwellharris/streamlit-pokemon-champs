# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn

LOGGER = get_logger(__name__)


def run():
    st.set_page_config( 
        page_title="Pokemon C.H.A.M.P.S.",
        page_icon="🏆",
    )

    st.write("# Are you ready to ***Win Them All*** 👑")

    st.sidebar.header('Select an Option')
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        The Pokemon Tournament Training Club has began it's 2024 Season Training! This upcoming season is going to be very different however. We have been hard at work creating the ultimate application that helps create winning decks. This year we are unveiling the **Pokemon Card-based Helper for Assessing Match Performance System**! We like to call it **Pokemon CHAMPS** around the office though.

        This revolutionary application will take the input of user cards and outputs the potential success rating for the user. The application will also output potential add-on's to your deck to add more flavor and achieve tournament dominance!

        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


# Data Prep
data_file = 'data/tournaments.csv'
df = pd.read_csv(data_file)

# Streamlit App
st.title('Pokemon Tournaments Analysis')

# Visualization #1: Display the top 10 cards by occurrences
st.header('Top 10 Cards in Winning Decks')
card_occurrences = df['name_card'].value_counts()
top_cards = card_occurrences.head(10)
st.bar_chart(top_cards)

# Visualization #2: Correlation Heatmap
st.header('Correlation Heatmap of Numerical Variables')
numerical_columns = df[['amount_card', 'price_card', 'all_time_score', 'ranking_player_tournament']]
correlation_matrix = numerical_columns.corr()
st.pyplot(sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5).figure)

# Visualization #3: Count the number of tournaments in each country
st.header('Number of Tournaments in Each Country')
region_counts = df['country_tournament'].value_counts(dropna=False)
st.bar_chart(region_counts)

# Visualization #4: Average cost of cards by country
st.header('Average Cost of a Deck per Country')
df['price_card'] = pd.to_numeric(df['price_card'], errors='coerce')
average_cost_per_country = df.groupby('country_tournament')['price_card'].mean().reset_index()
st.bar_chart(average_cost_per_country.set_index('country_tournament'))

# Train a RandomForestClassifier
st.header('Train a RandomForestClassifier for Card Success Prediction')

# Define success criteria
card_occurrences = df['name_card'].value_counts().reset_index()
card_occurrences.columns = ['name_card', 'appearances_in_winning_decks']
success_threshold = card_occurrences['appearances_in_winning_decks'].quantile(0.9)

# Create a binary target variable
card_occurrences['success'] = card_occurrences['appearances_in_winning_decks'] >= success_threshold

# Merge success information back to the original DataFrame
df = pd.merge(df, card_occurrences[['name_card', 'success']], on='name_card', how='left')

# Select features
X = df[['name_card']]

# Encode categorical features
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X[['name_card']])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, df['success'], test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
classification_result = classification_report(y_test, y_pred)

# Display classification report
st.subheader('Model Evaluation (RandomForestClassifier)')
st.text(classification_result)

# Predict success for a new card
st.header('Predict Card Success')
new_card_name = st.text_input('Enter a card name:')
new_card_encoded = encoder.transform([[new_card_name]])
prediction = model.predict(new_card_encoded)

# Display prediction
st.write(f'The predicted success for card "{new_card_name}" is: {prediction[0]}')

# Additional Checks
st.subheader('Additional Checks')
st.text(df['success'].value_counts())
st.text(df['name_card'].value_counts())

if __name__ == "__main__":
    run()