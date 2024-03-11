# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.



from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_html_components as html

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
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


app.layout = html.Div(children=[
    html.H1(children='Credito Imobiliario'),
        html.H2(children='Carteira Ativa', style={'text-align': 'center'}),

    html.Div(children='''
        Carteira Ativa
    '''),

    dcc.Graph(
        id='carteira_ativa',
        figure=fig1
    ),        
   
     
    html.Div(children='''
        Carteira Ativa por Renda
    '''),
    
    dcc.Graph(
        id='carteira_renda',
        figure=fig3
    ),
     
    html.Div(children='''
        Número de Operações por Renda
    '''),
    
    dcc.Graph(
        id='operacos_renda',
        figure=fig4
    ),
     
          
    html.Div(children='''
        Ticket Médio por Renda
    '''),
    
    dcc.Graph(
        id='ticket_medio_renda',
        figure=fig5
    ),
     
               
    html.Div(children='''
        Carteira Ativa por Ocupação
    '''),
    
    dcc.Graph(
        id='ativa_ocupacao',
        figure=fig6
    ),
     
    html.Div(children='''
        Carteira Ativa por Regiao
    '''),
    
    dcc.Graph(
        id='ativa_regiao',
        figure=fig7
    ),
    
            html.H2(children='Carteira Inadimplida', style={'text-align': 'center'}),
            
  html.Div(children='''
        Carteira Inadimplida
    '''),
    
    dcc.Graph(
        id='carteira_inadimplida',
        figure=fig2
    ),
    
    html.Div(children='''
        Carteira Inadimplida por Renda
    '''),
    
    dcc.Graph(
        id='inad_renda',
        figure=fig11
    ),    
    
    html.Div(children='''
        Carteira Inadimplida por Ocupação
    '''),
    
    dcc.Graph(
        id='inad_ocupacao',
        figure=fig12
    ),    
    
    html.Div(children='''
        Carteira Inadimplida por Regiao
    '''),
    
    dcc.Graph(
        id='inad_regiao',
        figure=fig13
    ),   
    
                html.H2(children='Inadimplencia (%) ', style={'text-align': 'center'}),
    
    html.Div(children='''
        Inadimplencia(%)
    '''),
     
    dcc.Graph(
        id='inadimplencia',
        figure=fig20
    ),    
        
    
    html.Div(children='''
        Carteira Inadimplida por Renda (%)
    '''),
     
    dcc.Graph(
        id='inad_renda_p',
        figure=fig21
    ),    
    
    html.Div(children='''
        Carteira Inadimplida por Ocupação (%)
    '''),
    
    dcc.Graph(
        id='inad_ocupacao_p',
        figure=fig22
    ),    
    
    html.Div(children='''
        Carteira Inadimplida por Regiao (%)
    '''),
    
    dcc.Graph(
        id='inad_regiao_p',
        figure=fig23
    )   
     
     
])

if __name__ == '__main__':
    app.run(debug=True)
    
    with open("index.html", "w") as file:
        file.write(app())

