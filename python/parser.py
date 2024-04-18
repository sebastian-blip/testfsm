import os.path

import textfsm
import pandas as pd

from metadata.path import Path


def parsear_data(comando: str):
    """

    Args:
        comando:

    Returns:

    """

    templates = Path.__dict__

    with open(templates.get(f'data_{comando}'), "r") as f:
        data_content = f.read()

    with open(templates.get(comando), "r") as f:
        re_table = textfsm.TextFSM(f)
        result = re_table.ParseText(data_content)



    # Crear DataFrame de Pandas
    columns = re_table.header
    df = pd.DataFrame(result, columns=columns)
    salida = os.path.join(Path.out_, f'{comando}.csv')
    df.to_csv(salida)


if __name__ == '__main__':
    parsear_data('mpls_deteils')
    parsear_data('route_table')
    parsear_data('mpls_prelines')
    parsear_data('mpls_deteils')
