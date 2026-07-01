import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/search/"


st.title("🔍 TalentMatch Search")


query = st.text_area(
    "Décrivez le profil recherché"
)


if st.button("Rechercher"):

    if query.strip() == "":

        st.warning("Veuillez saisir une recherche.")

    else:

        response = requests.post(

            API_URL,

            json={

                "query": query

            }

        )

        if response.status_code == 200:

            results = response.json()

            if len(results) == 0:

                st.warning("Aucun candidat trouvé.")

            else:

                st.success(f"{len(results)} candidat(s) trouvé(s).")

                for candidate in results:

                    st.subheader(candidate["name"])

                    st.metric(

                        "Score",

                        f'{candidate["score"]}%'

                    )

                    st.write("Email :", candidate["email"])

                    st.write("Ville :", candidate["city"])

                    st.write("Expérience :", candidate["experience_years"])

                    st.write("Compétences :")

                    st.write(candidate["skills"])

                    st.divider()

        else:

            st.error(response.text)