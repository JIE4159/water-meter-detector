# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:29:12 2019

@author: xiong
"""


import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

server=app.server
   
app = dash.Dash()

app.layout = html.Div([
    html.H1(
        children='Welcome to Meter Identification System',
        style={
            'textAlign': 'center','backgroundColor':'green'}
    )
]) 

  
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

   

if __name__ == '__main__':
    app.run_server(debug=True)
