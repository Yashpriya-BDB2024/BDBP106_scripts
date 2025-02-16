#!/bin/bash
#Function to delete a file
delete_file () {
read -p "Enter the file name:" file
if [ -f "$file" ]; then
rm -rf "$file"
else 
echo "Its not a file; enter correct existing file name"
fi
}
#Copy the file to filename.bak
copy_file () {
read -p "Enter the file name:" file_name
if [ -f "$file_name" ]; then
cp "$file_name" "$file_name.bak"
else
echo "Its not a file; enter the correct existing file name"
fi
}
#Rename the given file by using the given new name
rename_file () {
read -p "Enter the file name:" File
read -p "Enter the new name of the file with extension:" new_name
if [ -f "$File" ]; then
mv "$File" "$new_name"
else
echo "The file has been renamed successfully."
fi
}
#Create a new file 
create_file () {
read -p "Enter the new file name without extension:" New_Name
touch "$New_Name.txt"
echo "New file has been created"
}
#List the files present in the given directory
list_files () {
read -p "Enter the directory name:" Dir
if [ -d "$Dir" ]; then
ls "$Dir"
else
echo "Error: Its not a valid directory"
fi
}
#Help - Display the information regarding all the operations
display_help () {
echo "delete  - Delete a file"
echo "copy    - Copy a file to .bak file"
echo "rename  - Rename a file"
echo "create  - Create a new file"
echo "list    - List files in a directory"
echo "help    - Display this help message"
}
#check if atleast one operation argument is provided
if [ $# -eq 0 ]; then
echo "No operation specified"
exit 1
fi
file_operation="$1"
case "$file_operation" in
  delete)
      delete_file
      ;;
   copy)
      copy_file
      ;;
    rename)
      rename_file
      ;;
    create)
       create_file
       ;;
    list)
      list_files
      ;;
    help)
      display_help
      ;;
    *)
  esac

