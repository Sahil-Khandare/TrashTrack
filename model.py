import streamlit as st
from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")


@st.cache_resource
def load_model():

    classifier = pipeline(
        "image-classification",
        model="prithivMLmods/Augmented-Waste-Classifier-SigLIP2",
        token=HF_TOKEN
    )

    return classifier


def predict_waste(classifier, image):

    results = classifier(image)

    return results