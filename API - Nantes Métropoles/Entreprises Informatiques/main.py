import requests
import json


def callApi(url, param=""):
    r = requests.get(url, param)
    if r.status_code != 200:
        raise Exception("GET /challenges/ {}".format(r.status_code))
    data = r.json()
    print(data['denomationusuelleetablissement'])

    return


def main():
    url = "https://data.nantesmetropole.fr/api/records/1.0/search/?dataset=244400404_base-sirene-entreprises-nantes-metropole&rows=50&q=classeetablissement=%27Programmation%20Informatique%27"
    param = ""
    callApi(url, param)

    return


if __name__ == "__main__":
    print("DÉBUT \n ---------")
    main()
    print("-------- \n FIN")
