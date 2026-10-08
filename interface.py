import streamlit as st
from chatbot import ask_llm




# 1. Configuration de la page
st.set_page_config(
    page_title="Orange Digital Center Maroc",
    page_icon="🟧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Injection du CSS Personnalisé (Style ODC + Chatbot Flottant)
st.markdown(
    """
    <style>
    /* --- Styles de la page ODC --- */
    .title-highlight {
        color: #FF7900;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 16px;
        margin-bottom: 0;
    }
    .odc-header {
        color: #000000;
        font-size: 50px;
        font-weight: 800;
        margin-top: 0;
        padding-top: 0;
    }
    
    /* Style des cartes pour les piliers */
    .pillar-card {
        background-color: #F8F9FA;
        padding: 30px;
        border-radius: 8px;
        border-bottom: 4px solid #FF7900;
        height: 100%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .pillar-card-black {
        border-bottom: 4px solid #000000;
    }
    .pillar-card h3 {
        color: #000000 !important;
        margin-bottom: 10px;
    }
    .pillar-card p {
        color: #555555;
        font-size: 16px;
    }

    /* --- Styles du Chatbot Flottant (Ultra-Robuste) --- */
    /* Positionnement du conteneur en bas à droite */
    div[data-testid="stPopover"] {
        position: fixed !important;
        bottom: 40px !important;
        right: 40px !important;
        width: 60px !important;
        height: 60px !important;
        z-index: 999999 !important;
    }

    /* Transformer le bouton en pastille ronde */
    div[data-testid="stPopover"] > button {
        width: 60px !important;
        height: 60px !important;
        border-radius: 50% !important;
        background-color: #000000 !important; /* Bouton noir pour contraster avec le orange */
        border: 2px solid #FF7900 !important;
        box-shadow: 0 6px 16px rgba(0,0,0,0.3) !important;
        padding: 0 !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        transition: transform 0.2s ease-in-out;
    }

    /* Masquer le chevron par défaut */
    div[data-testid="stPopover"] > button svg {
        display: none !important;
    }

    /* Style de l'émoji */
    div[data-testid="stPopover"] > button p {
        font-size: 28px !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Effet au survol */
    div[data-testid="stPopover"] > button:hover {
        transform: scale(1.1);
        background-color: #111111 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Contenu de la Page (Présentation ODC Maroc)
st.markdown("<p class='title-highlight'>Innovation & Inclusion</p>", unsafe_allow_html=True)
st.markdown("<h1 class='odc-header'>Orange Digital Center Maroc</h1>", unsafe_allow_html=True)
# st.markdown("### Propulser les talents numériques de demain.")
st.header("Propulser les talents numériques de demain.")
st.write("L'Orange Digital Center (ODC) est un écosystème complet dédié à l'accompagnement des jeunes, à la formation au numérique, et à l'innovation technologique au Maroc.")

st.divider()

st.header("L'Écosystème : 3 Programmes Clés")
st.write("Découvrez nos piliers pour vous accompagner de la formation jusqu'à l'entrepreneuriat :")

st.markdown("<br>", unsafe_allow_html=True)

# Affichage sous forme de colonnes (similaire à la slide Grid)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="pillar-card">
        <h3>💻 L'École du Code</h3>
        <p>Formation gratuite aux métiers technologiques pour les jeunes, avec ou sans diplôme, axée sur la pratique et l'insertion professionnelle.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pillar-card pillar-card-black">
        <h3>🛠️ FabLab Solidaire</h3>
        <p>Atelier de fabrication numérique ouvert équipé d'imprimantes 3D et de découpeuses laser pour prototyper et donner vie à vos projets.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="pillar-card">
        <h3>🚀 Orange Fab</h3>
        <p>Accélérateur de startups technologiques innovantes pour soutenir l'écosystème entrepreneurial et nouer des partenariats commerciaux.</p>
    </div>
    """, unsafe_allow_html=True)


# 4. Logique du Chatbot Flottant
# Initialisation de l'historique
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", 
         "content": "👋 Bonjour ! Je suis l'assistant de l'Orange Digital Center Maroc. Avez-vous une question sur l'École du Code, le FabLab ou Orange Fab ?"}
    ]


# Création du popover avec use_container_width=False
with st.popover("💬", use_container_width=False):
    st.markdown("**Assistant ODC Maroc** 🟧")
    
    # Conteneur des messages
    messages_container = st.container(height=275, width=500)
    with messages_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
                
    # # Champ de saisie
    # input_col1, input_col2 = st.columns([3, 1])
    # with input_col1:
    #     user_input = st.text_input("Posez votre question...", label_visibility="collapsed", key="chat_input")
    # with input_col2:
    #     send_button = st.button("Envoyer")
    with st.form(key="chat_form", clear_on_submit=True, border=False):
        input_col1, input_col2 = st.columns([3, 1])
        with input_col1:
            user_input = st.text_input("Posez votre question...", label_visibility="collapsed")
        with input_col2:
            send_button = st.form_submit_button("Envoyer")

    # Traitement du message envoyé
    if send_button and user_input:
        # Afficher le message utilisateur
        st.session_state.messages.append({"role": "user", "content": user_input})

        bot_response = ask_llm(st.session_state.messages)

        # Ajouter et afficher la réponse du bot
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.rerun()


