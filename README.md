# 🧠 Acetylcholinesterase Bioactivity Prediction using Machine Learning
### 🔬 Predicting pIC₅₀ values of molecules using cheminformatics and ML, powered by PaDEL-Descriptor and Streamlit.
---

## 📘 Overview
This project predicts the **bioactivity (pIC₅₀)** of molecules against the **Acetylcholinesterase (AChE)** enzyme — a crucial target in neurodegenerative diseases such as **Alzheimer’s**. It integrates **cheminformatics**, **PaDEL molecular descriptors**, and **machine learning** into an interactive **Streamlit** web app.  
Users can upload a `.txt` file containing **SMILES strings** and **Molecule IDs**, automatically generate **PubChemFP descriptors**, and predict **pIC₅₀** values using a trained ML model.

---

## 🚀 Features
- 📤 Upload `.txt` file containing SMILES and molecule IDs  
- ⚗️ Automatically compute **PubChemFP descriptors** using **PaDEL**  
- 🧮 Predict **pIC₅₀** values using a pre-trained **scikit-learn** model  
- 📊 Display predictions in a beautiful interactive table  
- 💾 Download prediction results as a `.csv` file  
- 🧠 Clean, scientific, and user-friendly interface  

---

## 🧠 Background Concepts

### 🔹 Acetylcholinesterase (AChE)
A key enzyme that breaks down acetylcholine. Its inhibition improves memory and cognitive function — making it a target for **Alzheimer’s disease** drugs.

### 🔹 SMILES
**Simplified Molecular Input Line Entry System** — a textual way to represent molecular structures.  
Example:  
`CCO` → Ethanol  
`CC(=O)O` → Acetic acid

### 🔹 PaDEL-Descriptor
An open-source Java-based software that computes **over 1,400 molecular descriptors** and **12 fingerprint types**.  
Here, it’s used to generate **PubChemFP fingerprints**, converting molecules into numeric vectors suitable for ML models.

### 🔹 pIC₅₀
A transformed representation of IC₅₀ (half-maximal inhibitory concentration):  
\[
pIC_{50} = -\log_{10}(IC_{50} \times 10^{-9})
\]  
Higher pIC₅₀ = Stronger inhibition.

---

## 💡 Project Approach

1️⃣ **Data Collection:**  
   Data was retrieved from the **ChEMBL** database containing SMILES and IC₅₀ values for AChE inhibitors.  

2️⃣ **Descriptor Generation:**  
   Used **PaDEL-Descriptor** to generate **PubChemFP** molecular fingerprints.  

3️⃣ **Data Preprocessing:**  
   - Removed null and duplicate records  
   - Filtered descriptors for variance and correlation  
   - Saved final features to `descriptor_list.csv`  

4️⃣ **Model Training:**  
   - Evaluated models: Random Forest, Decision Tree, XGBoost  
   - Chose best model using R², RMSE, MAE  
   - Saved trained model as `acetylcholinesterase_model.pkl`  

5️⃣ **Streamlit Deployment:**  
   A web interface allows users to upload SMILES, generate descriptors, and predict pIC₅₀ values.

---

## 📂 Project Structure

bio_informatics_project/  
│  
├── app/  
│   ├── app.py                         # Streamlit main app  
│   ├── acetylcholinesterase_model.pkl # Trained ML model  
│   ├── descriptor_list.csv            # List of descriptors used for training  
│   ├── requirements.txt               # Dependencies list  
│   ├── mols/                          # Temporary molecule storage  
│   ├── sample_input.txt               # Example input file  
│  
├── acetylcholinesterase_bioinformatics_part_1.py  
├── acetylcholinesterase_bioinformatics_part_2.py  
├── acetylcholinesterase_bioinformatics_part_3.py  
├── acetylcholinesterase_bioinformatics_part_4.py  
├── acetylcholinesterase_bioinformatics_part_5.py  
├── .gitignore  
└── README.md  

---

## 📄 Input Example
**sample_input.txt**

CHEMBL192  CC(=O)Oc1ccccc1C(=O)O  
CHEMBL1824 CCOC(=O)c1ccc(O)cc1  
CHEMBL1825 CCN(CC)CCCC(C)Nc1ccc2c(c1)OCO2  

---

## 📊 Output Example
| Molecule ID | Predicted pIC₅₀ |
|--------------|----------------|
| CHEMBL192 | 4.7357 |
| CHEMBL1824 | 3.3010 |
| CHEMBL1825 | 7.5224 |

---

## 🖥️ Streamlit App (Screenshots)
<p align="center">
  <img src="screenshots/1.png" width="360" alt="Upload file interface">
  <img src="screenshots/2.png" width="360" alt="Prediction results table">
</p>
> Add your screenshots inside the `/screenshots` folder to display them here.

---

## ⚙️ Installation & Usage
### 🧩 Step 1 — Clone the Repository
git clone https://github.com/your-username/acetylcholinesterase-bioactivity.git  
cd acetylcholinesterase-bioactivity/app  

### 🧩 Step 2 — Create a Virtual Environment
python -m venv venv  

Activate the environment  
- **Windows:** venv\Scripts\activate  
- **macOS / Linux:** source venv/bin/activate  

### 🧩 Step 3 — Install Dependencies
pip install -r requirements.txt  

### 🧩 Step 4 — Run the Streamlit App
streamlit run app.py  

After running the command, open the local URL (usually http://localhost:8501) in your browser.  
Upload a `.txt` file containing **SMILES strings** and **Molecule IDs**, click **Predict**, and view results instantly.  
You can also download predictions as a `.csv` file from the app interface.

---

## 🧠 Technologies Used
| Tool | Purpose |
|------|----------|
| **Python** | Core programming language |
| **PaDEL-Descriptor** | Descriptor and fingerprint generation |
| **scikit-learn** | Machine learning model training |
| **Streamlit** | Web-based user interface |
| **pandas / numpy** | Data processing |
| **joblib** | Model serialization |
| **ChEMBL Database** | Source of molecular bioactivity data |

---

## 🔮 Future Work
- Add more descriptor sets (e.g., MACCSFP, CDKFP)  
- Extend prediction to other enzyme targets  
- Integrate molecular docking validation  
- Enable multi-file batch uploads  
- Containerize the app with **Docker**  
- Deploy on **Hugging Face Spaces** or **Streamlit Cloud**

---

## 📚 References
- [ChEMBL Database](https://www.ebi.ac.uk/chembl/)  
- [PaDEL-Descriptor](http://www.yapcwsoft.com/dd/padeldescriptor/)  
- [scikit-learn Documentation](https://scikit-learn.org/stable/)  
- Yap CW. (2011). *PaDEL-Descriptor: An open-source software to calculate molecular descriptors and fingerprints.* _Journal of Computational Chemistry._
