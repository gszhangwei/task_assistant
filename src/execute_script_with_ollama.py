import subprocess
from langchain_community.llms import Ollama
from prompt_generator_factory import PromptGeneratorFactory
from config import GENERATOR_CONFIG, GENERATOR_PROMPT_TEMPLATE
import os


def execute_script(script_name, script_path):
    path_join = os.path.join(script_path, script_name)
    try:
        result = subprocess.run(['python3', path_join], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"执行脚本 {script_name} 时出错: {e}"


def analyze_and_execute(input_text):
    llm = Ollama(model="llama3.1")
    generator_type = determine_generator_type(llm, input_text)
    script_name = generate_script_name(llm, generator_type, input_text)
    print("Script_name: ", script_name)
    return execute_script_if_valid(generator_type, script_name)


def determine_generator_type(llm, input_text):
    generator_type_prompt = create_generator_type_prompt(input_text)
    print("Generator_type_prompt: ", generator_type_prompt)
    generator_type_response = llm.invoke(generator_type_prompt)
    print("Generator_type_response: ", generator_type_response)
    print("")
    return generator_type_response.strip()


def create_generator_type_prompt(input_text):
    available_generator_types = PromptGeneratorFactory.get_available_generator_types()
    descriptions = "\n".join([f"{key}: {value['description']}" for key, value in GENERATOR_CONFIG.items()])
    return GENERATOR_PROMPT_TEMPLATE.format(
        types=', '.join(available_generator_types),
        input_text=input_text,
        descriptions=descriptions
    )


def generate_script_name(llm, generator_type, input_text):
    prompt_generator = PromptGeneratorFactory.get_prompt_generator(generator_type)
    script_prompt = prompt_generator.generate_prompt(input_text)
    script_response = llm.invoke(script_prompt)
    return script_response.strip()


def execute_script_if_valid(generator_type, script_name):
    prompt_generator = PromptGeneratorFactory.get_prompt_generator(generator_type)
    if script_name in prompt_generator.scripts:
        script_path = GENERATOR_CONFIG[generator_type]['path']
        return execute_script(script_name, script_path)
    else:
        return "未找到匹配的脚本或响应无效。"
