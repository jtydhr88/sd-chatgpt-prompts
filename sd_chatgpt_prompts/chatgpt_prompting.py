from sd_chatgpt_prompts.generator_builder import GeneratorBuilder
import modules.scripts as scripts
from pathlib import Path
import gradio as gr
from modules.shared import opts
import modules
from modules import script_callbacks

VERSION = "0.1.0"

base_dir = Path(scripts.basedir())

def generate_prompts(elements):
    openai_api_key = ""
    prefix = "If you are an AI artist, please describe a painting, must includes the following elements:"

    generator_builder = GeneratorBuilder(openai_api_key, prefix)

    result = generator_builder.generate_prompts(elements)

    return result

loaded_count = 0


class Script(scripts.Script):
    def __init__(self):
        global loaded_count
        loaded_count += 1

        if loaded_count % 2 == 0:
            return

    def title(self):
        return f"ChatGPT Prompts v{VERSION}"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        self.infotext_fields = []
        ctrls_group = (gr.State(is_img2img),)

        with gr.Group():
            with gr.Accordion("ChatGPT", open=False, elem_id="chatgpt"):
                with gr.Group():
                    ctrls = self.uigroup(is_img2img)

                    ctrls_group += ctrls

                return ctrls_group

    def uigroup(self, is_img2img):
        ctrls = ()
        infotext_fields = []

        with gr.Row():
            chatgpt_prompt_elements = gr.Textbox(
                label=opts.chatgpt_prefix,
                value="",
                elem_id="chatgpt-prompt-elements"
            )

        def chat(chatgpt_prompt_elements_input):
            openai_api_key = opts.openai_api_key
            prefix = opts.chatgpt_prefix
            temperature = float(opts.chatgpt_temperature)
            max_tokens = int(opts.max_tokens)

            generator_builder = GeneratorBuilder(openai_api_key, prefix, temperature, max_tokens)

            result = generator_builder.generate_prompts(chatgpt_prompt_elements_input)

            print(result)

            return result

        chat_button = gr.Button(value="Chat and send the result to prompt")

        chat_button.click(fn=chat, inputs=[chatgpt_prompt_elements])

        ctrls += (chatgpt_prompt_elements, chat_button, )

        return ctrls

    def process(self, p, is_img2img=False, *args):
        print("process")

