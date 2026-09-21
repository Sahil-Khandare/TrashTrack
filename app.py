import streamlit as st

from model import load_model, predict_waste
from guidance import get_guidance
from utils import load_css, process_image

st.set_page_config(
    page_title="TrashTrack",
    page_icon="♻️",
    layout="wide"
)

load_css("style.css", "assets/background.png")

st.markdown(
    "<h1><b>TrashTrack</b></h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3><i>AI Powered Waste Identification & Smart Segregation</i></h3>",
    unsafe_allow_html=True
)

with st.spinner("Loading AI waste classifier..."):
    classifier = load_model()

uploaded_file = st.file_uploader(
    "Upload an image of a waste item",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    try:
        image = process_image(uploaded_file)

    except Exception:
        st.error("Unable to process this image. Please upload a valid JPG or PNG.")
        st.stop()

    st.image(
        image,
        caption="Uploaded Waste Image",
    )

    with st.spinner("Analyzing waste image..."):
        results = predict_waste(classifier, image)

    top_result = results[0]

    label = top_result["label"]
    confidence = top_result["score"]
    
    information = get_guidance(label)

    st.subheader("Analysis")

    st.success(
        f"Detected Waste: **{label.title()}**"
    )

    st.metric(
        "AI Confidence",
        f"{confidence:.2%}"
    )

    if confidence < 0.40:

        st.error(
            "TrashTrack is not confident enough to "
            "provide a disposal recommendation."
        )

        st.warning(
            f"The model predicted **{label.title()}**, but "
            f"its confidence is only **{confidence:.2%}**."
        )

        st.info(
            "Please upload a clearer image containing "
            "a single waste item."
        )

    elif confidence <= 0.60:

        st.warning(
            f"The AI has moderate confidence "
            f"({confidence:.2%}) in this prediction."
        )

        st.info(
            "The recommendation below is only a general "
            "suggestion. Please verify the waste type "
            "before disposal."
        )

        if information:

            st.subheader("Suggested Waste Category")
            st.info(information["category"])

            st.subheader("Suggested Disposal Guidance")
            st.write(information["guidance"])

            st.subheader("Sustainability Tip")
            st.write(information["tip"])

    else:

        st.success(
            f"High-confidence prediction "
            f"({confidence:.2%})"
        )

        if information:

            st.subheader("Recommended Waste Category")
            st.success(information["category"])

            st.subheader("Disposal Guidance")
            st.write(information["guidance"])

            st.subheader("Sustainability Tip")
            st.write(information["tip"])

    st.markdown("---")

    st.subheader("Prediction Breakdown")

    for result in results[:5]:

        result_label = result["label"]
        result_score = result["score"]

        st.write(
            f"**{result_label.title()}** — "
            f"{result_score:.2%}"
        )

        st.progress(float(result_score))

    st.caption(
        "Responsible AI Notice: Predictions are generated "
        "by an AI image-classification model and may be "
        "incorrect. Disposal recommendations are general "
        "guidance and may vary according to local "
        "waste-management rules."
    )

with st.sidebar:

    st.markdown(
        "<h2 class='sidebar-title'>Waste Categories</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="category-item">
            <span>Organic / Wet Waste</span>
        </div>

        <div class="category-item">
            <span>Recyclable / Dry Waste</span>
        </div>

        <div class="category-item">
            <span>Hazardous / E-Waste</span>
        </div>

        <div class="category-item">
            <span>Textile / Reuse</span>
        </div>

        <div class="category-item">
            <span>Residual Waste</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
<div class="bmc-footer">
<p>For Official Waste Management Info:</p>
<a href="https://portal.mcgm.gov.in/irj/portal/anonymous/qlchfengswm" target="_blank">
BMC Solid Waste Management Department
</a>
</div>
""",
    unsafe_allow_html=True
)