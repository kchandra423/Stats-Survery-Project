import csv

import matplotlib.pyplot
from matplotlib import pyplot as plt
import numpy as np


def plot_replacements(bars: list):
    f, ax = plt.subplots()
    title = 'Teacher opinion on possible replacements'
    prev = None
    for bar in bars:
        plt.bar(np.array(list(bar.keys())), np.array(list(bar.values())), bottom=prev)
        if prev is not None:
            prev += np.array(list(bar.values()))
        else:
            prev = np.array(list(bar.values()))
    plt.legend(["Math and CS", "English", "Science", "Social Studies", "World Language", "Other"])

    # plt.bar(np.array(list(bars.keys())), np.array(list(bars.values())))
    plt.xlabel('Replacement Idea', fontsize=14)
    plt.title(title, fontsize=20)
    plt.ylabel('Count', fontsize=14)
    f.set_figwidth(13)
    plt.savefig(f'graphs/{title}')
    plt.show()


# [ { response : amount, response : amount, response: amount}
#   repeat for all 3
# ]
def plot_opinions(bars: list, x_label: str = None, y_label: str = None, title: str = None, figsize=(5, 5),
                  fontsize=14):
    f, ax = plt.subplots(figsize=figsize)
    prev = None
    for bar in bars:
        plt.bar(np.array(list(bar.keys())), np.array(list(bar.values())), bottom=prev)
        if prev is not None:
            prev += np.array(list(bar.values()))
        else:
            prev = np.array(list(bar.values()))
    plt.legend(["Math and CS", "English", "Science", "Social Studies", "World Language", "Other"])
    f.set_figwidth(12)
    f.set_figheight(10)
    matplotlib.pyplot.ylim(top=11)

    if x_label is not None and type(x_label) is str:
        plt.xlabel(x_label, fontsize=fontsize)
    if y_label is not None and type(y_label) is str:
        plt.ylabel(y_label, fontsize=fontsize)
    if title is not None and type(title) is str:
        plt.title(title, fontsize=20)
    plt.savefig(f'graphs/{title}.png')
    plt.show()


def standardize_email(teacher: str) -> str:
    teacher = teacher.replace('@fuhsd.org', '')
    return teacher.replace("_", " ").lower()


def standardize(teacher: str) -> str:
    teacher = teacher.replace(',', '')
    return teacher.lower()


def get_teachers_emails(file_name: str) -> set:
    x = set()
    with open(file_name, 'r') as f:
        lines = f.read().split('\n')
        for row in lines:
            x.add(standardize_email(row))
    return x


def get_teachers(file_name: str) -> set:
    x = set()
    with open(file_name, 'r') as f:
        lines = f.read().split('\n')
        for row in lines:
            x.add(standardize(row))
    return x


def find_replacement_amounts(group: dict, replacements: dict):
    for response in group.values():
        # opinions[response[0]] += 1
        if response[1] != '':
            replacements[response[1]] += 1


def find_amounts(group: dict, opinions: dict):
    for response in group.values():
        opinions[response[0]] += 1
        # if response[1] != '':
        #     replacements[response[1]] += 1


def get_default() -> dict:
    return {'Strongly Disapprove': 0, 'Moderately Disapprove': 0, 'Neutral': 0, 'Moderately Approve': 0,
            'Strongly Approve': 0}


def get_replacements() -> dict:
    return {'Monday skinny': 0, 'Friday skinny': 0, 'Alternating': 0,
            'Longer days, no/short fifth': 0,
            'Longer year, no/short fifth': 0}


def find_replacement_data():
    math_cs = {}
    english = {}
    science = {}
    social_studies = {}
    world_language = {}
    other = {}
    with open('res/all.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        label = True
        for row in csv_reader:
            if label:
                label = False
                continue
            name = standardize_email(row[1])
            if name in math_cs_teachers:
                math_cs[name] = (row[2], row[3])
            elif name in english_teachers:
                english[name] = (row[2], row[3])
            elif name in science_teachers:
                science[name] = (row[2], row[3])
            elif name in social_studies_teachers:
                social_studies[name] = (row[2], row[3])
            elif name in world_language_teachers:
                world_language[name] = (row[2], row[3])
            else:
                other[name] = (row[2], row[3])

    math_cs_replacements = get_replacements()
    find_replacement_amounts(math_cs, math_cs_replacements)
    all_replacements.append(math_cs_replacements)

    english_replacements = get_replacements()
    find_replacement_amounts(english, english_replacements)
    all_replacements.append(english_replacements)

    science_replacements = get_replacements()
    find_replacement_amounts(science, science_replacements)
    all_replacements.append(science_replacements)

    social_studies_replacements = get_replacements()
    find_replacement_amounts(social_studies, social_studies_replacements)
    all_replacements.append(social_studies_replacements)

    world_language_replacements = get_replacements()
    find_replacement_amounts(world_language, world_language_replacements)
    all_replacements.append(world_language_replacements)

    other_replacements = get_replacements()
    find_replacement_amounts(other, other_replacements)
    all_replacements.append(other_replacements)


def plot_data_for_opinions(csvfile: str, treatment: str):
    math_cs = {}
    english = {}
    science = {}
    social_studies = {}
    world_language = {}
    other = {}
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file)
        label = True
        for row in csv_reader:
            if label:
                label = False
                continue
            name = standardize_email(row[1])
            if name in math_cs_teachers:
                math_cs[name] = (row[2], row[3])
            elif name in english_teachers:
                english[name] = (row[2], row[3])
            elif name in science_teachers:
                science[name] = (row[2], row[3])
            elif name in social_studies_teachers:
                social_studies[name] = (row[2], row[3])
            elif name in world_language_teachers:
                world_language[name] = (row[2], row[3])
            else:
                other[name] = (row[2], row[3])
            if 'Control' in csvfile and name in control:
                control.remove(name)
            if 'Different' in csvfile and name in dif_word:
                dif_word.remove(name)
            if 'Additional' in csvfile and name in additional_info:
                additional_info.remove(name)

    math_cs_opinions = get_default()
    find_amounts(math_cs, math_cs_opinions)

    english_opinions = get_default()
    find_amounts(english, english_opinions)

    science_opinions = get_default()
    find_amounts(science, science_opinions)

    social_studies_opinions = get_default()
    find_amounts(social_studies, social_studies_opinions)

    world_language_opinions = get_default()
    find_amounts(world_language, world_language_opinions)

    other_opinions = get_default()
    find_amounts(other, other_opinions)

    plot_opinions(
        [math_cs_opinions, english_opinions, science_opinions, social_studies_opinions, world_language_opinions,
         other_opinions], x_label="Teacher Opinion",
        y_label="Count",
        title=f"Teacher opinion on removing Wednesday Skinny days ({treatment})")


# def turn_into_email(name: str) -> str:
#     return name.replace(' ', '_') + '@fuhsd.org'


if __name__ == '__main__':
    math_cs_teachers = get_teachers("res/teachers/math_and_compsci_teachers.txt")
    english_teachers = get_teachers("res/teachers/english_teachers.txt")
    social_studies_teachers = get_teachers("res/teachers/social_studies_teachers.txt")
    science_teachers = get_teachers("res/teachers/science_teachers.txt")
    world_language_teachers = get_teachers("res/teachers/world_language_teachers.txt")
    all_replacements = []
    control = get_teachers_emails('res/control_email_list.txt')
    dif_word = get_teachers_emails('res/diferent_wording_email_list.txt')
    additional_info = get_teachers_emails('res/additional_info_email_list.txt')

    find_replacement_data()
    plot_data_for_opinions('res/Survey - Control Responses.csv', 'Control')
    plot_data_for_opinions('res/Survey - Additional Information.csv', 'Additional Information')
    plot_data_for_opinions('res/Survey - Different Wording.csv', 'Different Wording')
    plot_replacements(all_replacements)
    # print(control)
    # print(dif_word)
    # print(additional_info)
