# -*- coding: UTF-8 -*-
"""Import Modules"""
import streamlit as st
import pandas as pd
from io import StringIO, BytesIO
import tempfile
from docx import Document
from os import path
from datetime import datetime


class ContractAutomator:
    """Contract Automator Class"""

    def __init__(self) -> None:

        # import local modules

        from config import Config
        from utils import Utils
        from forms import Forms
        
        self.config = Config()
        self.util = Utils()
        self.forms = Forms()

        self.single_cont_path = path.join(self.config.vars.static_dir,
                                  self.config.vars.contrato_single)
        
        self.joint_cont_path = path.join(self.config.vars.static_dir,
                                  self.config.vars.contrato_joint)

        st.set_page_config("Pleno Contratos", page_icon="📝", layout="wide")


    def cover(self) -> None :
        """Generates App cover"""
    
        st.image(path.join(self.config.vars.static_dir,
                           self.config.vars.pleno_logo), width=350)

        st.markdown(
                    """
                    <style>

                    button {
                        color: white !important;
                        display: flex !important;
                        justify-content: center !important;
                    }

                    button:hover {
                        color: white !important;
                        border: 2px solid blue !important;
                    }

                    button:active {
                        color: black !important;
                        background-color: blue !important;
                        border: 2px solid blue !important;
                        box-shadow: none !important; /* Remove efeito vermelho */
                    }

                    button:focus {
                        color: white !important;
                        border: 2px solid blue !important;
                        outline: none !important;
                    }

                    [data-testid="stExpander"] :hover summary {
                        color: white !important; 
                        border: 2px blue !important;
                    }

                    </style>

                    <div style="padding-top: 0px; padding-bottom: 0px;">
                        <h1 style="margin: 0; color: white">Automatizador de Contratos</h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown("""<hr style="height:2px;border:none;color:blue;background-color:blue;" /> """,
                        unsafe_allow_html=True)


    def individual_single_contract(self):
        """Receives Informations
        Makes a single Contract"""

        st.write("#")

        replacements = self.forms.single_account_form()

        st.session_state["contract_replacements"] = replacements

        c1, c2, c3 = st.columns([4, .5, 3])

        if st.button("Concluir"):

            if all(replacements.values()):
                
                data_assinatura = f"{datetime.today().day} de {self.config.meses_ano[datetime.today().month - 1]} de {datetime.today().year}"
                
                st.session_state["contract_replacements"]["[data_emissao]"] =  data_assinatura
                st.session_state["contract_replacements"]["[taxa_gestao_escrito]"] = self.utils.converter_porcentagem(replacements["[taxa_gestao]"])
                
                edited_docx_stream = self.util.replace_words(docx_path=self.single_cont_path,
                                                        replacement_dict= st.session_state["contract_replacements"])

                st.download_button(
                    label="Faça o Download do contrato personalizado",
                    data=edited_docx_stream.getvalue(),
                    file_name=f"Contrato Gestão {replacements["[nome_titular]"]}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            else:
                c1.error("Preencha todos os campos em questão, mesmo que com um espaço em branco")


    def joint_single_contract(self):
        """Receives JA Informations
        Makes a single Contract"""

        st.write("#")

        replacements = self.forms.joint_account_form()

        st.session_state["contract_replacements"] = replacements

        c1, c2, c3 = st.columns([4, .5, 3])

        if st.button("Concluir"):

            if all(replacements.values()):

                data_assinatura = f"{datetime.today().day} de {self.config.meses_ano[datetime.today().month - 1]} de {datetime.today().year}"
                
                st.session_state["contract_replacements"]["[data_emissao]"] =  data_assinatura
                st.session_state["contract_replacements"]["[taxa_gestao_escrito]"] = self.utils.converter_porcentagem(replacements["[taxa_gestao]"])
                
                edited_docx_stream = self.util.replace_words(docx_path=self.joint_cont_path,
                                                        replacement_dict= st.session_state["contract_replacements"])
                
                st.download_button(
                    label="Faça o Download do contrato personalizado",
                    data=edited_docx_stream.getvalue(),
                    file_name=f"Contrato Gestão {replacements["[nome_cliente]"]}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
            
            else:
                c1.error("Preencha todos os campos em questão, mesmo que com um espaço em branco")


    def __call__(self):
        """Runs the Instance"""

        self.cover()

        if "selected_contract" not in st.session_state:
            st.session_state["selected_contract"] = "individual"

        with st.sidebar:
            conta_individual = st.button("Gerar contrato - Conta Individual")
            conta_conjunta = st.button("Gerar contrato - Conta Conjunta")

        if conta_conjunta:
            st.session_state["selected_contract"] = "conjunta"
        elif conta_individual:
            st.session_state["selected_contract"] = "individual"
        
        if st.session_state["selected_contract"] == "conjunta":
            if st.toggle("Gerar contratos a partir de arquivo excel", value=True):
                st.write("#")
                self.util.replace_from_table(self.joint_cont_path)
            else:
                self.joint_single_contract()
        else:
            if st.toggle("Gerar contratos a partir de arquivo excel", value=True):
                st.write("#")
                self.util.replace_from_table(self.single_cont_path)
            else:
                self.individual_single_contract()