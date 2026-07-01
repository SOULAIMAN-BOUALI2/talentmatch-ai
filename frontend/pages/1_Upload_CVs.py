import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/upload/"

st.title("📄 Import des CV")

uploaded_files = st.file_uploader(
    "Sélectionnez un ou plusieurs CV",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Importer"):

    if not uploaded_files:

        st.warning("Veuillez sélectionner au moins un PDF.")

    else:

        files = []

        for file in uploaded_files:

            files.append(

                (
                    "files",
                    (
                        file.name,
                        file,
                        "application/pdf"
                    )
                )

            )

        with st.spinner("Analyse des CV..."):

            response = requests.post(
                API_URL,
                files=files
            )

        if response.status_code == 200:

            st.success("Import terminé.")

            st.json(
                response.json()
            )

        else:

            st.error(response.text)