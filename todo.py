#!/usr/bin/python

import sys, getopt

def listTodo(inputfile):
  

def main(argv):
  inputfile = '~/todo.txt'
  action = 'meow'
  try:
    opts, args = getopt.getopt(argv, "i:l", ["ifile=","list"])
  except getopt.GetoptError:
    print 'todo -h'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'help for h'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-l", "==list"):
      action = 'list'
  print 'input file is "', inputfile

if __name__ == "__main__":
  main(sys.argv[1:])
