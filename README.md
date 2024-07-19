# California Housing Price Prediction
![image](https://github.com/user-attachments/assets/622c1365-7eb9-47fe-92c4-be66e6852646)


https://github.com/user-attachments/assets/d470d9ac-f730-4b0b-ab6a-e942015b1f12


## Description
This project aims to predict housing prices in California using various features such as median income, housing median age, total rooms, and proximity to the ocean. The project utilizes a machine learning pipeline to preprocess data, train a model, and evaluate its performance.

## Installation
To run this project, you will need Python 3.11.7 and the following libraries:
- NumPy
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn
- ydata_profiling

You can install these dependencies using pip:

## Usage
To use this project, follow these steps:
1. Clone the repository to your local machine.
2. Run the Jupyter Notebook `california_house.ipynb` to perform data analysis, model training, and evaluation.

## Data Analysis
The project starts with an exploratory data analysis (EDA) using pandas profiling and seaborn for visualization. This includes univariate and multivariate analysis to understand the relationships between different features.

## Model Training and Evaluation
Several regression models are trained and evaluated to predict the median house value. The models include RandomForestRegressor, AdaBoostRegressor, and GradientBoostingRegressor, among others. The best-performing model is identified through cross-validation and further optimized using hyperparameter tuning.

## Results
The RandomForestRegressor model with specific hyperparameters was found to perform the best. The model achieved an R2 score of [insert R2 score here] on the test set, indicating [brief explanation of the result].

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the [insert license here] License - see the LICENSE file for details.

## Acknowledgments
- Thanks to [Dataset source] for providing the California housing dataset.
- Inspired by [any tutorials, articles, etc. that inspired your project].
