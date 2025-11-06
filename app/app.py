import streamlit as st
import pandas as pd
import os
import shutil
import joblib
from padelpy import padeldescriptor

# -------------------------------
# Streamlit Page Setup
# -------------------------------
st.set_page_config(
    page_title="Acetylcholinesterase Bioactivity Predictor",
    page_icon="🧪",
    layout="wide"
)

st.markdown(
    """
    <style>
        .stApp {
            background-color: #f8fafc;
        }
        .main-title {
            text-align: center;
            font-size: 2.2rem;
            color: #1e3a8a;
            margin-bottom: 0.5rem;
        }
        .sub-title {
            text-align: center;
            font-size: 1rem;
            color: #334155;
            margin-bottom: 2rem;
        }
        .success-box {
            background-color: #ecfdf5;
            border-radius: 10px;
            padding: 0.6rem 1rem;
            color: #065f46;
        }
        .info-box {
            background-color: #eff6ff;
            border-radius: 10px;
            padding: 0.6rem 1rem;
            color: #1e3a8a;
        }
        .section-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: #1e40af;
            margin-top: 1.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------------
# Page Header
# -------------------------------
st.markdown("<h1 class='main-title'>🧪 Acetylcholinesterase Bioactivity Predictor</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='sub-title'>Upload a <b>.txt</b> file containing SMILES and Molecule IDs.<br>"
    "The app will generate <b>PubChemFP descriptors</b>, predict <b>pIC₅₀</b> values using your trained model,<br>"
    "and return results as a downloadable CSV.</p>",
    unsafe_allow_html=True,
)

# -------------------------------
# File Upload Section
# -------------------------------
uploaded_file = st.file_uploader("📂 Upload your SMILES text file", type=['txt'])

if uploaded_file is not None:
    # Save uploaded file locally
    input_path = "input_molecules.smi"
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.markdown("<div class='success-box'>✅ File uploaded successfully!</div>", unsafe_allow_html=True)

    # Display uploaded data
    st.markdown("<h3 class='section-title'>📘 Input Molecules</h3>", unsafe_allow_html=True)
    uploaded_data = pd.read_csv(uploaded_file, sep="\t", header=None, names=["SMILES", "Molecule_ID"])
    st.dataframe(uploaded_data, use_container_width=True)

    # -------------------------------
    # Create required folder for PaDEL
    # -------------------------------
    if not os.path.exists("mols"):
        os.mkdir("mols")

    # Move file (cross-platform)
    shutil.move(input_path, os.path.join("mols", "molecule.smi"))

    st.markdown("<div class='info-box'>🧩 Generating PubChemFP descriptors using PaDEL... Please wait.</div>", unsafe_allow_html=True)

    # -------------------------------
    # Generate Descriptors
    # -------------------------------
    padeldescriptor(
        mol_dir='mols',
        d_file='descriptors.csv',
        fingerprints=True,
        retainorder=True,
        removesalt=True,
        standardizenitro=True
    )

    st.markdown("<div class='success-box'>✅ Descriptors generated successfully!</div>", unsafe_allow_html=True)

    df_desc = pd.read_csv("descriptors.csv")
    st.markdown("<h3 class='section-title'>🧮 Example of Generated Descriptors</h3>", unsafe_allow_html=True)
    st.dataframe(df_desc.head(), use_container_width=True)

    # -------------------------------
    # Load trained model & descriptor list
    # -------------------------------
    model_path = "acetylcholinesterase_model.pkl"
    descriptor_list_path = "descriptor_list.csv"

    if os.path.exists(model_path) and os.path.exists(descriptor_list_path):
        model = joblib.load(model_path)
        st.markdown("<div class='success-box'>✅ Trained model loaded!</div>", unsafe_allow_html=True)

        if 'Name' in df_desc.columns:
            df_desc = df_desc.drop(columns=['Name'])

        descriptor_list = pd.read_csv(descriptor_list_path)
        feature_names = descriptor_list.columns.tolist()

        X = df_desc.reindex(columns=feature_names, fill_value=0)

        st.markdown(f"<div class='info-box'>🔢 {len(feature_names)} features matched from training descriptors.</div>", unsafe_allow_html=True)

        # -------------------------------
        # Predict pIC50
        # -------------------------------
        predictions = model.predict(X)
        df_results = pd.DataFrame({
            "Molecule_ID": uploaded_data["Molecule_ID"],
            "SMILES": uploaded_data["SMILES"],
            "Predicted_pIC50": predictions
        })

        # Save output
        output_file = "predicted_pIC50_results.csv"
        df_results.to_csv(output_file, index=False)

        st.markdown("<h3 class='section-title'>🔍 Prediction Results</h3>", unsafe_allow_html=True)
        st.dataframe(df_results, use_container_width=True)

        st.download_button(
            label="📥 Download Predictions as CSV",
            data=open(output_file, "rb").read(),
            file_name="predicted_pIC50_results.csv",
            mime="text/csv"
        )

    else:
        if not os.path.exists(model_path):
            st.error("❌ Trained model file not found. Please place 'acetylcholinesterase_model.pkl' in the app directory.")
        if not os.path.exists(descriptor_list_path):
            st.error("❌ Descriptor list file not found. Please place 'descriptor_list.csv' in the app directory.")
