#!/bin/bash
read -p "Enter the name of the source directory:" source
read -p "Enter the name of the destination directory:" destination
cp -r $source/* $destination 
