"""
Testes de validação de datas e horas
"""

import pytest
from source.valid_entries import *


@pytest.mark.parametrize(
    'data, retorno',
    [
        ('01/01/2020', '01/01/2020'),
        ('31/12/2025', '31/12/2025'),
        ('29/02/2020', False),
        ('-8/12/2025', False),
        ('', False),
        ('01 08 2019', False),
    ]
)
def test_data_valida(data, retorno):
    assert data_valida(data) == retorno


@pytest.mark.parametrize(
    'hora, retorno',
    [
        ('00:00', '00:00'),
        ('23:59', '23:59'),
        ('24:00', False),        
        ('23:99', False),
        ('12 00', False),        
    ]
)
def test_hora_valida(hora, retorno):
    assert hora_valida(hora) == retorno
