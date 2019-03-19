import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

current_dir = '/home/edward/Documents/Kuliah/TA-D4TI-06/Produk/dark/Images/002'
new_dir    = 'Images/002'
# Directory where the data will reside, relative to 'darknet.exe'
#path_data = './NFPAdataset/'

# Percentage of images to be used for the test set
percentage_test = 20;

# Create and/or truncate train.txt and test.txt
file_train = open('train2.txt', 'w')
file_test = open('test2.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(new_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(new_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1
