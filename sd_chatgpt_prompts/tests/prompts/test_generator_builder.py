from sd_chatgpt_prompts.generator_builder import GeneratorBuilder


def test_generator_builder():
    openai_api_key = ""
    prefix = "If you are an AI artist, please describe a painting, must includes the following elements:"
    elements = "girl, castle, sky"

    generator_builder = GeneratorBuilder(openai_api_key, prefix)

    result = generator_builder.generate_prompts(elements)

    print(result)


test_generator_builder()
