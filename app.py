import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.analysis import (
    dataset_summary,
    missing_data,
    numerical_columns,
    categorical_columns
)

from utils.charts import (
    missing_chart,
    histogram,
    boxplot,
    correlation_heatmap,
    scatter_plot,
    category_chart
)

st.set_page_config(
    page_title="Advanced Data Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Advanced Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.header("Dataset Preview")

    st.dataframe(df.head())

    summary = dataset_summary(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", summary["Rows"])
    col2.metric("Columns", summary["Columns"])
    col3.metric("Duplicates", summary["Duplicate Rows"])
    col4.metric("Missing", summary["Missing Values"])

    st.divider()

    st.header("Data Types")

    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Datatype": df.dtypes.astype(str)
    })

    st.dataframe(dtype_df)

    st.divider()

    st.header("Missing Value Analysis")

    missing_df = missing_data(df)

    st.dataframe(missing_df)

    st.plotly_chart(
        missing_chart(missing_df),
        use_container_width=True
    )

    st.divider()

    numeric_cols = numerical_columns(df)

    if len(numeric_cols) > 0:

        st.header("Statistical Summary")

        st.dataframe(
            df[numeric_cols].describe()
        )

        st.divider()

        st.header("Correlation Analysis")

        st.plotly_chart(
            correlation_heatmap(
                df[numeric_cols]
            ),
            use_container_width=True
        )

        st.divider()

        st.header("Numerical Analysis")

        selected_num = st.selectbox(
            "Select Numerical Column",
            numeric_cols
        )

        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(
                histogram(df, selected_num),
                use_container_width=True
            )

        with col2:
            st.plotly_chart(
                boxplot(df, selected_num),
                use_container_width=True
            )

        if len(numeric_cols) >= 2:

            st.divider()

            st.header("Relationship Analysis")

            x_col = st.selectbox(
                "X Axis",
                numeric_cols,
                key="x"
            )

            y_col = st.selectbox(
                "Y Axis",
                numeric_cols,
                key="y"
            )

            st.plotly_chart(
                scatter_plot(
                    df,
                    x_col,
                    y_col
                ),
                use_container_width=True
            )

    cat_cols = categorical_columns(df)

    if len(cat_cols) > 0:

        st.divider()

        st.header("Categorical Analysis")

        selected_cat = st.selectbox(
            "Select Category",
            cat_cols
        )

        st.plotly_chart(
            category_chart(
                df,
                selected_cat
            ),
            use_container_width=True
        )

    st.divider()

    st.header("Raw Dataset")

    st.dataframe(df)

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Dataset",
        data=csv,
        file_name="processed_data.csv",
        mime="text/csv"
    )

else:

    st.info("Upload a dataset to begin analysis.")
