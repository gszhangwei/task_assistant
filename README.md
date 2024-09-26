# Script Analysis and Execution System

## Project Introduction

This is a script analysis and execution system based on Streamlit and Ollama. The system can analyze the text input by the user, determine the appropriate generator type, generate the corresponding script name, and execute the matching script. The entire process is presented through a user-friendly web interface.

## Main Features

- Text Input: Users can input the text that needs to be analyzed.
- Automatic Analysis: The system uses the Ollama model to analyze the input and determine the appropriate generator type.
- Script Selection: Based on the analysis results, the system generates the corresponding script name.
- Script Execution: If a matching script is found, the system will execute the script and return the result.
- Result Display: The execution result is directly displayed on the web interface.

## Environment Requirements

- Python 3.10+
- Streamlit
- Langchain
- Ollama

## Environment Setup Steps

1. Clone the project repository:
   ```
   git clone git@github.com:gszhangwei/task_assistant.git
   cd task_assistant
   ```

2. Create and activate a virtual environment (optional):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip3 install -r requirements.txt
   ```

4. Install and set up Ollama:
   - Visit [Ollama Official Website](https://ollama.ai/) to download and install Ollama
   - Ensure Ollama service is running by executing `ollama run llama3.1`

5. Configure the project:
   - Check and update the configuration information in the `config.py` file
   - Ensure the paths in `GENERATOR_CONFIG` are set correctly

## Running the Application

Execute the following command in the project root directory:
```streamlit run src/app.py```

Then visit the displayed URL in your browser (usually `http://localhost:8501`).

## Usage Instructions

1. Enter the content you want to analyze in the text box.
2. Click the "Analyze and Execute" button.
3. The system will automatically analyze your input and execute the corresponding script.
4. The execution result will be displayed on the page.

## Project Structure
````
project/
│
├── src/
│ ├── advanced_scripts
│ ├── expert_scripts
│ ├── python_scripts
│ ├── app.py # Main Streamlit application file
│ ├── execute_script_with_ollama.py # Core logic implementation
│ ├── prompt_generator_factory.py # Prompt generator factory
│ └── config.py # Configuration file
│
├── requirements.txt # Project dependencies
└── README.md # Project documentation
````

## Contribution
Feel free to submit issues and pull requests. This is a basic version, and there is much room for improvement. We hope everyone can provide feedback and help improve it together.

## License
[MIT](https://choosealicense.com/licenses/mit/)