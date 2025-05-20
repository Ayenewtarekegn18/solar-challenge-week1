import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


def load_data(country: str) -> pd.DataFrame:
    """
    Load and clean data for the specified country.

    Args:
        country (str): Country name (Benin, SierraLeone, or Togo)

    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    # Map country names to file paths
    file_map = {
        "Benin": "data/benin-malanville.csv",
        "SierraLeone": "data/sierraleone-bumbuna.csv",
        "Togo": "data/togo-dapaong_qc.csv"
    }

    if country not in file_map:
        raise ValueError(f"Unknown country: {country}")

    file_path = file_map[country]

    # Check if file exists
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    try:
        # Load the data
        df = pd.read_csv(file_path)

        if df.empty:
            raise ValueError(f"Empty dataset loaded for {country}")

        # Add country column
        df['Country'] = country

        # Convert timestamp to datetime if it exists
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])

        return df

    except Exception as e:
        raise Exception(f"Error processing data for {country}: {str(e)}")


def get_summary_stats(df: pd.DataFrame, metrics: list) -> pd.DataFrame:
    """
    Calculate summary statistics for specified metrics.

    Args:
        df (pd.DataFrame): Input dataframe
        metrics (list): List of metric columns to analyze

    Returns:
        pd.DataFrame: Summary statistics
    """
    stats = []
    for metric in metrics:
        if metric in df.columns:
            metric_stats = df.groupby('Country')[metric].agg([
                'mean', 'std', 'min', 'max'
            ]).round(2)
            stats.append(metric_stats)

    return pd.concat(stats, axis=1) if stats else pd.DataFrame()


def create_boxplot(df: pd.DataFrame, metric: str) -> go.Figure:
    """
    Create a boxplot for the specified metric.

    Args:
        df (pd.DataFrame): Input dataframe
        metric (str): Metric to plot

    Returns:
        go.Figure: Boxplot figure
    """
    fig = px.box(
        df,
        x='Country',
        y=metric,
        title=f"{metric} Distribution by Country",
        points='outliers'
    )
    fig.update_layout(
        yaxis_title=f"{metric} (W/m²)",
        showlegend=False
    )
    return fig


def create_time_series(df: pd.DataFrame, metric: str) -> go.Figure:
    """
    Create a time series plot for the specified metric.

    Args:
        df (pd.DataFrame): Input dataframe
        metric (str): Metric to plot

    Returns:
        go.Figure: Time series figure
    """
    if 'timestamp' not in df.columns:
        return go.Figure()

    fig = px.line(
        df,
        x='timestamp',
        y=metric,
        color='Country',
        title=f"{metric} Over Time"
    )
    fig.update_layout(
        yaxis_title=f"{metric} (W/m²)",
        xaxis_title="Time"
    )
    return fig


def get_top_regions(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    """
    Get top regions by average metric value.

    Args:
        df (pd.DataFrame): Input dataframe
        metric (str): Metric to analyze

    Returns:
        pd.DataFrame: Top regions table
    """
    if 'Region' not in df.columns:
        return pd.DataFrame()

    top_regions = df.groupby(['Country', 'Region'])[
        metric].mean().reset_index()
    top_regions = top_regions.sort_values(metric, ascending=False).head(10)
    top_regions[metric] = top_regions[metric].round(2)
    return top_regions


def calculate_correlation(df: pd.DataFrame, metrics: list) -> pd.DataFrame:
    """
    Calculate correlation matrix for specified metrics.

    Args:
        df (pd.DataFrame): Input dataframe
        metrics (list): List of metrics to correlate

    Returns:
        pd.DataFrame: Correlation matrix
    """
    available_metrics = [m for m in metrics if m in df.columns]
    if len(available_metrics) < 2:
        return pd.DataFrame()

    corr_matrix = df[available_metrics].corr().round(2)
    return corr_matrix


def get_metric_description(metric: str) -> str:
    """
    Get description for the specified metric.

    Args:
        metric (str): Metric name

    Returns:
        str: Metric description
    """
    descriptions = {
        "GHI": "Global Horizontal Irradiance - Total solar radiation received on a horizontal surface",
        "DNI": "Direct Normal Irradiance - Solar radiation received directly from the sun",
        "DHI": "Diffuse Horizontal Irradiance - Solar radiation scattered by the atmosphere"
    }
    return descriptions.get(metric, "No description available.")
