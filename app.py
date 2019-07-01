# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:29:12 2019

@author: xiong
"""
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('results1.csv')

def generate_table(dataframe, max_rows=len(df)):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
   
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server
app.config['suppress_callback_exceptions']=True
markdown_text = '''
### Dash Title Here

Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''
app.layout = html.Div(children=[
    html.H1(
        children='Smart Meter: Anomaly Detector',
        style={
            'textAlign': 'left','backgroundColor':'#80ced6','font_family':'italic','font-size':'50px','text-indent': '3%'}
    ),
    html.H2('Welcome to Meter Identification System. Less Loss, More Gain.',
            style={
            'textAlign': 'center','color':'red','font-size':'30px','text-indent':'50px'}),
    html.Div([
                    
        html.Label('Input Your Meter ID'),
        dcc.Dropdown(id='box1',style={'width': '40%', 'display': 'inline-block', 'verticalAlign': "middle"},placeholder="Input Your Meter ID",
                     options=[{'label': i, 'value': i} for i in set(df.Meter_id)]),
        html.Label('OR',style={'color':'red','font-size':'15px'}),
        html.Label('Select Your Meter Size'),
        dcc.Dropdown(
            id='dropdown1',
            options=[{'label': i, 'value': i} for i in [ 1.   ,  3.   ,  0.625,  2.   ,  4.   ,  0.75 ,  1.5  ,  6.   ,
       10.   ,  8. ]],style={'width': '40%', 'display': 'inline-block', 'verticalAlign': "middle"}),
    
        html.Label('Select Your Customer Type'),
        dcc.Dropdown(
            id='dropdown2',
            options=[{'label': i, 'value': i} for i in ['CONSOLIDATED','RESIDENTIAL','MULTI-FAMILY','COMMERCIAL','BOAT DOCK','CITY','HOTEL','HOSPITAL','COLLEGE AND UNIVERSITY','SPRINKLER','POOL']],
            style={'width': '40%', 'display': 'inline-block', 'verticalAlign': "middle"})      
    ]),
        html.Label('Result:',style={'color':'red','font-size':'15px'}),
        html.Div(id='tablecontainer',style={'border-style': 'solid', 'padding': '0 20','text-indent': '5%', 'textAlign': 'center'})
    ])

 
@app.callback(
    dash.dependencies.Output('tablecontainer', 'children'),
    [dash.dependencies.Input('dropdown1', 'value'),
    dash.dependencies.Input('dropdown2', 'value'),
    dash.dependencies.Input('box1', 'value')])  


def update_table(dropdown1,dropdown2,box1):
    if box1 is not None:
        if box1 in (set(df.Meter_id)):
            dff=df[df.Meter_id==box1]
            return generate_table(dff)
        else:
            return 'Please input a right meter ID.'
    elif box1 is None:
        if dropdown1 is None and dropdown2 is None:
            return generate_table(df)
        else:
            dff = df[(df.Meter_size==dropdown1)]
            dff = dff[(dff.Cust_type_code==dropdown2)] 
            return generate_table(dff)

if __name__ == '__main__':
    app.run_server(debug=True)
