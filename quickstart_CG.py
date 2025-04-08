from deepsearcher.configuration import Configuration, init_config
from deepsearcher.online_query import query

# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# local_path = './assets/pdf'

# website_url = 'https://en.wikipedia.org/wiki/Event_camera'

config = Configuration()

# Customize your config here,
# more configuration see the Configuration Details section below.
config.set_provider_config("llm", "OpenAI", {"model": "gpt-4o-mini"})
# config.set_provider_config("llm", "OpenAI", {"model": "o1-mini"})
# config.set_provider_config("llm", "TogetherAI", {"model": "deepseek-ai/DeepSeek-V3"})

config.set_provider_config("embedding", "OpenAIEmbedding", {"model": "text-embedding-3-small"})
# config.set_provider_config("embedding", "OpenAIEmbedding", {"model": "text-embedding-ada-002"})

# config.set_provider_config("file_loader", "PDFLoader", {})
# config.set_provider_config("embedding", "OpenAIEmbedding", {"model", "text-embedding-ada-002"}) ## This doesn't work, gives mapping error
init_config(config = config)

# Load your local data
# from deepsearcher.offline_loading import load_from_local_files
# load_from_local_files(paths_or_directory= local_path)

# # (Optional) Load from web crawling (`FIRECRAWL_API_KEY` env variable required)
# from deepsearcher.offline_loading import load_from_website
# load_from_website(urls=website_url)

# Query
result = query("Discuss the phenomena that could result in flickering in unresolved MWIR pixels containing a rocket plume.") # Your question here