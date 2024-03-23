import datasets


# sake_qa_list
# input: Question
# output: Answer
sake_qa_list = []

sake_data = datasets.load_dataset("json", data_files = "json/sake_dataset_v1.jsonl")
for i in range(len(sake_data['train'])):
    sake = sake_data['train'][i]
    prefecture = sake['prefecture']
    city = sake['city']
    place = f"{prefecture}{city}"
    brewer = sake['brewer']
    name = sake['brand+name']

    qa_type = "place"
    question_1 = f"{name}はどこで作られているお酒ですか？"
    answer_1 = f"{prefecture}{city}"
    qa_1 = {
        "input": question_1,
        "output": answer_1,
        "type": qa_type
    }
    sake_qa_list.append(qa_1)

    qa_type = "brewer"
    question_2 = f"{name}はどの酒蔵で作られているお酒ですか？"
    answer_2 = f"{brewer}"
    qa_2 = {
        "input": question_2,
        "output": answer_2,
        "type": qa_type
    }
    sake_qa_list.append(qa_2)

    qa_type = "name"
    question_3 = f"{place}で作られているお酒の名前は何ですか？"
    answer_3 = f"{name}"
    qa_3 = {
        "input": question_3,
        "output": answer_3,
        "type": qa_type
    }
    sake_qa_list.append(qa_3)

    qa_type = "name"
    question_4 = f"{brewer}が作っているお酒の名前は何ですか？"
    answer_4 = f"{name}"
    qa_4 = {
        "input": question_4,
        "output": answer_4,
        "type": qa_type
    }
    sake_qa_list.append(qa_4)

sake_qa_dataset = datasets.Dataset.from_list(sake_qa_list)
print(sake_qa_dataset)

sake_qa_dataset.push_to_hub("yuiseki/sake_qa")
