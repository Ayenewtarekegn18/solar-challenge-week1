# Solar Data Analysis Dashboard

This project provides an interactive dashboard for analyzing solar data from multiple locations in West Africa.

## Features

- Interactive data visualization using Streamlit
- Multiple dataset comparison (Benin, Togo, Sierra Leone)
- Boxplots of Global Horizontal Irradiance (GHI)
- Top regions analysis
- Time series analysis
- Correlation analysis
- Weather impact visualization

## Development Process

1. Project Structure:

   ```
   ├── app/
   │   ├── __init__.py
   │   ├── main.py      # Streamlit application
   │   └── utils.py     # Utility functions
   ├── data/            # Data files (gitignored)
   ├── notebooks/       # Jupyter notebooks for analysis
   └── requirements.txt # Project dependencies
   ```

2. Setup:

   - Create and activate virtual environment:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate  # Windows
     source venv/bin/activate # Linux/Mac
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. Running the Dashboard:
   ```bash
   streamlit run app/main.py
   ```

## Usage

1. Launch the dashboard using the command above
2. Use the sidebar to:
   - Select datasets to compare
   - Navigate between different analysis pages
3. Available pages:
   - Overview: GHI comparison and top regions
   - Time Series Analysis: Temporal patterns
   - Correlation Analysis: Variable relationships
   - Weather Impact: Weather effects on solar generation

## Data

The dashboard uses the following datasets:

- Benin (Malanville)
- Togo (Dapaong)
- Sierra Leone (Bumbuna)

Note: Data files are stored locally and gitignored for privacy.

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## License

This project is licensed under the MIT License.
