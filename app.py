# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:29:12 2019

@author: xiong
"""


import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

df = pd.read_csv(results1.csv')

def generate_table(dataframe):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
   
app = dash.Dash()
server=app.server

app.layout = html.Div([
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
        dcc.Input(id='box1',type='number',style={'width': '16%', 'display': 'inline-block', 'verticalAlign': "middle"}),
        html.Label('OR',style={'color':'red','font-size':'15px'}),
        html.Label('Select Your Meter Size'),
        dcc.Dropdown(
            id='dropdown1',
            options=[{'label': i, 'value': i} for i in [ 1.   ,  3.   ,  0.625,  2.   ,  4.   ,  0.75 ,  1.5  ,  6.   ,
       10.   ,  8. ]],style={'width': '40%', 'display': 'inline-block', 'verticalAlign': "middle"}),
    
        html.Label('Select Your Customer Type'),
        dcc.Dropdown(
            id='dropdown2',
            options=[{'label': i, 'value': i} for i in [ 1.,  3.,  2.,  5.,  4., 13., -1.,  8.,  9., 12.,  7.]],
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
        dff=df[df.Meter_id==box1]
        return generate_table(dff)
    elif box1 is None:
        if dropdown1 is None and dropdown2 is None:
            return 'Please input a right meter ID.'
        else:
            dff = df[(df.Meter_size==dropdown1)]
            dff = dff[(dff.Cust_type_code==dropdown2)] 
            return generate_table(dff)

  
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

   

if __name__ == '__main__':
    app.run_server(debug=True)
