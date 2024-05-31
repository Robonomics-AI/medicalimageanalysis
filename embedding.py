import base64
import json


def get_image_embedding():
    with open("ColorRx-English-Logo-HTWT-Generics.png", "rb") as f:
        encoded_image = base64.b64encode(f.read()).decode('utf-8')
        print(encoded_image)
        with open("output.json", "w") as outfile:
            json.dump({"base_64_encoding": encoded_image}, outfile, indent=4)
    return json.dumps({"base_64_encoding": encoded_image})


if __name__ == '__main__':
    get_image_embedding()
