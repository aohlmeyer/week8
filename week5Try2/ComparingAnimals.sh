#!/bin/bash
 
animal=" cat fish mouse gerbil bird snake lizard dog"

for animal in $animal
do

	echo "Some people have a "$animal" as a pet."
done

if [ $@ = dog ]
then
	echo "Dogs are the best!"
else
	echo "However, dogs are the best." 
fi

