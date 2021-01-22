import os
import json
import requests

def generate_catalog(package_name: str):
    repo_root = "http://repo.x-i-a.com/library"
    result_json = {"package": {"name": package_name, "version": ""},
                   "modules": [], "connectors": []}
    package_path = os.path.join("..", "library", package_name)
    connector_path = os.path.join( package_path, "connectors")
    module_path = os.path.join( package_path, "modules")
    for filename in os.listdir(connector_path):
        with open(os.path.join(connector_path, filename), "r") as fp:
            connector_detail = json.load(fp)
            connector_name = filename.replace("_", "-")[:-5]
            connector_title = connector_detail['title']
            connector_ref = "/".join([repo_root, package_name, "connectors", filename])
            connector = {"name": connector_name, "title": connector_title, "ref": connector_ref}
            result_json["connectors"].append(connector)

    for filename in os.listdir(module_path):
        with open(os.path.join(module_path, filename), "r") as fp:
            module_detail = json.load(fp)
            module_name = ''.join([s.title() for s in filename[:-5].split('_')])
            module_title = module_detail['title']
            module_ref = "/".join([repo_root, package_name, "modules", filename])
            module = {"name": module_name, "title": module_title, "ref": module_ref}
            result_json["modules"].append(module)

    with open(os.path.join( package_path, 'catalog.json'), 'w') as fp:
        json.dump(result_json, fp, ensure_ascii=False, indent=2)


# print(generate_catalog("xialib"))

#generate_catalog("xialib")
generate_catalog("xialib-firestore")
generate_catalog("xialib-gcs")
generate_catalog("xialib-pubsub")
#resp = requests.get("http://repo.x-i-a.com/library/xialib-pubsub/catalog.json")
#print(resp.json())