import json
import os
import sys
import argparse

def __unity_type_map(param_input_type, param_json_key, param_existing_classes):
    param_json_key = param_json_key.title()

    input_type = param_input_type

    unity_type = ""

    unity_type_map = {
        dict: "{0}ObjectResponse".format(param_json_key),
        int: "int",
        str: "string",
        float: "float",
        bool: "bool",
    }
    if type(input_type) is list:
        input_type = input_type[0]
        if type(input_type) is dict:
            __create_unity_class(input_type, param_json_key, param_existing_classes)
        unity_type = "{0}[]".format(
            __unity_type_map(input_type, param_json_key, param_existing_classes)
        )
    else:
        unity_type = unity_type_map[type(input_type)]

    return unity_type


def __create_classes_file(param_file_name, param_json_data, param_path):
    file_name = "{0}/{1}.cs".format(param_path, param_file_name)
    if not os.path.exists(os.path.dirname(file_name)):
        try:
            os.makedirs(os.path.dirname(file_name))
        except:
            print("error")
    class_file = open(file_name, "w+")
    class_file_content = __create_classes_file_content(param_json_data, param_file_name)
    class_file.write(class_file_content)
    class_file.close()


def __create_unity_class(param_json_data, param_json_key, param_existing_classes):
    response_class = {"name": "{0}".format(param_json_key), "attributes": []}
    for key in param_json_data:
        value = __unity_type_map(param_json_data[key], key, param_existing_classes)
        if type(param_json_data[key]) is dict:
            __create_unity_class(
                param_json_data=param_json_data[key],
                param_json_key=key,
                param_existing_classes=param_existing_classes,
            )
        attribute = {"name": key, "value": value}
        response_class.get("attributes").append(attribute)
    param_existing_classes.append(response_class)


def __create_classes_file_content(param_json_data, param_file_name):
    content = ""

    classes = []

    response_class = {"name": param_file_name, "attributes": []}

    for key in param_json_data:
        value = __unity_type_map(param_json_data[key], key, classes)
        if type(param_json_data[key]) is dict:
            __create_unity_class(
                param_json_data=param_json_data[key],
                param_json_key=key,
                param_existing_classes=classes,
            )
        attribute = {"name": key, "value": value}
        response_class.get("attributes").append(attribute)
    classes.append(response_class)
    content += "using System;\n"
    content += "namespace {0}Namespace".format(response_class.get("name"))
    content += "{\n"
    class_attr = []
    for c in classes:
        content += "\n    [Serializable]\n"
        content += "    public class {0}ObjectResponse\n".format(c.get("name").title())
        content += "    {\n"
        for a in c.get("attributes"):
            class_attr.append(
                "       public {0} {1};".format(a.get("value"), a.get("name"))
            )
        content += "\n".join(class_attr)
        content += "\n    }\n"
        class_attr = []
    content += "\n}\n"
    return content


def create_json_response_classes(
    param_input_file_name, param_output_file_name, param_output_file_path
):
    with open(param_input_file_name) as json_file:
        data = json.load(json_file)
        __create_classes_file(
            param_file_name=param_output_file_name,
            param_json_data=data,
            param_path=param_output_file_path,
        )

input_parser = argparse.ArgumentParser()

input_parser.add_argument("-f", "--File", help="e.x. -f SomeFile.json", required=True)
input_parser.add_argument("-p", "--Path", help="e.x. -p ~/SomeProject/", required=False, default="./")

input_args = input_parser.parse_args()

if input_args.File:
    json_file = input_args.File
if input_args.Path:
    output_path = input_args.Path

class_name = json_file.split(".json")[0]
create_json_response_classes(json_file, class_name, output_path)
