from transformers import AutoTokenizer, AutoModelForCausalLM
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def load_model(model_id):
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(model_id)

        return tokenizer, model
    except Exception as e:
        log.error(f"Failed to load model {model_id}: {str(e)}")
        return None, None

load_model("gpt2")