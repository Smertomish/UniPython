import plotly.express as px
import pandas as pd

trees = pd.read_csv('trees.csv')

# Построение тепловой карты
fig = px.density_heatmap(trees, x="Girth", y="Height", z="Volume", histfunc="sum", nbinsx=20, nbinsy=20)

# Настройка осей и меток
fig.update_layout(
    xaxis_title="Обхват ствола, дюймы",
    yaxis_title="Высота, футы",
    coloraxis_colorbar_title="Объем, футы^3"
)

# Отображение графика
fig.show()