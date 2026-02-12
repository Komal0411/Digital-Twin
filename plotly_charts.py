import plotly.express as px

def build_forecast_chart(df, x, y, title):
    fig = px.scatter(
        df, x=x, y=y,
        size=y, color=y,
        color_continuous_scale="Turbo",
        title=title
    )
    fig.update_layout(
        template="plotly_dark",
        height=500,
        title_x=0.5
    )
    return fig
