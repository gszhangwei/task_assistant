from abc import ABC, abstractmethod
from config import SCRIPT_PROMPT_TEMPLATE


class BasePromptGenerator(ABC):
    def __init__(self, scripts, description):
        self.scripts = scripts
        self.description = description

    @abstractmethod
    def generate_prompt(self, input_text):
        pass

    def create_script_prompt(self, input_text):
        descriptions = "\n".join([f"{key}: {value}" for key, value in self.scripts.items()])
        return SCRIPT_PROMPT_TEMPLATE.format(
            scripts=', '.join(self.scripts.keys()),
            input_text=input_text,
            descriptions=descriptions
        )


class PromptGenerator(BasePromptGenerator):
    def generate_prompt(self, input_text):
        prompt = self.create_script_prompt(input_text)
        print("Script prompt:", prompt)
        return prompt


class AdvancedPromptGenerator(BasePromptGenerator):
    def generate_prompt(self, input_text):
        # 可以在这里添加高级生成器的特定逻辑
        prompt = self.create_script_prompt(input_text)
        print("Script prompt:", prompt)
        return prompt

