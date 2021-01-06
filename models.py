from config import Config
from modules.tts.synthesizer import Synthesizer


config = Synthesizer.load_config("data/config.yaml")

natasha = Synthesizer.from_config(config, name="natasha")

models = {
    "Natasha": natasha,
    Config.ALL_MODELS_KEY: None
}