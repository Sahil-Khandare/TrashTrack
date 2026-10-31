# TrashTrack – AI-Powered Waste Classification & Smart Segregation

**TrashTrack** is an AI powered waste classification and disposal guidance web application developed as part of the **1M1B AI for Sustainability Virtual Internship**, supported by AICTE in collaboration with IBM SkillsBuild.

The application uses an AI image-classification model to identify different types of waste from uploaded images and provides appropriate waste categories, disposal recommendations, and sustainability tips.

TrashTrack aims to make waste segregation easier and encourage responsible consumption, recycling, and reuse.

**Live Application:** https://trashtrack-ai.streamlit.app/

## Problem Statement

Improper waste segregation and limited awareness of disposal methods contribute to environmental pollution, landfill accumulation, and inefficient recycling.

People often struggle to identify whether an item should be recycled, reused, composted, or disposed of as residual or hazardous waste.

TrashTrack addresses this problem by providing an accessible AI-powered solution that helps users identify waste materials and understand appropriate disposal practices.

## Solution

TrashTrack combines AI based image classification with a rule based disposal guidance system.

Users upload an image of a waste item, and the AI model predicts its category. Based on the prediction, the application displays relevant disposal guidance and sustainability tips.

### Key Features

- **AI Waste Classification:** Identifies waste materials from uploaded images.
- **Multiple Waste Categories:** Supports 10 classes of waste.
- **Smart Disposal Guidance:** Provides category-specific disposal recommendations.
- **Sustainability Tips:** Encourages recycling, reuse, and responsible waste management.
- **Confidence-Based Predictions:** Uses confidence thresholds to handle uncertain predictions.
- **Prediction Breakdown:** Displays the top five model predictions with confidence scores.
- **User Friendly Interface:** Built with Streamlit and custom CSS styling.
- **Responsible AI Notice:** Communicates prediction limitations and encourages users to verify disposal recommendations.

## AI Model

TrashTrack uses the following Hugging Face image classification model:

**Model:** [Augmented-Waste-Classifier-SigLIP2](https://huggingface.co/prithivMLmods/Augmented-Waste-Classifier-SigLIP2)

The model predicts one of the following 10 waste classes:

| AI Prediction | Waste Category |
|---|---|
| Battery | Hazardous / E-Waste |
| Biological | Organic / Wet Waste |
| Cardboard | Recyclable / Dry Waste |
| Glass | Recyclable Waste |
| Metal | Recyclable / Dry Waste |
| Paper | Recyclable / Dry Waste |
| Plastic | Recyclable / Dry Waste |
| Clothes | Textile / Reuse |
| Shoes | Textile / Reuse |
| Trash | Residual Waste |

### Confidence-Based Recommendation System

TrashTrack uses confidence thresholds to determine how recommendations are displayed:

| Model Confidence | Application Behaviour |
|---|---|
| Below 40% | Displays an uncertainty warning and requests a clearer image. |
| 40%–60% | Displays a cautious, general disposal suggestion. |
| Above 60% | Displays the recommended waste category and disposal guidance. |

The AI model performs single-label image classification. Images containing multiple waste items may produce uncertain predictions.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application and user interface |
| Hugging Face Transformers | AI image-classification pipeline |
| SigLIP2 | Waste image-classification model |
| PyTorch | Deep learning framework |
| Pillow (PIL) | Image processing and conversion |
| HTML & CSS | Interface styling |
| python-dotenv | Environment variable management |

## Project Architecture

```text
                 User
                   |
                   v
          Upload Waste Image
                   |
                   v
              app.py
          (Streamlit UI)
                   |
                   v
             utils.py
       (Image Preprocessing)
                   |
                   v
              model.py
        (SigLIP2 Classifier)
                   |
                   v
          Predicted Waste Label
                   |
                   v
             guidance.py
       (Rule-Based Guidance)
                   |
                   v
       Confidence-Based Analysis
                   |
                   v
       Disposal Guidance & Tips
```

## Project Structure

```text
TrashTrack/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│   └── background.png
│
├── app.py
├── model.py
├── guidance.py
├── utils.py
├── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation & Setup

Follow these steps to run TrashTrack locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Sahil-Khandare/TrashTrack.git
```

### 2. Navigate to the Project Directory

```bash
cd TrashTrack
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Hugging Face Token (Optional)

If you use a Hugging Face access token, create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token
```

Keep your `.env` file private and never upload it to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## Sustainable Development Goals (SDGs)

TrashTrack primarily supports:

### SDG 12 – Responsible Consumption and Production

Encourages responsible waste segregation, recycling, reuse, and reduction of waste generation.

### SDG 11 – Sustainable Cities and Communities

Promotes awareness of proper waste management practices that contribute to cleaner and more sustainable communities.

### SDG 13 – Climate Action

Encourages sustainable consumption and waste-management habits that can contribute to reducing environmental impact.

## Responsible AI & Limitations

- Predictions are generated by an AI image classification model and may not always be correct.
- The model is designed to classify one primary waste item, not detect multiple objects independently.
- Confidence scores indicate the model's prediction confidence, not guaranteed real world accuracy.
- Disposal recommendations are general guidance and may vary depending on local waste management regulations.
- Users should verify hazardous waste disposal instructions with appropriate local authorities.

## Future Improvements

- Support for detecting multiple waste items in a single image.
- Integration of location specific waste disposal guidelines.
- Addition of nearby recycling and waste collection centre information.
- Improved classification through additional training data.
- Support for more regional waste categories and disposal practices.

## Developed By

**Sahil Anand Khandare**

AI for Sustainability Virtual Internship Project

**1M1B (One Million for One Billion)**  
Supported by AICTE | In collaboration with IBM SkillsBuild

## Project Links

- **Live Application:** https://trashtrack-ai.streamlit.app/
- **GitHub Repository:** https://github.com/Sahil-Khandare/TrashTrack
- **AI Model:** https://huggingface.co/prithivMLmods/Augmented-Waste-Classifier-SigLIP2

---

<p align="center">
  ♻️ <b>TrashTrack – Making Waste Segregation Smarter for a Sustainable Tomorrow.</b>
</p>
