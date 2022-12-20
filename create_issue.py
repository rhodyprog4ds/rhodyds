# dev script
import pandas as pd
import yaml as yml


def yml_df(file):
    with open(file, 'r') as f:
        file_unparsed = f.read()
    file_dict = yml.safe_load(file_unparsed)
    return pd.DataFrame(file_dict)

# TODO: fix year site
ach = yml_df('../BrownFall22/_data/achievments.yml')

'\n - [ ] '.join(['']+ach['components'][0])


with open ('issue_tmplt.yml','r') as tmpt_f:
    yml_ic_template = tmpt_f.read()


with open ('issue_head.yml','r') as tmpt_f:
    action_head = tmpt_f.read()


def issue_action_str(row):
    rep_dict = {}
    if type(row['components']) ==list:
        rep_dict['components_checklist'] = '\n            - [ ] '.join(['']+row['components'])
    else:
        rep_dict['components_checklist'] = ''
    rep_dict['name'] = row['name']
    rep_dict['description'] = row['description']
    return yml_ic_template.format_map(rep_dict)

all_issues = ach.apply(issue_action_str,axis=1).values)
grading_issue_action = '\n'.join([action_head]+list(all_issues)).replace('{','{{').replace('}','}}')


with open('grading_issues.yml', 'w') as gi_file:
    gi_file.write(grading_issue_action)
