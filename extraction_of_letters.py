{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPvT9jCk+Hnjg15wAlbWCvu"
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Z44Y6q6JDGsn"
      },
      "outputs": [],
      "source": [
        "# extraction of vowels from a string"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l=\"hello\"\n",
        "for val in l:\n",
        "  if val in ('a','e','i','o','u'):\n",
        "    print(val)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dWm2hBqKDymk",
        "outputId": "e1ed5f51-c9b7-4c24-e33d-dcdfb2e4b7df"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "e\n",
            "o\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "s=\"HelloWorld\"\n",
        "res=list(filter(lambda c:c.isupper(),s))\n",
        "print(res)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s0fDOBKGGtAt",
        "outputId": "36b8f07a-def8-4132-d07a-ee85dca30485"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['H', 'W']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#function to check the upper case letters in string\n",
        "def strup():\n",
        "  for val in s:\n",
        "    if val in (\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"):\n",
        "      print(val)\n",
        "strup()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wM7bBvdUG60J",
        "outputId": "684d8a4a-c3ff-47a1-b550-81a9c4b67950"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "H\n",
            "W\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "dx2nPhANHllR"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}