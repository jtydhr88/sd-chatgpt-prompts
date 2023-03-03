import openai


class GeneratorBuilder:
    def __init__(self, openai_api_key, prefix, temperature=0.6, max_tokens=512):
        self._openai_api_key = openai_api_key
        self._prefix = prefix
        self._temperature = temperature
        self._max_tokens = max_tokens

        openai.api_key = self._openai_api_key

    def generate_prompts(self, elements):
        prompts = self._prefix + elements

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompts,
            temperature=self._temperature,
            max_tokens=self._max_tokens,
        )

        result = response.choices[0].text

        return result
