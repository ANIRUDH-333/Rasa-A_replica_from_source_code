from rasa.model_training import train
from rasa.cli.shell import shell_nlu
from rasa.cli.shell import shell
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m' , '--model' ,type = str )
#parser.add_argument('-e' , '--endpoints' , type = str)
#parser.add_argument('-cr' , '--credentials' , type = str)

shell_nlu(parser.parse_args())


