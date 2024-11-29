# Project Setup

## Steps to Download `requirements.txt` and Freeze Requirements

1. **Download `requirements.txt**:

    ```sh
    wget https://example.com/path/to/requirements.txt -O requirements.txt
    ```

2. **Install the requirements**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Freeze the current environment's packages**:

    ```sh
    pip freeze > requirements.txt
    ```

Make sure to commit the updated `requirements.txt` file to the repository if any new packages are added.