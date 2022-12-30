import pandas as pd
import os 
import json
import sys
import shutil

def parse_row(row):
    mask = row.index.isin(["output_id"])
    culled_row = row[~mask]
    culled_row_lists = culled_row.apply(parse_string)
    
    index_arr_of_arrs = [[name + "_1", name + "_2", name + "_3"] for name in culled_row.index]
    index_arr = ["output_id"] + [elt for clump in index_arr_of_arrs for elt in clump]
    content_arr = [row["output_id"]] + [grid for entry in culled_row_lists for grid in entry]

    new_row_series = pd.Series(content_arr, index_arr)

    return new_row_series
    

def parse_string(pred_string):
    list_of_pred_strings = pred_string.split(" ")
    list_of_pred_strings = [elt for elt in list_of_pred_strings if elt != ""]
    list_of_pred_lists = [[elt for elt in arr.split("|") if elt != ""] for arr in list_of_pred_strings]
    list_of_pred_arrs = [[[int(n) for n in row] for row in lst] for lst in list_of_pred_lists]

    while len(list_of_pred_arrs) < 3:
        list_of_pred_arrs.append([[0]]) # add a single black square as the prediction
    
    return list_of_pred_arrs

def score(sub_table, solver_list):
    for solver in solver_list:
        sub_table[solver + '_correct'], sub_table[solver + '_correct_indices']= zip(*sub_table.apply(lambda row: score_row(row, solver), axis=1))

def get_problem(row):
    problem_file = row["problem_file"]
    with open(os.path.join(dataset, problem_file)) as problem:
        problem = json.load(problem)
    
    return problem, row["index"]

def score_row(row, solver_name):
    problem, index = get_problem(row)
    correct_answer = problem["test"][index]["output"]
    index_string = ""
    for guess_index in range(1,4):
        index_string = index_string + str(guess_index) + ", " if row[solver_name + "_" + str(guess_index)] == correct_answer else index_string
    
    if index_string != "":
        index_string = index_string[:-2]
        return (True, index_string)
    else:
        return (False, index_string)

def add_problem_info(sub_table):
    sub_table['problem_file'] = sub_table.apply(lambda x: f'{x["output_id"].split("_")[0]}.json', axis=1)
    sub_table['index'] = sub_table.apply(lambda x: int(x["output_id"].split("_")[1]), axis=1)

def gen_suggestions(row, solver_list, output_name):
    problem, index = get_problem(row)
    correct_answer = problem["test"][index]["output"]

    for solver in solver_list:   
        suggested_answers = [correct_answer] + list(row[[solver + "_1", solver + "_2", solver + "_3"]])

        stimulus = problem["test"][index]["input"]
        problem["test"] = []

        for suggested_answer in suggested_answers:
            problem["test"].append({
                "input": stimulus,
                "output": suggested_answer
            })
        
        suggestion_dir = os.path.join("output", output_name, f"{solver}_{output_name}")

        if not os.path.isdir(suggestion_dir):
            os.mkdir(suggestion_dir)
        
        with open(os.path.join(suggestion_dir, f'{row["output_id"]}.json'), 'w') as suggestion_file:
            json.dump(problem, suggestion_file, indent=4)


if __name__ == "__main__":
    # if the name of the dataset was given
    if len(sys.argv) > 1:
        dataset = sys.argv[1]
    else:
        dataset = "arc-datasets/small_dataset_0"

    # if the name of the input file (the submission file to score) was given
    if len(sys.argv) > 2:
        submission_name = sys.argv[2]
    else:
        submission_name = "output/submission.csv"
    
    # if the name of the output file (the name of the zip file in which both the output json and the score csv will be stored) was given
    if len(sys.argv) > 3:
        output_name = sys.argv[3]
    else:
        output_name = os.path.basename(submission_name).split(".")[0]

    full_filename = os.path.join("output", output_name)
    
    sub_table = pd.read_csv(submission_name)
    solver_list = [col for col in sub_table.columns if col != "output_id"]


    # parse table and add necessary columns
    parsed_table = sub_table.apply(parse_row, axis=1)
    add_problem_info(parsed_table)

    # generate visualizable answer suggestions
    if not os.path.isdir("output"):
        os.mkdir("output")
    if not os.path.isdir(full_filename):
        os.mkdir(full_filename)

    parsed_table.apply(lambda row: gen_suggestions(row, solver_list, output_name), axis=1)

    # scoring
    score(parsed_table, solver_list)
    index_list = ["problem_file", "index"] + \
                    [solver + "_correct" for solver in solver_list] + \
                    [solver + "_indices" for solver in solver_list]
    score_table = parsed_table[index_list]
    score_table.to_csv(os.path.join(full_filename, f"{output_name}.csv"))

    shutil.make_archive(full_filename, 'zip', full_filename)
    shutil.rmtree(full_filename)
    