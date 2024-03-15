echo "Running the program with the NASA file"
echo "Available scripts:"

ls Lab1and2/*.py

read -p "Write down file with extension and params: " file

path_to_file=$PWD/Lab1and2/NASA.txt
path_to_script=$PWD/Lab1and2/$file
python $path_to_script $@ < $path_to_file


echo "End of the program"
