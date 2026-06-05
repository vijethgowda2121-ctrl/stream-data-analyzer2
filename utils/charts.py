import plotly.express as px
import plotly.graph_objects as go


def missing_chart(df_missing):

    fig = px.bar(
        df_missing,
        x="Column",
        y="Percent",
        color="Percent",
        title="Missing Values (%)"
    )

    return fig


def histogram(df, column):

    fig = px.histogram(
        df,
        x=column,
        nbins=30,
        title=f"Distribution of {column}"
    )

    return fig


def boxplot(df, column):

    fig = px.box(
        df,
        y=column,
        title=f"Box Plot - {column}"
    )

    return fig


def correlation_heatmap(df):

    corr = df.corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    return fig


def scatter_plot(df, x, y):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        trendline="ols",
        title=f"{x} vs {y}"
    )

    return fig


def category_chart(df, column):

    counts = (
        df[column]
        .astype(str)
        .value_counts()
        .head(20)
        .reset_index()
    )

    counts.columns = ["Category", "Count"]

    fig = px.bar(
        counts,
        x="Category",
        y="Count",
        color="Count",
        title=f"{column} Distribution"
    )

    return fig
