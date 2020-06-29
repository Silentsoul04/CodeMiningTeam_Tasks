# -*- coding: utf-8 -*-

"""
Created on 2020-06-29 21:39  

@author: congyingxu

用于生成包含全部 train、validate、test的数据集
其中。按照5:1:1分配
"""

from CommonFunction import File_processing
all_train = ""
all_valid = ""
all_test = ""


folder = 'Dataset/ner_data/'

def main():
    global all_test, all_train, all_valid, folder

    # read
    all_train_list = File_processing.read_TXTfile(folder + 'memc_train.txt').split('\n\n')
    all_valid_list = File_processing.read_TXTfile(folder + 'memc_valid.txt').split('\n\n')
    all_test_list = File_processing.read_TXTfile(folder + 'memc_test.txt').split('\n\n')
    print(len(all_train_list),len(all_valid_list),len(all_test_list))

    completed_categ = []
    file_names = File_processing.walk_L1_FileNames(folder)
    for file_name in file_names:
        categ_name = file_name.split('_')[0]


        if file_name.startswith('memc_') or file_name.startswith('.') or file_name.startswith('all_') or categ_name in completed_categ:
            continue
        else:
            print('categ_name', categ_name)
            # read test
            test_dataset_list = File_processing.read_TXTfile(folder + categ_name +'_test.txt').split('\n\n')
            train_dataset_list = File_processing.read_TXTfile(folder + categ_name + '_train.txt').split('\n\n')

            # test_dataset_list.extend(train_dataset_list)
            cate_dataset =  test_dataset_list + train_dataset_list
            len_cate_dataset = len(cate_dataset)

            # print(train_dataset_list)
            # print(test_dataset_list)

            # extent dataset list
            all_train_list.extend( cate_dataset[:int(len_cate_dataset *5/7)] )
            all_valid_list.extend( cate_dataset[int(len_cate_dataset *5/7) : int(len_cate_dataset *6/7)] )
            all_test_list.extend( cate_dataset[int(len_cate_dataset *6/7) : ] )
            print(len(all_train_list), len(all_valid_list), len(all_test_list))

        completed_categ.append(categ_name)


    # write
    # org txt
    for ele in all_train_list:
        all_train += ele + '\n\n'
    for ele in all_valid_list:
        all_valid += ele + '\n\n'
    for ele in all_test_list:
        all_test += ele + '\n\n'

    File_processing.write_TXTfile(folder + 'all_train.txt',all_train)
    File_processing.write_TXTfile(folder + 'all_valid.txt', all_valid)
    File_processing.write_TXTfile(folder + 'all_test.txt',all_test)

if __name__ == '__main__':
    main()
    print()

