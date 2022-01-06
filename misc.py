import json

def restore_json():

# print("Editing json file...")
# with open('database\example_database.json', 'r+') as file:
#     file_data = json.load(file)
#     file_data["appKeys"].append("I Love Pizza")
#     file.seek(0)
#     json.dump("I Love Pizza", file, indent = 4)
# time.sleep(5)
    print("Restoring json database...")

    with open('database\example_database_backup.json', 'r') as backup:
        backup_data = json.load(backup)

        with open('database\example_database.json', 'w') as newfile:
            json.dump(backup_data, newfile, indent = 4)


def restore_log():
    print("clearing log file...")
    with open('log\output.log', 'w') as file:
        file.write("---CEILING---")
