import pandas as pd
import plotly.graph_objects as go

def initialize_heatmap_dict():
    """Initializes a dictionary for heatmap data accumulation."""
    return {
        day: {str(hour): 0 for hour in range(24)}
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    }

def parse_timestamps_to_heatmap(df, timestamp_column):
    """Parses DataFrame timestamps into a structured heatmap dictionary."""
    DoW_hours = initialize_heatmap_dict()
    df[timestamp_column] = pd.to_datetime(df[timestamp_column], errors='coerce')
    df = df.dropna(subset=[timestamp_column])
    
    for idx, gp in df.groupby(df[timestamp_column].dt.dayofweek):
        day_name = gp[timestamp_column].dt.day_name().iloc[0]
        hour_block = gp.groupby(gp[timestamp_column].dt.hour).size()
        for hour, count in hour_block.items():
            DoW_hours[day_name][str(hour)] = count
    return pd.DataFrame.from_dict(DoW_hours)

def calculate_time_with_offset(hour, offset):
    """Adjusts hour by the UTC offset and formats it into 12-hour AM/PM string."""
    utc_hour = (hour + offset + 24) % 24
    am_pm = "AM" if 0 <= utc_hour < 12 else "PM"
    utc_hour = utc_hour % 12 if utc_hour != 0 else 12
    return f'{utc_hour} {am_pm}'

def setup_plot(heatmap_df, title, user_utc_offset):
    """Sets up the Plotly heatmap plot with dual y-axes."""
    y2_data = [calculate_time_with_offset(hour, user_utc_offset) for hour in range(0, 24, 2)]

    fig = go.Figure()
    heatmap_trace = go.Heatmap(
        z=heatmap_df.values,
        x=heatmap_df.columns,
        y=[i for i in range(24)],
        colorscale='Inferno',
        colorbar=dict(x=1.15)
    )

    scatter_trace = go.Scatter(
        x=y2_data,
        y=heatmap_df.index,
        mode='markers',
        marker=dict(size=0),
        showlegend=False,
        yaxis='y2'
    )

    fig.add_trace(heatmap_trace)
    fig.add_trace(scatter_trace)
    fig.update_traces(visible=False, selector=dict(yaxis='y2'))

    fig_title = 'Heatmap of ' + title
    fig.update_layout(
        title=fig_title,
        xaxis_title='Day of the Week',
        yaxis=dict(
            title='Hour of the Day (UTC)',
            domain=[0, 1],
            range=[-0.5, 23.5],
            tickmode='array',
            tickvals=[i for i in range(0, 24, 2)],
            ticktext=[f'{i:02}:00' for i in range(0, 24, 2)],
        ),
        yaxis2=dict(
            title=f'Time of Day (UTC {user_utc_offset:+})',
            domain=[0, 1],
            range=[-0.5, 23.5],
            overlaying='y',
            side='right',
            tickmode='array',
            tickvals=[i for i in range(0, 24, 2)],
            ticktext=[calculate_time_with_offset(hour, user_utc_offset) for hour in range(0, 24, 2)],
            showgrid=False,
            zeroline=False
        ),
    )
    return fig

def heatmap_from_excel(file_path, sheet_name, timestamp_column, title, user_utc_offset=0):
    """Generates a heatmap from an Excel file."""
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=[timestamp_column])
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {e}")

    heatmap_df = parse_timestamps_to_heatmap(df, timestamp_column)
    fig = setup_plot(heatmap_df, title, user_utc_offset)
    return fig

def heatmap_from_plaintext(file_path, title, timestamp_format='%Y-%m-%d %H:%M:%S', user_utc_offset=0):
    """Generates a heatmap from a plaintext file with timestamps."""
    try:
        with open(file_path, 'r') as file:
            timestamps = pd.DataFrame(file.read().splitlines(), columns=['timestamp'])
    except Exception as e:
        raise ValueError(f"Error reading plaintext file: {e}")

    timestamps['timestamp'] = pd.to_datetime(timestamps['timestamp'], format=timestamp_format, errors='coerce')
    timestamps = timestamps.dropna(subset=['timestamp'])
    heatmap_df = parse_timestamps_to_heatmap(timestamps, 'timestamp')
    fig = setup_plot(heatmap_df, title, user_utc_offset)
    return fig

def heatmap_from_csv(file_path, timestamp_column, title, timestamp_format='%Y-%m-%d %H:%M:%S', user_utc_offset=0):
    """Generates a heatmap from a CSV file."""
    try:
        df = pd.read_csv(file_path, usecols=[timestamp_column])
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {e}")

    df[timestamp_column] = pd.to_datetime(df[timestamp_column], format=timestamp_format, errors='coerce')
    df = df.dropna(subset=[timestamp_column])
    heatmap_df = parse_timestamps_to_heatmap(df, timestamp_column)
    fig = setup_plot(heatmap_df, title, user_utc_offset)
    return fig

# Example usage:
# fig = heatmap_from_excel('data/example.xlsx', 'Sheet1', 'timestamp', 'Excel Data', user_utc_offset=+8)
# fig.show()
# fig = heatmap_from_plaintext('data/timestamps.txt', 'Plaintext Data', user_utc_offset=-5)
# fig.show()
# fig = heatmap_from_csv('data/events.csv', 'timestamp', 'CSV Data', user_utc_offset=+3)
# fig.show()
