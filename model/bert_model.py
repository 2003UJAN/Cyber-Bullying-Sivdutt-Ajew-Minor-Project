from transformers import BertTokenizer, BertForSequenceClassification
import torch

model_name = "unitary/toxic-bert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probs = torch.softmax(logits, dim=1)
    label = torch.argmax(probs).item()
    confidence = probs[0][label].item()
    return label, confidence
