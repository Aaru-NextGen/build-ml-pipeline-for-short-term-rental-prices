This project is an attempt to predict rental prices. 


## SetUp

Clone the project
```bash
git clone https://github.com/Aaru-NextGen/build-ml-pipeline-for-short-term-rental-prices.git
```

Go into the project.
```
cd build-ml-pipeline-for-short-term-rental-prices
```

### Project dependencies

1. Python
2. Pip
2. Pyenv

### Create environment

Make sure to have pyenv install ( instruction to install pyenv **here** ) and ready, then create a new environment using the ``requirements.txt``.

```bash
> python -m venv [name_of_the_env_folder] 
> pip install -r requirements.txt
> soruce .[name_of_the_env_folder]/bin/activate
```

### Get API key for Weights and Biases
Let's make sure we are logged in to Weights & Biases. Get your API key from W&B by going to 
[https://wandb.ai/authorize](https://wandb.ai/authorize) and click on the + icon (copy to clipboard), 
then paste your key into this command:

```bash
> wandb login [your API key]
```

You should see a message similar to:
```
wandb: Appending key for api.wandb.ai to your netrc file: /home/[your username]/.netrc
```

If interested in the already created artifact visit public project in W&B here.______


## Usage

### Running a single step

```bash
> mlflow run . -P steps=<name_of_the_step> --env-manager=virtualenv
```
These are the folloing list of step names.

1. download
2. basic_cleaning
3. data_check
4. data_split
5. train_random_forest
6. test_regression_model

*Note* : before running make sure if all the parameters of that step is available in W$B or local depending on the setp.

Details of each step of the parameters required for each step are avilable in the MLproject file in each step present in ``component`` folder or ``src`` folder.

To run entire flow as it is or to overwrite some parameters or for hyperparameter optimization, use mlflow command as follows

```base
# over all flow
> mlflow run . --env-manager=virtualenv

# to overwrite few parameter
> mlflow run . \
  -P hydra_options="modeling.random_forest.n_estimators=10 etl.min_price=50"
```

## W&B and GitHub links
1. w&B repo [link](https://wandb.ai/arunprabhath/nyc_airbnb?workspace=user-arunprabhath)
2. github repo [link](https://github.com/Aaru-NextGen/build-ml-pipeline-for-short-term-rental-prices)