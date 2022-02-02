'''
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame(dict(
    x = [0, 10, 20, 30],
    y = [0, 10, 10, 0]
))
fig = px.line(df, x="x", y="y", title="Unsorted Input")
fig.show()

df = df.sort_values(by="x")
fig = px.line(df, x="x", y="y", title="Sorted Input")
fig.show()

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[0, 10, 20, 30, 10, 0, 20],
    y=[0, 10, 10, 0, 10, 0, 10],
    mode='lines',
    name='lines'))
fig.add_trace(go.Scatter(
    x=[0, 10, 20, 30],
    y=[0, 10, 10, 0],
    mode='markers',
    name='markers'))

fig.show()
'''

import altair as alt
# from vega_datasets import data
import pandas as pd

data = pd.DataFrame({'x': [0, 10, 20, 30],
                     'y': [0, 10, 10, 0]})

chart = alt.Chart(data).mark_line(point=True).encode(
    alt.X('x', scale=alt.Scale(zero=True)),
    alt.Y('y', scale=alt.Scale(zero=True)),
)

chart.show()
