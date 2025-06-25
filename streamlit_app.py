import streamlit as st
from streamlit_extras.stylable_container import stylable_container


primary_background = '#111111'
secondary_background = '#171717'
dark_text_color = '#171717'
light_text_color = '#E8E8E8'
color_1 = '#fc4778' #Pink
color_2 = '#3952f5' #Purple
border_color = '#3c3c3c'
caption_color = '#878884'

def tile(key, height, border):
    border_style = f"1px solid {border_color};" if border else "none;"
    
    with stylable_container(
        key=key,
        css_styles=f'''
        {{
            background-color: {secondary_background};
            font-family: "Source Sans Pro", sans-serif;
            font-weight: 400;
            border-radius: 0.5rem;
            border: {border_style};
            padding: calc(1em - 1px);
            color: {light_text_color};
        }}
        '''
    ):
        return st.container(border=False, height=height)
    
st.header("Metrics", anchor=False)

options = ["All", "YTD", "Quarter", "Month"]
selection = st.segmented_control(
    "Timeframe", options, selection_mode="single", label_visibility='visible'
)

balance, profit, deposits, withdrawals = st.columns(4, border=False)

with balance:
    tile("balance_tile", 100, True)

with profit:
    tile("profit_tile", 100, True)

with deposits:
    tile("deposits_tile", 100, True)

with withdrawals:
    tile("withdrawals_tile", 100, True)


tile("chart_tile", 350, True)


