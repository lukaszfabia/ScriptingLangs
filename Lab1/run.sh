echo "Running the program with the NASA file"
echo "Available scripts:"

ls Lab1/*.py

read -p "Write down file with extension and params: " file

path_to_file=$PWD/Lab1/NASA.txt
path_to_script=$PWD/Lab1/$file
python $path_to_script $@ < $path_to_file


echo "End of the program"
