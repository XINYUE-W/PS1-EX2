Q1 When you added your .gitignore to your repo to ignore .csv files, was the file indeed ignored?
Yes. After adding *.csv to the .gitignore file, any new CSV files I created were no longer tracked by Git. However, the ones that had already been committed before, such as gdp_clean.csv, were still shown.
To stop tracking them completely, I used the command git rm --cached gdp_clean.csv. After that, Git ignored all .csv files as expected.


Q2 Why do we have to add additional_dependencies to mypy in the .pre-commit-config.yaml?

Each pre-commit hook runs in its own small virtual environment, which doesn’t automatically include all the packages used in the project. Adding additional_dependencies makes sure that mypy has access to the type stubs for libraries like pandas, requests, and matplotlib.
Without these, mypy would report missing import errors. Including them allows type checking to run smoothly inside pre-commit.
