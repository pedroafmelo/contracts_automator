# -*- codfing: UTF-8 -*-
"""Import Modules"""

import streamlit as st
from datetime import datetime


class Forms:
    """Contracts Formularies class"""

    def __init__(self):
        """Initializes Instance"""

        # import local modules
        
        from config import Config

        self.config = Config()


    def single_account_form(self) -> dict:
         """Generates Single Account
         Formulary"""
         
         c1, c2, c3 =st.columns([4, .5, 3])

         with c1.expander("Formulário de conta individual"):

            nome_cliente = st.text_input("Digite o nome do cliente")
            st.write("#")
            nacionalidade_cliente = st.text_input("Digite a nacionalidade do cliente")
            st.write("#")
            est_civil_cliente = st.text_input("Digite o estado civil do cliente")
            st.write("#")
            documento_cliente = st.selectbox("Escolha o documento do cliente: ", ["Identidade", "Passaporte"])
            st.write("#")
            if documento_cliente == "Identidade":
                numero_doc_cliente = st.text_input("Digite o RG do cliente")
                emissor_identidade = st.text_input("Digite o emissor do documento da identidade")
                documento_cliente = f"Portador da Cédula de Identidade RG de nº {numero_doc_cliente.upper()} {emissor_identidade.upper()}"
            else:
                numero_doc_cliente = st.text_input("Digite o Passaporte do cliente")
                documento_cliente = f"Portador do passaporte de nº {numero_doc_cliente.upper()}"
            st.write("#")
            cpf_cliente = st.text_input("Digite o cpf do cliente, no formado 999.999.999-99")
            st.write("#")
            endereco_cliente = st.text_input("Digite o endereço do cliente, no formato (Rua, número)")
            st.write("#")
            cidade_cliente = st.text_input("Digite o bairro, a cidade e o estado do cliente, no formato (Bairro, Cidade)")
            st.write("#")
            sigla_estado_cliente = st.text_input("Digite a sigla do estado do cliente")
            st.write("#")
            complemento_endereco = st.text_input("Digite o complemento do endereço do cliente, no formato (Ap. XXXX)")
            endereco_cliente = f"{endereco_cliente.capitalize()} - {complemento_endereco.capitalize()} - {cidade_cliente.capitalize()} - {sigla_estado_cliente.upper()}"
            st.write("#")
            cep_cliente = st.text_input("Digite o CEP do cliente, no formato (XXXXX-YYY)")
            st.write("#")
            email_cliente = st.text_input("Digite o e-mail do cliente")
            st.write("#")
            perfil_cliente = st.selectbox("Perfil do Cliente", ["Conservador", "Moderado", "Arrojado", "Agressivo"])
            if perfil_cliente == "Conservador":
                texto_performance = " "
            else:
                texto_performance = self.config.vars.texto_performance
            st.write("#")
            taxa_gestao = st.text_input("Digite a taxa de gestão acordada com o cliente, no formato x,y%")
            st.write("#")
            local_assinatura = st.text_input("Digite o local de assinatura do contrato de gestão, no formado Cidade - Sigla do Estado")

         replacements = {
            "[nome_titular]": nome_cliente.upper().strip(),
            "[nacionalidade_titular]": nacionalidade_cliente.lower().strip(),
            "[est_civil_titular]": est_civil_cliente.lower().strip(),
            "[documento_titular]": documento_cliente.strip(),
            "[cpf_titular]": cpf_cliente.strip(),
            "[endereco_titular]": endereco_cliente.strip(),
            "[cep_titular]": cep_cliente.strip(),
            "[email_titular]": email_cliente.lower().strip(),
            "[taxa_gestao]": taxa_gestao.strip(),
            "[texto_performance]": texto_performance,
            "[local_emissao]": local_assinatura.strip(),
            "[assinatura_titular]": nome_cliente.upper().strip(),
                }

         return replacements
    

    def joint_account_form(self) -> dict:
        """Generates Joint Account
        Formulary"""

        c1, c2 =st.columns(2)

        with c1.expander("Formulário de conta conjunta - Titular"):

            nome_titular = st.text_input("Digite o nome do titular")
            st.write("#")
            nacionalidade_titular = st.text_input("Digite a nacionalidade do titular")
            st.write("#")
            est_civil_titular = st.text_input("Digite o estado civil do titular")
            st.write("#")
            documento_titular = st.selectbox("Escolha o documento do titular: ", ["Identidade", "Passaporte"])
            st.write("#")
            if documento_titular == "Identidade":
                numero_doc_titular = st.text_input("Digite o RG do titular")
                emissor_identidade_titular = st.text_input("Digite o emissor do documento da identidade do titular")
                documento_titular = f"portador da Cédula de Identidade RG de nº {numero_doc_titular.upper()} {emissor_identidade_titular.upper()}"
            else:
                numero_doc_titular = st.text_input("Digite o Passaporte do titular")
                documento_titular = f"portador do passaporte de nº {numero_doc_titular.upper()}"
            st.write("#")
            cpf_titular = st.text_input("Digite o cpf do titular, no formado 999.999.999-99")
            st.write("#")
            endereco_titular = st.text_input("Digite o endereço do titular, no formato (Rua, número)")
            st.write("#")
            cidade_titular = st.text_input("Digite o bairro, a cidade e o estado do titular, no formato (Bairro, Cidade)")
            st.write("#")
            sigla_estado_titular = st.text_input("Digite a sigla do estado do titular")
            st.write("#")
            complemento_titular = st.text_input("Digite o complemento do endereço do titular, no formato (Ap. XXXX)")
            endereco_titular = f"{endereco_titular.capitalize()} - {complemento_titular.capitalize()} - {cidade_titular.capitalize()} - {sigla_estado_titular.upper()}"
            st.write("#")
            cep_titular = st.text_input("Digite o CEP do titular, no formato (XXXXX-YYY)")
            st.write("#")
            email_titular = st.text_input("Digite o e-mail do titular")
            st.write("#")
            perfil_titular = st.selectbox("Perfil do titular", ["Conservador", "Moderado", "Arrojado", "Agressivo"])
            if perfil_titular == "Conservador":
                texto_performance = ""
            else:
                texto_performance = self.config.vars.texto_performance
            st.write("#")
            taxa_gestao = st.text_input("Digite a taxa de gestão acordada com o titular, no formato x,y%")
            st.write("#")
            local_assinatura = st.text_input("Digite o local de assinatura do contrato de gestão, no formado Cidade - Sigla do Estado")


        with c2.expander("Formulário de conta conjunta - Secundário"):

            nome_secundario = st.text_input("Digite o nome do secundário")
            st.write("#")
            nacionalidade_secundario = st.text_input("Digite a nacionalidade do secundário")
            st.write("#")
            est_civil_secundario = st.text_input("Digite o estado civil do secundário")
            st.write("#")
            documento_secundario = st.selectbox("Escolha o documento do secundário: ", ["Identidade", "Passaporte"])
            st.write("#")
            if documento_secundario == "Identidade":
                numero_doc_secundario = st.text_input("Digite o RG do secundário")
                emissor_identidade_secundario = st.text_input("Digite o emissor do documento da identidade do secundário")
                documento_secundario = f"Portador da Cédula de Identidade RG de nº {numero_doc_secundario.upper()} {emissor_identidade_secundario.upper()}"
            else:
                numero_doc_secundario = st.text_input("Digite o Passaporte do secundário")
                documento_secundario = f"Portador do passaporte de nº {numero_doc_secundario.upper()}"
            st.write("#")
            cpf_secundario = st.text_input("Digite o cpf do secundário, no formado 999.999.999-99")
            st.write("#")
            moram_juntos = st.checkbox("Moram juntos", value=True)
            if not moram_juntos:
                endereco_secundario = st.text_input("Digite o endereço do secundário, no formato (Rua, número)")
                st.write("#")
                cidade_secundario = st.text_input("Digite o bairro, a cidade e o estado do secundário, no formato (Bairro, Cidade)")
                st.write("#")
                sigla_estado_secundario = st.text_input("Digite a sigla do estado do secundário")
                st.write("#")
                complemento_secundario = st.text_input("Digite o complemento do endereço do secundário, no formato (Ap. XXXX)")
                endereco_secundario = f"{endereco_secundario.capitalize()} - {complemento_secundario.capitalize()} - {cidade_secundario.capitalize()} - {sigla_estado_secundario.upper()}"
                st.write("#")
                cep_secundario = st.text_input("Digite o CEP do secundário, no formato (XXXXX-YYY)")
            else:
                endereco_secundario = endereco_titular
                cep_secundario = cep_titular
            st.write("#")
            email_secundario = st.text_input("Digite o e-mail do secundário")
            st.write("#")

        replacements = {
            "[nome_titular]": f"{nome_titular.upper().strip()}",
            "[nacionalidade_titular]": nacionalidade_titular.lower().strip(),
            "[est_civil_titular]": est_civil_titular.lower().strip(),
            "[documento_titular]": documento_titular.strip(),
            "[cpf_titular]": cpf_titular.strip(),
            "[endereco_titular]": endereco_titular.strip(),
            "[cep_titular]": cep_titular.strip(),
            "[email_titular]": email_titular.lower().strip(),
            "[nome_secundario]": f"{nome_secundario.upper().strip()}",
            "[nacionalidade_secundario]": nacionalidade_secundario.lower().strip(),
            "[est_civil_secundario]": est_civil_secundario.lower().strip(),
            "[documento_secundario]": documento_secundario.strip(),
            "[cpf_secundario]": cpf_secundario.strip(),
            "[endereco_secundario]": endereco_secundario.strip(),
            "[cep_secundario]": cep_secundario.strip(),
            "[email_secundario]": email_secundario.lower().strip(),
            "[taxa_gestao]": taxa_gestao.strip(),
            "[texto_performance]": texto_performance,
            "[local_emissao]": local_assinatura.strip(),
            "[assinatura_titular]": f"{nome_titular.upper().strip()}",
            "[assinatura_secundario]": f"{nome_secundario.upper().strip()}",
        }

        return replacements