{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/nabilaizzatul00/mentalhealthstudent/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uXBhAeSIET3W",
        "outputId": "52257667-7b65-416b-de3c-ef8edc5e53e4"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.7/9.7 MB\u001b[0m \u001b[31m67.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m92.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m5.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "\n",
        "import streamlit as st\n",
        "\n",
        "st.write('Hello, *World!* :sunglasses:')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A2Nm7UuJEnL0",
        "outputId": "9ceaa1b2-3740-4390-fdb9-7f5173a83013"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!npm install localtunnel"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "29zLhW8OEttR",
        "outputId": "7e7e7170-3795-460f-ece7-fe92972ec011"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K\n",
            "added 22 packages in 3s\n",
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K\n",
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K3 packages are looking for funding\n",
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K  run `npm fund` for details\n",
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run app.py &>/content/logs.txt &"
      ],
      "metadata": {
        "id": "wOBp6_GkEztT"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!npx localtunnel --port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vy37NHYoE4fo",
        "outputId": "b35fe12a-84d7-4db4-faf0-782d04d38134"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0Kyour url is: https://clear-eels-laugh.loca.lt\n",
            "^C\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "L5dR64Pfp2nX",
        "outputId": "c182dbc8-8222-4172-9e17-43e92f313bf4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Training Logistic Regression...\n",
            "Accuracy: 0.5500\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.67      0.71      0.69        14\n",
            "           1       0.20      0.17      0.18         6\n",
            "\n",
            "    accuracy                           0.55        20\n",
            "   macro avg       0.43      0.44      0.44        20\n",
            "weighted avg       0.53      0.55      0.54        20\n",
            "\n",
            "--------------------------------------------------\n",
            "Training Naïve Bayes...\n",
            "Accuracy: 0.6000\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.69      0.79      0.73        14\n",
            "           1       0.25      0.17      0.20         6\n",
            "\n",
            "    accuracy                           0.60        20\n",
            "   macro avg       0.47      0.48      0.47        20\n",
            "weighted avg       0.56      0.60      0.57        20\n",
            "\n",
            "--------------------------------------------------\n",
            "Training SVM...\n",
            "Accuracy: 0.6000\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.67      0.86      0.75        14\n",
            "           1       0.00      0.00      0.00         6\n",
            "\n",
            "    accuracy                           0.60        20\n",
            "   macro avg       0.33      0.43      0.38        20\n",
            "weighted avg       0.47      0.60      0.53        20\n",
            "\n",
            "--------------------------------------------------\n",
            "Training Random Forest...\n",
            "Accuracy: 0.5500\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.67      0.71      0.69        14\n",
            "           1       0.20      0.17      0.18         6\n",
            "\n",
            "    accuracy                           0.55        20\n",
            "   macro avg       0.43      0.44      0.44        20\n",
            "weighted avg       0.53      0.55      0.54        20\n",
            "\n",
            "--------------------------------------------------\n",
            "Training Gradient Boosting...\n",
            "Accuracy: 0.7000\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.79      0.79      0.79        14\n",
            "           1       0.50      0.50      0.50         6\n",
            "\n",
            "    accuracy                           0.70        20\n",
            "   macro avg       0.64      0.64      0.64        20\n",
            "weighted avg       0.70      0.70      0.70        20\n",
            "\n",
            "--------------------------------------------------\n",
            "Training XGBoost...\n",
            "Accuracy: 0.7500\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.85      0.79      0.81        14\n",
            "           1       0.57      0.67      0.62         6\n",
            "\n",
            "    accuracy                           0.75        20\n",
            "   macro avg       0.71      0.73      0.72        20\n",
            "weighted avg       0.76      0.75      0.75        20\n",
            "\n",
            "--------------------------------------------------\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.11/dist-packages/xgboost/core.py:158: UserWarning: [17:48:47] WARNING: /workspace/src/learner.cc:740: \n",
            "Parameters: { \"use_label_encoder\" } are not used.\n",
            "\n",
            "  warnings.warn(smsg, UserWarning)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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/sCBA/Lz81PVqlVd2kNDQxUSEqIDBw64tFeoUCFHHyVKlNCJEyc8jDinLl26KDY2Vo888ojKli2rrl27atGiRddMKi7HWaNGjRznatWqpf/97386e/asS/uV91KiRAlJcute7r//fgUGBuq9997TggUL1LBhwxy/5WXZ2dmaPHmyqlWrJrvdrltvvVWlS5fWDz/8oFOnTuV5zNtuu82thZX//ve/VbJkSaWnp+vVV19VmTJl8vxdAFdHIgGfFBQUpPDwcG3fvt2t71252PFqChUqlGu7YRgej3F5/v6ygIAArV69Wl9++aUefvhh/fDDD+rSpYvuvffeHNfeiBu5l8vsdrs6deqkuXPnaunSpVetRkjSiy++qISEBDVt2lRvv/220tLStHz5ckVGRua58iL9+fu4Y+vWrTpy5Igkadu2bW59F8DVkUjAZ7Vr10579+7V+vXrr3ttRESEsrOztXv3bpf233//XSdPnnTuwDBDiRIlXHY4XHZl1UOS/Pz81KJFC02aNEk//vijxo0bp5UrV+qrr77Kte/Lce7atSvHuf/+97+69dZbVaxYsRu7gavo3r27tm7dqjNnzuS6QPWyDz74QM2bN9ebb76prl27qlWrVmrZsmWO3ySvSV1enD17Vr1791bt2rX16KOPasKECdq0aZNp/QN/ZyQS8FnPPPOMihUrpkceeUS///57jvN79+7VK6+8IunP0rykHDsrJk2aJElq27ataXFVqVJFp06d0g8//OBsy8jI0NKlS12uO378eI7vXn4w05VbUi8LCwtT/fr1NXfuXJe/mLdv365ly5Y579MKzZs315gxYzRt2jSFhoZe9bpChQrlqHa8//77+u2331zaLic8uSVd7ho+fLgOHjyouXPnatKkSapYsaLi4+Ov+jsCyDseSAWfVaVKFS1cuFBdunRRrVq1XJ5suW7dOr3//vvq1auXJKlevXqKj4/XG2+8oZMnT6pZs2bauHGj5s6dqw4dOlx1a6EnunbtquHDh6tjx456+umnde7cOU2fPl3Vq1d3WWyYnJys1atXq23btoqIiNCRI0f0+uuvq1y5cmrcuPFV+3/55ZfVpk0bxcTEqG/fvjp//rymTp2q4OBgJSYmmnYfV/Lz89MLL7xw3evatWun5ORk9e7dW40aNdK2bdu0YMECVa5c2eW6KlWqKCQkRDNmzFBg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mqlZs2YKDw/XQw89pFOnTpkaHAAA+P9SUlIUHBzscqSkpFz3e6mpqTp58qR69eplekw242pv4rqKLl26aOvWrZo6dapiYmIkSevXr9fAgQNVv359vfvuu6YH6a4t+097OwSgQIosF+TtEIACx9/j2nze9Zifbko/b3Wu5VFFonXr1ipatKg+/vhjU+L4K7d/vk8++URpaWlq3Lixs61169aaNWuW7rvvPlODAwDAF5g1nZCXpOFKBw4c0JdffqklS5aYEsOV3J7aKFWqlIKDg3O0BwcHq0SJEqYEBQAAzDF79myVKVNGbdu2taR/txOJF154QQkJCTp8+LCz7fDhwxo2bJhGjhxpanAAAPgCbz2QKjs7W7Nnz1Z8fLwKF7ZmDidPvUZHR7uUZXbv3q0KFSqoQoUKkqSDBw/Kbrfr6NGjeuyxxywJFACAm5W33pPx5Zdf6uDBg+rTp49lY+QpkejQoYNlAQAA4Ov8vPR461atWsnNPRVuy1MiMXr0aEuDAAAAN6d82PQCAMDfW0F9BbgZ3E4ksrKyNHnyZC1atEgHDx7UxYsXXc4fP37ctOAAAPAFvptGeLBrIykpSZMmTVKXLl106tQpJSQkqFOnTvLz81NiYqIFIQIAgILK7URiwYIFmjVrloYMGaLChQurW7du+s9//qNRo0bp22+/tSJGAABuan42mylHQeR2InH48GFFRUVJkooXL+58v0a7du306aefmhsdAAA+wFvPkcgPbicS5cqVU0ZGhiSpSpUqWrZsmaQ/33vu7mM7AQDAzc3tRKJjx45asWKFJOmpp57SyJEjVa1aNfXs2dPSB14AAHCzstlsphwFkdu7NsaPH+/87126dFFERITWrVunatWqqX379qYGBwCALyigOYAp3K5IXOkf//iHEhISdNddd+nFF180IyYAAHCTuOFE4rKMjAxe2gUAQC58edcGT7YEAMBiBTQHMAWJBAAAFiuoCyXNYNrUBgAA+PvJc0UiISHhmuePHj16w8GYpXQQz7MAclOi4ZPeDgEocM5vnWb5GL78r/Y8JxJbt2697jVNmza9oWAAAPBFvjy1kedE4quvvrIyDgAAcBNisSUAABbz892CBIkEAABW8+VEwpfXfwAAAItRkQAAwGIstgQAAB5jauMK33zzjR566CHFxMTot99+kyTNnz9fa9asMTU4AABQsLmd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\n"
          },
          "metadata": {}
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import LabelEncoder, StandardScaler\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.naive_bayes import GaussianNB\n",
        "from sklearn.svm import SVC\n",
        "from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier\n",
        "from xgboost import XGBClassifier\n",
        "from sklearn.metrics import accuracy_score, classification_report\n",
        "from sklearn.metrics import confusion_matrix\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Load dataset\n",
        "file_path = \"Student Mental health.csv\"\n",
        "df = pd.read_csv(file_path)\n",
        "\n",
        "# Drop unnecessary columns (Timestamp is not useful for prediction)\n",
        "df = df.drop(columns=['Timestamp'])\n",
        "\n",
        "# Handle missing values (if any)\n",
        "df = df.dropna()\n",
        "\n",
        "# Encode categorical variables\n",
        "label_encoders = {}\n",
        "for col in df.columns:\n",
        "    if df[col].dtype == 'object':\n",
        "        le = LabelEncoder()\n",
        "        df[col] = le.fit_transform(df[col])\n",
        "        label_encoders[col] = le  # Store encoders for later use\n",
        "\n",
        "# Define features and target variable\n",
        "#X = df.drop(columns=['Do you have Depression?'])  # Features\n",
        "#y = df['Do you have Depression?']  # Target\n",
        "\n",
        "X = df.drop(columns=['Do you have Anxiety?'])  # Features\n",
        "y = df['Do you have Anxiety?']  # Target\n",
        "\n",
        "# Split dataset into training (80%) and testing (20%)\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "\n",
        "# Standardize features for models that need it\n",
        "scaler = StandardScaler()\n",
        "X_train_scaled = scaler.fit_transform(X_train)\n",
        "X_test_scaled = scaler.transform(X_test)\n",
        "\n",
        "# Define models\n",
        "models = {\n",
        "    'Logistic Regression': LogisticRegression(),\n",
        "    'Naïve Bayes': GaussianNB(),\n",
        "    'SVM': SVC(),\n",
        "    'Random Forest': RandomForestClassifier(n_estimators=100),\n",
        "    'Gradient Boosting': GradientBoostingClassifier(n_estimators=100),\n",
        "    'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss')\n",
        "}\n",
        "\n",
        "# Train and evaluate models\n",
        "for name, model in models.items():\n",
        "    print(f\"Training {name}...\")\n",
        "    if name in ['Logistic Regression', 'SVM']:  # Models that need scaled data\n",
        "        model.fit(X_train_scaled, y_train)\n",
        "        y_pred = model.predict(X_test_scaled)\n",
        "    else:\n",
        "        model.fit(X_train, y_train)\n",
        "        y_pred = model.predict(X_test)\n",
        "\n",
        "    # Print accuracy and classification report\n",
        "    print(f\"Accuracy: {accuracy_score(y_test, y_pred):.4f}\")\n",
        "    print(classification_report(y_test, y_pred))\n",
        "    print(\"-\" * 50)\n",
        "# Membuat confusion matrix\n",
        "#cm = confusion_matrix(y_test, y_pred, labels=[\"Yes\", \"No\"])\n",
        "cm = confusion_matrix(y_test, y_pred, labels=[1, 0])\n",
        "\n",
        "# Menampilkan confusion matrix dengan heatmap\n",
        "sns.heatmap(cm, annot=True, fmt=\"d\", cmap=\"Blues\", xticklabels=[\"Yes\", \"No\"], yticklabels=[\"Yes\", \"No\"])\n",
        "plt.xlabel(\"Predicted Label\")\n",
        "plt.ylabel(\"True Label\")\n",
        "plt.title(\"Confusion Matrix\")\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_test"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 711
        },
        "id": "kifGySqfzd1g",
        "outputId": "98ae6914-596f-4f97-94b7-616b76e08abf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "84    0\n",
              "54    0\n",
              "71    0\n",
              "46    1\n",
              "45    1\n",
              "39    0\n",
              "22    0\n",
              "81    0\n",
              "10    0\n",
              "0     0\n",
              "18    1\n",
              "30    0\n",
              "74    1\n",
              "33    1\n",
              "91    1\n",
              "4     0\n",
              "77    0\n",
              "78    0\n",
              "12    0\n",
              "31    0\n",
              "Name: Do you have Anxiety?, dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Do you have Anxiety?</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>84</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>54</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>71</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>46</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>39</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>81</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>74</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>33</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>91</th>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>77</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>78</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>31</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    }
  ]
}