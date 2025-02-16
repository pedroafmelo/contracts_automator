# -*- coding: UTF-8 -*-
"""Import Modules"""
from os.path import join, dirname
from dataclasses import dataclass
from yaml import load
from yaml.loader import SafeLoader


@dataclass
class Variables:
    """ Variables dataclass """
    
    # paths and extensions
    static_dir: str
    pleno_logo: str
    texto_performance: str
    contrato_single: str
    contrato_joint: str


class Config:
    """Configuration Interface"""

    def __init__(self) -> None:
        """Load instance Variables"""
        
        data = {}
        with open(join(dirname(__file__), "env.yaml"), encoding="utf-8") as file:
            data=load(file, Loader=SafeLoader)

        self.vars = Variables(
                static_dir=data.get("static_dir"),
                pleno_logo=data.get("pleno_logo"),
                texto_performance=data.get("texto_performance"),
                contrato_single=data.get("contrato_single"),
                contrato_joint=data.get("contrato_joint")
        )
        
        self.meses_ano = [
                "janeiro", "fevereiro", "março", "abril", "maio", "junho",
                "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
                ]

    def __repr__(self) -> str:
        """ Basic class
        representation """

        return str(self.vars)
    
    def __str__(self) -> str:
        """ Print
        representation """

        return str(self.vars)