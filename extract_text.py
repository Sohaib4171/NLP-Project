# required libraries
import pandas as pd
from pdfminer.layout import LAParams
from pdfminer import high_level
import PyPDF2
from tika import parser

# csv files
train = pd.read_csv('dataset/train.csv')
# test = pd.read_csv('dataset/test.csv')
test=pd.read_csv('predictionData/predict.csv')

#paths
train_path = "dataset/trainResumes/"
# test_path = "dataset/testResumes/"
test_path="predictionData/predictResumes/"

# epty list for resumes text
train_resumes = []
test_resumes = []

# ids
ids = list(train.CandidateID)
test_ids = list(test.CandidateID)

# pdf2string
def pdf2string_train(path, ids, resumes):
    for i in ids:
        main_path = path+i+'.pdf'
        # text = high_level.extract_text(main_path)
        parsed_pdf = parser.from_file(main_path)
        text=parsed_pdf['content']
        str_list = text.split()
        str_list = str_list[:]
        string = ' '.join(str_list)
        resumes.append(string)
        

def pdf2string_test(path, test_ids, resumes):
    for i in test_ids:
        main_path = path+i+'.pdf'
        parsed_pdf = parser.from_file(main_path)
        text=parsed_pdf['content']
        # text = high_level.extract_text(main_path)
        str_list = text.split()
        str_list = str_list[:]
        string = ' '.join(str_list)
        resumes.append(string)


pdf2string_train(train_path, ids, train_resumes)
pdf2string_test(test_path,  test_ids, test_resumes)

print(train_resumes[0])
print('==================')
print(test_resumes[0])