from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

MODEL_NAME = "framonmar7/depression-classifier"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
