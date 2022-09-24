from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.Div([
        dcc.Markdown(
            '''
            # Project 1 Cholera Outbreak
            ## Made by: Taylor Wong
            Includes: Dash v 2.6, Plot.ly, Pandas, Python 3.9
    
            *[Dataset used](https://laulima.hawaii.edu/access/content/group/MAN.XLSIDA484jl.202310/ASSIGNMENTS/Cholera.zip)*
            '''
        )
    ], style={'text-align': 'center'}),
    html.Div(
        [
            html.Div([
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"]
                )
            ], style={'display': 'center'})
            for page in dash.page_registry.values()
        ], style={'display': 'center'}
    ),
    html.Hr(),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)
