# open a file
# (w = write r+ = read and write r = read by default a = append)
# w will create new file if there is no file to overwrite.
yoel_file = open('yoel.txt', 'a')

numbers = [7, 7, 0]
for i in range(len(numbers)):
    num = numbers[i]
    yoel_file.write("{}\n".format(num))

# write to the file
# yoel_file.write('\nHello\n')
# close a file [do not forget]
yoel_file.close()

# read a file
# print(yoel_file.read())

# Look up how to read lines from a file in python
new_file = open('new_file.txt')
file_items = new_file.readlines()

for i in range(len(file_items)):
    each_item = file_items[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])
    file_items[i] = each_item[0:-1]
    print(file_items)

# print(file_items)

new_file.close()

# add logic last letter cut off for new file
