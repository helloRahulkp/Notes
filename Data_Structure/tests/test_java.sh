#!/bin/bash
# Simple script to run Java tests
find ../Java -name "*.java" > sources.txt
javac @sources.txt && java org.junit.runner.JUnitCore TestAVLTree