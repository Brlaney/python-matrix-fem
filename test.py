import altair as alt
import pandas as pd

data = pd.DataFrame({'x': [0, 10, 20, 30],
                     'y': [0, 10, 10, 0]})

chart = alt.Chart(data).mark_circle(point=True).encode(
    alt.X('x', scale=alt.Scale(zero=True)),
    alt.Y('y', scale=alt.Scale(zero=True)),
)

chart.show()
