# Data Preprocessing CLI Tool

This project is a command-line tool that provides data preprocessing functionalities for machine learning tasks. The tool is developed using Python and utilizes the pandas and scikit-learn libraries.
## Features

The tool provides the following preprocessing functionalities:
    
   <ul>
   <li>Data Description: displays the description of a particular column, the description of all columns, or the entire dataset.</li>
   <li>Handling Null Values: allows the user to remove a column or fill null values with mean, median, or mode.</li>
   <li>Encoding Categorical Data: allows the user to perform one hot encoding of a column or display the categorical columns.</li>
   <li>Feature Scaling of the Dataset: allows the user to normalize or standardize the dataset.</li>
   <li>Download the Modified Dataset: allows the user to download the modified dataset.</li>
   </ul>

## Installation

To use this tool, follow these steps:
    <ol>
    <li>Clone this repository to your local machine.</li>
    <li>Create a virtual environment and activate it.</li>
    <li>Install the required packages using the command pip install -r requirements.txt.</li>
    </ol>
## Usage

To use the tool, run the following command:

`python main.py input_file.csv`

where input_file.csv is the path to your input CSV file.

After running the command, the tool will display the columns in the dataset and prompt you to select a preprocessing task.
## Contributing

Contributions are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.
