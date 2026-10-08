import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_llm(historique_streamlit: list) -> str:

    instructions_systeme = """
    Tu es l'assistant virtuel officiel de l'Orange Digital Center (ODC) Maroc.
    Ton rôle est de répondre aux questions des étudiants et des jeunes talents.
    
    Règles à respecter :
    - Sois toujours poli, accueillant et professionnel.
    - Réponds de manière concise (pas de longs paragraphes) et sous forme de bullets points/courts paragraphes lorsque tu vas lister les formations en cas de demande.
    - N'en fais pas trop de bullets !
    - Si tu ne connais pas la réponse, invite l'utilisateur à visiter le site web officiel de l'ODC Maroc "www.orangedigitalcentermaroc.com" ou à se rendre sur place.
    - Ne réponds qu'aux questions liées à la technologie, à la formation, à l'entrepreneuriat et à l'ODC Maroc.
    - Réponds juste en français.
    - Quand la personne te dit au revoir, fais un petit au revoir aussi en disant par exemple que nous sommes toujours heureux de vous acceuil chez odc agadir !
    """

    messages = [
        SystemMessage(content=instructions_systeme), # Le cadre / les règles
    ]

    for msg in historique_streamlit:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(AIMessage(content=msg["content"]))

    response = llm.invoke(messages)
    return response.content