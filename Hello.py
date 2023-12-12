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
import altair as alt
import base64
import numpy
import pydeck

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

    st.header('Enter a card')

    card_input = "Lugia"

    card = st.text_area("Card:", card_input, height=50)
    card = card.splitlines()
    card = '\n'.join(card) #Concatonates list to string

    st.write("""
             ***
             """)
    
    st.header('Input: ')
    card

    st.header('Output: ')




if __name__ == "__main__":
    run()
