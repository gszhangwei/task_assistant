from abc import ABC, abstractmethod


class BasePromptGenerator(ABC):
    def __init__(self, scripts):
        self.scripts = scripts

    @abstractmethod
    def generate_prompt(self, input_text):
        pass


class PromptGenerator(BasePromptGenerator):
    def generate_prompt(self, input_text):
        script_list = "\n".join([f"{i + 1}. {script}" for i, script in enumerate(self.scripts)])
        prompt = f"根据以下输入，选择一个Python脚本并执行：\n\n{input_text}\n\n可选脚本：\n{script_list}\n\n请只返回要执行的脚本文件名。"
        return prompt


class AdvancedPromptGenerator(BasePromptGenerator):
    def generate_prompt(self, input_text):
        script_list = "\n".join([f"{i + 1}. {script}" for i, script in enumerate(self.scripts)])
        prompt = f"高级模式：根据以下输入，选择一个Python脚本并执行：\n\n{input_text}\n\n可选脚本：\n{script_list}\n\n请只返回要执行的脚本文件名。"
        return prompt


class ExpertPromptGenerator(BasePromptGenerator):
    def generate_prompt(self, input_text):
        script_list = "\n".join([f"{i + 1}. {script}" for i, script in enumerate(self.scripts)])
        prompt = f"专家模式：根据以下输入，选择一个Python脚本并执行：\n\n{input_text}\n\n可选脚本：\n{script_list}\n\n请只返回要执行的脚本文件名。"
        return prompt
