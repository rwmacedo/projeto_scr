# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df_tratada = pd.read_csv('df_tratada.csv')
df = pd.read_csv('df_tratada.zip', compression='zip')
df_total= pd.read_csv('df_total.csv')
df_renda= pd.read_csv('df_renda.csv')
df_ocupacao= pd.read_csv('df_ocupacao.csv')
df_regiao= pd.read_csv('df_regiao.csv')


fig1 = px.line(df_total, x="data_base", y= 'carteira_ativa', title="Carteira Ativa")
fig2 = px.line(df_total, x="data_base", y= 'carteira_inadimplida_arrastada', title="Carteira inadimplida")
fig3 = px.line(df_renda, x="data_base", y="carteira_ativa", color='renda', title="Carteira Ativa por Renda")
fig4 = px.line(df_renda, x="data_base", y="numero_de_operacoes", color='renda', title="Número de Operações por Renda")
fig5 = px.line(df_renda, x="data_base", y="ticket", color='renda', title="Ticket médio por Renda")
fig6 = px.line(df_ocupacao, x="data_base", y="carteira_ativa", color='ocupacao', title="Carteira Ativa por Ocupação")
fig7 = px.line(df_regiao, x="data_base", y="carteira_ativa", color='regiao', title="Carteira Ativa por Região")



fig11= px.line(df_renda, x="data_base", y="carteira_inadimplida_arrastada", color='renda', title="Inadimplencia por Renda")
fig12 = px.line(df_ocupacao, x="data_base", y="carteira_inadimplida_arrastada", color='ocupacao', title="Carteira Inadimplida por Ocupação")
fig13 = px.line(df_regiao, x="data_base", y="carteira_inadimplida_arrastada", color='regiao', title="Carteira Inadimplida por Região")


fig20 = px.line(df_total, x="data_base", y= 'inadimplencia', title="Carteira inadimplida")
fig21= px.line(df_renda, x="data_base", y="inadimplencia", color='renda', title="Inadimplencia por Renda (%)")
fig22 = px.line(df_ocupacao, x="data_base", y="inadimplencia", color='ocupacao', title="Carteira Inadimplida por Ocupação (%)")
fig23 = px.line(df_regiao, x="data_base", y="inadimplencia", color='regiao', title="Carteira Inadimplida por Região (%)")


app.layout = dbc.Container([
    html.H1('Credito Imobiliario', className='mt-5 mb-4 text-center'),

    html.H2('Carteira Ativa', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='carteira_ativa', figure=fig1),
            width=12
        )
    ]),
    
    html.Hr(),
     
  html.H2('Carteira Ativa por Renda', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='carteira_renda', figure=fig3),
            width=12
        )
    ]),
    
    html.Hr(),
    
     html.H2(' Número de Operações por Renda', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='operacos_renda', figure=fig4),
            width=12
        )
    ]),
    
    html.Hr(),
    
 html.H2(' Ticket Médio por Renda', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='ticket_medio_renda', figure=fig5),
            width=12
        )
    ]),
    
    html.Hr(),
          
    html.H2('Carteira Ativa por Ocupação', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='ativa_ocupacao', figure=fig6),
            width=12
        )
    ]),
    
    html.Hr(),
               
    html.H2('Carteira Ativa por Regiao', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='ativa_regiao', figure=fig7),
            width=12
        )
    ]),
    
    html.Hr(), 
     
       
    #        html.H1(children='Carteira Inadimplida', style={'text-align': 'center'}),
            
    html.H2('Carteira Inadimplida', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='carteira_inadimplida', figure=fig2),
            width=12
        )
    ]),
    
    html.Hr(), 
    
    html.H2('Carteira Inadimplida por Renda', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='inad_renda', figure=fig11),
            width=12
        )
    ]),
    
    html.Hr(),
    
     html.H2('Carteira Inadimplida por Ocupação', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='inad_ocupacao', figure=fig12),
            width=12
        )
    ]),
    
    html.Hr(),
     
     html.H2('Carteira Inadimplida por Regiao', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='inad_regiao', figure=fig13),
            width=12
        )
    ]),
    
    html.Hr(), 
    
       
     #           html.H1(children='Inadimplencia (%) ', style={'text-align': 'center'}),
    
     html.H2('Inadimplencia(%)', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='inadimplencia', figure=fig20),
            width=12
        )
    ]),
    
    html.Hr(), 

        
     html.H2('Carteira Inadimplida por Renda (%)', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='inad_renda_p', figure=fig21),
            width=12
        )
    ]),
    
    html.Hr(), 
        
    html.H2('Carteira Inadimplida por Ocupação (%)', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='inad_ocupacao_p', figure=fig22),
            width=12
        )
    ]),
    
    html.Hr(), 
          
    
     html.H2('Carteira Inadimplida por Regiao (%)', className='mb-3 text-center'),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='inad_regiao_p', figure=fig23),
            width=12
        )
    ]),
    
    html.Hr(),  
    

     
     
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
