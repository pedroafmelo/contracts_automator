# TO DO
"""
- Conversar com o Matheus para ver possibilidade de incluir CEP e emissor do documento como 
"""

# -*- coding: UTF-8 -*-
"""Import Modules"""
import pandas as pd
from io import StringIO, BytesIO
from docx import Document
from pdf2docx import Converter
from datetime import datetime
import streamlit as st
import zipfile
from num2words import num2words


class Utils:
    """Files Manipulator class"""

    def __init__(self):
        """Initializes Instance"""
        
        # import local modules
        from config import Config

        self.config = Config()


    def replace_words(self, docx_path: str, 
                      replacement_dict: dict) -> BytesIO:
        """Replaces the chosen words
        of the docx file"""

        doc = Document(docx_path)

        for pg in doc.paragraphs:
            for old_text, new_text in replacement_dict.items():
                pg.text = pg.text.replace(old_text, new_text)

        edited_docx_stream = BytesIO()
        doc.save(edited_docx_stream)
        edited_docx_stream.seek(0)

        return edited_docx_stream


    def receive_database(self, xlsx_file_fytes: BytesIO) -> pd.DataFrame:
        """Receives .xlsx file
        Return cleaned dataframe"""

        xlsx_file_fytes = BytesIO(xlsx_file_fytes.read())
        data = pd.read_excel(xlsx_file_fytes)

        return data
    
    @staticmethod
    def converter_porcentagem(texto):
        numero = texto.replace('%', '').replace(',', '.')
        valor = float(numero)
        texto_escrito = num2words(valor, lang='pt_BR').replace('ponto', 'vírgula')
    
        return f"{texto_escrito} por cento"
    

    def replace_from_table(self, doc_path) -> BytesIO | tuple:
        """Gets information 
        for each row"""

        def get_rows(row) -> dict:

            nome_secundario = row.get("Nome Completo - Titular Secundário", "").upper().strip()
            est_civil_secundario = row.get("Estado Civil - Titular Secundário", "").lower().strip()
            cpf_secundario = row.get("CPF - Titular Secundário", "").strip()
            endereco_secundario = row.get("Endereço Completo - Titular Secundário", "")
            email_secundario = row.get("E-mail - Titular Secundário", "")

            rg_cliente = f"Portador da Cédula de Identidade RG de nº {row["RG"]}"
            rg_secundario = f"Portador da Cédula de Identidade RG de nº {row.get("RG - Titular Secundário", "")}"


            return {
                "[nome_titular]": row["Nome Completo"].upper().strip(),
                "[nome_secundario]": nome_secundario,
                "[est_civil_titular]": row["Estado Civil"].lower().strip(),
                "[est_civil_secundario]": est_civil_secundario,
                "[documento_titular]": rg_cliente,
                "[documento_secundario]": rg_secundario,
                "[cpf_titular]": row["CPF"].strip(),
                "[cpf_secundario]": cpf_secundario,
                "[endereco_titular]": row["Endereço Completo"].strip(),
                "[endereco_secundario]": endereco_secundario,
                "[email_titular]": row["E-mail"].lower().strip(),
                "[email_secundario]": email_secundario,
                "[assinatura_titular]": row["Nome Completo"].upper().strip(),
                "[assinatura_secundario]": nome_secundario,
                "[data_emissao]": f"{datetime.today().day} de {self.config.meses_ano[datetime.today().month - 1]} de {datetime.today().year}",
                "[texto_performance]": self.config.vars.texto_performance
                }
        
        c1, c2, c3 = st.columns([4, .5, 3])

        uploaded_file = c1.file_uploader("Faça o upload da tabela em excel", type="xlsx")

        if uploaded_file is not None:
            table = self.receive_database(uploaded_file)

            if len(table) > 1:
            
                if "current_client" not in st.session_state:
                    st.session_state["current_client"] = 0

                if "zip_buffer" not in st.session_state:
                    st.session_state["zip_buffer"] = BytesIO()

                zip_buffer = st.session_state["zip_buffer"]
                current_client = st.session_state["current_client"]

                if current_client >= len(table):
                    zip_buffer.seek(0)
                    c3.write("#")
                    c3.download_button("Baixar Contratos Personalizados",
                                    zip_buffer,
                                    "Contratos Gestão.zip",
                                    "application/zip")
                    st.stop()
                
                
                row = table.iloc[current_client]
                replacements = get_rows(row)

                taxa_gestao = c3.text_input(f"Qual a taxa de gestão acordada para o cliente {replacements["[nome_titular]"]}?")

                if c3.button("Gerar contrato"):
                    if not taxa_gestao.strip():
                        c3.error("Preencha a taxa de gestão deste cliente antes de continuar!")
                    else:
                        taxa_gestao_escrito = self.converter_porcentagem(taxa_gestao)
                        replacements["[taxa_gestao]"] = taxa_gestao
                        replacements["[taxa_gestao_escrito]"] = taxa_gestao_escrito

                        edited_docstream = self.replace_words(docx_path=doc_path, 
                                                            replacement_dict=replacements)

                        filename = f"Contrato Gestão {replacements["[nome_titular]"].split(" ")[0]} {replacements["[nome_titular]"].split(" ")[1]}.docx"

            
                        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
                            zip_file.writestr(filename, edited_docstream.getvalue())

                        st.session_state["current_client"] += 1
                        st.rerun()

            else:
                replacements = get_rows(row=table.iloc[0])        
                edited_docstream = self.replace_words(docx_path=doc_path, 
                                                    replacement_dict=replacements)
                c3.write("#")
                c3.download_button("Baixar Contrato Personalizado",
                                    edited_docstream.getvalue(),
                                    "Contratos Gestão.zip",
                                    "application/zip")