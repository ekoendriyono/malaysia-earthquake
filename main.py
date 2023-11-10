import popularnews

if __name__ == '__main__':
    print('My Aplication')
    result= popularnews.extraction()
    popularnews.show_data(result)