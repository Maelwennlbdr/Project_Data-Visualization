import streamlit as st

# https://coolors.co/palette/f6bd60-f7ede2-f5cac3-84a59d-f28482

st.markdown("""
    <style>
    .a:link, .a:visited {
      background-color: #84A59D;
      color: #F2E8CF;
      padding: 14px 25px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      width: 100%;
    }

    .a:hover, .a:active {
      background-color: #5D847A;
    }

    .sous_a:link, .sous_a:visited {
      color: #5D847A;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      width: 100%;
    }

    .sous_a:hover, .sous_a:active {
      background-color: #FFF8F0;
    }

    h1, h2, h3, h4, h5, h6, p, label {
        color: #3B524C !important;
    }

    </style>
    """, unsafe_allow_html=True)

# Sidebar pour la navigation
with st.sidebar:
    st.image("./file/shooting-IMG_5665-36.png", width=150)
    st.title("Maelwenn Labidurie")
    st.header('Data and Artificial Intelligence')
    st.markdown('**Étudiante de M1 à EFREI Paris**')
    st.markdown("Promo: 2026")

    st.markdown('📧: Maelwenn.Labidurie@gmail.com')

    pdfFileObj = open('./file/CV_Maelwenn_Labidurie.pdf', 'rb')
    st.download_button('CV', pdfFileObj, file_name='CV_Maelwenn_Labidurie.pdf', mime='application/pdf')

    github = "https://github.com/Maelwennlbdr"
    st.markdown("[Github](%s)" % github)

    linkedin = "https://www.linkedin.com/in/maelwenn-labidurie-b94285223/"
    st.markdown("[Linkedin](%s)" % linkedin)

    # Navigation avec des boutons
    st.subheader("Navigation")
    app_1 = st.button("Cinema dataset")
    main = st.button("Portfolio/CV")


# Fonction pour exécuter et afficher le contenu d'un fichier Python
def execute_python_file(filepath):
    try:
        with open(filepath, 'r') as file:
            file_content = file.read()
            exec(file_content, globals())  # Exécution du contenu du fichier
    except Exception as e:
        st.error(f"Erreur lors de l'exécution du fichier {filepath}: {e}")


# Logiciel de navigation
if app_1:
    execute_python_file("./page/dataSet.py")
else:
    st.title('Welcome')
    st.markdown(
        'This is a project for the course *Data Visualization*. '
        'This project will present data from a dataset containing information on cinema attendance in France between 1980 and 2023.')

    st.markdown("# Table of contents")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
            <a href="#timeline" class="a">Timeline</a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
                    <a href="#skills" class="a">Skills</a>
                """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
                    <a href="#projects" class="a">Project</a>
                """, unsafe_allow_html=True)
        st.markdown(f"""
                    <a href="#machine" class="sous_a">Machine learning</a>
                """, unsafe_allow_html=True)
        st.markdown(f"""
                    <a href="#data" class="sous_a">Data Visualization</a>
                """, unsafe_allow_html=True)

    st.markdown("<div id='timeline'></div>", unsafe_allow_html=True)
    st.markdown("# Timeline")
    events = [
        {"year": "2018-2021", "name": "High School", "city": "Lannion",
         "details": "\nBaccalaureate with honours - specialty Mathematics and Physics."},
        {"year": "2021-2023", "name": "Prépa EFREI", "city": "Bègles",
         "details": "\nClassic preparatory class at EFREI Bordeaux."},
        {"year": "2023", "name": "Semester abroad", "city": "Toronto",
         "details": "\nSemester abroad at ILAC - Toronto."},
        {"year": "2024-2026", "name": "L3-M2", "city": "Villejuif",
         "details": "\nEnd of EFREI studies. Major Data and Artificial Intelligence (DAI)."}
    ]

    cols = st.columns(len(events))

    # Gestion des événements cliqués
    for i, event in enumerate(events):
        # Créer un bouton coloré pour chaque événement
        with cols[i]:
            if st.button(event["year"], key=event["name"], help=event["name"], use_container_width=True):
                st.write(f"**{event['name']} ({event['city']})** : {event['details']}")

    st.markdown("<div id='skills'></div>", unsafe_allow_html=True)
    st.markdown("# Skills")

    # Ajouter du style CSS personnalisé
    st.markdown("""
        <style>
        .skill-container {
            width: 100%;
            background-color: #f1f1f1;
            border-radius: 20px;
            margin: 10px 0;
            cursor: pointer; /* Change le curseur au survol */
        }
        .skill {
            text-align: left;
            padding: 10px;
            color: white;
            border-radius: 20px;
        }
        .skill-level {
            height: 30px;
            border-radius: 20px;
            line-height: 30px;
            padding-left: 10px;
        }
        .skill-text {
            font-size: 18px;
            font-weight: bold;
        }
        .python { width: 90%; background-color: #F28482; }
        .sql { width: 65%; background-color: #84A59D; }
        .ml { width: 85%; background-color: #F6BD60; }
        .math { width: 93%; background-color: #C7B8A8; }
        .dataViz { width: 77%; background-color:#F5CAC3; }
        .english { width: 86%; background-color: #C2837A; }
        </style>
        """, unsafe_allow_html=True)

    # Liste des compétences avec des niveaux et des détails
    skills = {
        "Python": {"class": "python", "details": ["Streamlit", "NumPy", "Pandas", "Scikit-learn", "tqdm", "..."]},
        "SQL": {"class": "sql", "details": ["NoSQL", "MySQL", "Oracle live"]},
        "Machine Learning": {"class": "ml",
                             "details": ["Decision tree", "MLP", "Random forest", "KNN", "Linear regression",
                                         "Logistic regression"]},
        "Mathematics": {"class": "math", "details": ["Statistics", "Probability", "Algebra", "Analysis"]},
        "Data Visualization": {"class": "dataViz", "details": ["Matplotlib", "Seaborn", "Plotly"]},
        "English": {"class": "english", "details": ["TOEIC - 920"]}
    }

    # Générer et afficher les skills avec des expandeurs
    for skill_name, skill_info in skills.items():
        # Afficher la barre de compétence
        st.markdown(f"""
            <div class="skill-container">
                <div class="skill {skill_info['class']}">
                    <div class="skill-text">{skill_name}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Créer un expander pour afficher les détails
        with st.expander(f"More detail", expanded=False):
            st.write(", ".join(skill_info["details"]))

    st.markdown("<div id='projects'></div>", unsafe_allow_html=True)
    st.markdown("# Projects")
    st.markdown("<div id='machine'></div>", unsafe_allow_html=True)
    st.markdown("## Machine Learning")
    st.markdown("### Boston housing dataset")
    with open("./file/Boston_housing.html", 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    st.components.v1.html(html_content, height=800, scrolling=True)

    st.markdown("### Wisconsin Breast Dataset")
    with open("./file/lab4_Albane_Maelwenn.html", 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    st.components.v1.html(html_content, height=800, scrolling=True)

    st.markdown("<div id='data'></div>", unsafe_allow_html=True)
    st.markdown("## Data Visualization")
    st.markdown("### Uber dataset 1")
    with open("./file/uber_1.html", 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    st.components.v1.html(html_content, height=800, scrolling=True)

    st.markdown("### Uber dataset 2")
    with open("./file/uber_2.html", 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
