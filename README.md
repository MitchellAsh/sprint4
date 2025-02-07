# Sprint4

Render: https://sprint4-26cu.onrender.com

Description

This project is an interactive tool designed to analyze and visualize information about vehicles in the United States. Using a dataset containing details such as price, model year, condition, type, odometer readings, and more, this tool allows users to explore trends and relationships between different vehicle attributes.

The project is built using Streamlit for the user interface and Plotly for dynamic and interactive visualizations.

Features

	•	Scatterplot Visualization: Analyze relationships between attributes like price, model year, odometer readings, and vehicle types.
	•	Dynamic Filters: Use checkboxes to filter the data by vehicle type.
	•	Interactive Interface: Hover over data points to see detailed information about individual vehicles.

Methods and Libraries Used

The following Python libraries were used in this project:
	•	Streamlit: To create an interactive and easy-to-use web application.
	•	Plotly: For creating scatterplots and other dynamic visualizations.
	•	Pandas: For data manipulation and preprocessing.

 How to Run the Project Locally

Follow these steps to set up and run the project on your local machine:

1. Clone the Repository

Clone the repository to your local machine:
git clone <repository_url>

2. Navigate to the Project Folder

Change your working directory to the project folder:
cd sprint4

3. Install Dependencies

Install the required libraries using pip:
pip install -r requirements.txt

4. Run the Application

Run the Streamlit app:
streamlit run app.py

5. Open in Your Browser

Once the app starts, Streamlit will provide a local URL (e.g., http://localhost:8501/). Open this URL in your web browser to use the tool.

Usage

This tool allows users to:
	•	Explore Data Trends: Visualize relationships like how vehicle prices vary with model year, condition, or odometer readings.
	•	Filter by Attributes: Focus on specific vehicle types (e.g., SUVs, sedans).
	•	Gain Insights: Identify trends, outliers, or patterns in US vehicle data.
