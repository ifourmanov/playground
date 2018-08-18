#!/bin/bash
for I in {1..4} 
do
  echo test$I > somefile.log.$I
done
echo test > somefile.log
