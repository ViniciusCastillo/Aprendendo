{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNlaadLeDqQJEFX/qTr0rqj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ViniciusCastillo/Aprendendo/blob/master/teste_fonte.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DwxxpryPKK5J",
        "outputId": "1cd7e145-756d-466a-bf2b-9723ee16473e"
      },
      "source": [
        "import pandas as pd\n",
        "dados = pd.read_csv(\"https://raw.githubusercontent.com/ViniciusCastillo/Aprendendo/master/A165345189_28_143_208.csv\", encoding=\"ISO-8859-1\", skiprows=3, skipfooter=12, sep=\";\", thousands=\".\", decimal=\",\")\n",
        "# criando o campo do códgio da região\n",
        "dados[\"Cod_Região\"]=dados[\"Unidade da Federação\"].str[0]\n",
        "# inclui os nomes das regiões\n",
        "Base_regioes = pd.DataFrame({\"Cod\":[\"1\",\"2\",\"3\",\"4\",\"5\"],\"Região\":[\"Norte\",\"Nordeste\",\"Sudeste\",\"Sul\",\"Centro-Oeste\"]}, columns=[\"Cod\",\"Região\"])\n",
        "Base_regioes = Base_regioes.set_index(\"Cod\")\n",
        "# inclui os nomes das regiões em dados\n",
        "dados = dados.join(Base_regioes, on=\"Cod_Região\")\n",
        "# retirando os números de antes do nome dos estados\n",
        "dados[\"Unidade da Federação\"] = dados[\"Unidade da Federação\"].str.replace(\"\\d+\", \"\")\n",
        "dados[\"Unidade da Federação\"] = dados[\"Unidade da Federação\"].str.strip()"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:2: ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support skipfooter; you can avoid this warning by specifying engine='python'.\n",
            "  \n"
          ]
        }
      ]
    }
  ]
}